"""Defines loss for multiple instance learning (MIL)."""

import torch
import torch.nn.functional as F
from sparsemax import Sparsemax


def mil_score(outputs, joint_probability=None, sparse=None):
    """Computes box-wise MIL score.

    The MIL score is the elementwise product of the detection and
    classification softmax scores. We optionally sparsemax over
    the detections dimension, which typically increases performance.
    """

    if joint_probability:
        dets_logits = inverse_sigmoid(torch.stack(outputs["obj_confs"]))
    else:
        dets_logits = outputs["det_logits"]

    # Softmaxes over the classes dimension.
    classes_logits = outputs["pred_logits"]
    classes = F.softmax(classes_logits, dim=2)

    # Computes detection sigmoid as proxy for detection confidence.
    dets_sigmoid = dets_logits.sigmoid()

    # Softmaxes or sparsemaxes over the detections dimension.
    if sparse:
        dets = Sparsemax(dim=1)(dets_logits)
    else:
        dets = F.softmax(dets_logits, dim=1)

    if joint_probability:
        num_classes = classes.shape[-1]
        dets = dets.unsqueeze(-1).repeat(1, 1, num_classes)

    # Computes element-wise product of the two scores.
    scores = classes * dets

    return dets_sigmoid, scores


def mil_label(batch_size, num_classes, targets, offset=0):
    """Gets the weak supervision label for MIL.

    There is a 1 in the class slot if there is
    at least one instance of that class in the image.
    """

    # Creates empty tensor for MIL labels.
    mil_labels = torch.zeros((batch_size, num_classes)).to(torch.device("cuda"))

    # Populates MIL label from targets.
    for j, img_target in enumerate(targets):
        for instance in img_target:
            cls = instance["category_id"]
            # Subtracts offset (e.g., if the labels are 1-indexed).
            cls -= offset
            # Sets class slot to 1 in the label.
            mil_labels[j][cls] = 1

    return mil_labels


def mil_nll(mil_scores, mil_labels, eps=1e-5):
    """Computes negative log-likelihood between MIL scores and MIL labels.

    eps argument prevents loss from becoming NaN.
    """

    # Computes class-wise log-likelihoods.
    class_likelihoods = mil_labels * torch.log(mil_scores + eps) + (
        1 - mil_labels
    ) * torch.log(1 - mil_scores + eps)

    # Computes mean NLL loss across batch.
    nll = -torch.sum(class_likelihoods, 1)
    mil_loss = torch.mean(nll, 0)

    return mil_loss


def objectness_mse_loss(dets_sigmoid, obj_confs):
    """Computes MSE regularization loss on detections and objectness.

    Aligns the maximum detection confidence of the weakly supervised
    model with the objectness confidence of the class-agnostic model.
    """

    # Computes maximum detection confidences and MSE loss.
    max_det_confs, _ = torch.max(dets_sigmoid, dim=2)
    objectness_loss = F.mse_loss(max_det_confs, torch.stack(obj_confs))

    return objectness_loss


def mil_loss(
    outputs,
    targets,
    joint_probability=None,
    objectness_scale=1,
    offset=0,
    sparse=None,
    weighted_sum=False,
):
    """Computes MIL score and label, then returns NLL loss with objectness."""
    losses = {}

    batch_size, _, classes = outputs["pred_logits"].shape
    mil_labels = mil_label(batch_size, classes, targets, offset=offset)

    dets_sigmoid, scores = mil_score(
        outputs,
        joint_probability=joint_probability,
        sparse=sparse,
    )
    if weighted_sum:
        weights = F.softmax(outputs["obj_confs"], dim=1)
        scores = F.softmax(scores * weights.unsqueeze(-1), dim=1)

    mil_scores = torch.sum(scores, 1)
    mil_loss = mil_nll(mil_scores, mil_labels)

    if objectness_scale > 0:
        if joint_probability:
            objectness_loss = 0.0 * torch.sum(outputs["det_logits"])
        else:
            objectness_loss = objectness_mse_loss(
                dets_sigmoid,
                outputs["obj_confs"],
            )
            objectness_loss *= objectness_scale

        losses["loss_mil"] = mil_loss + objectness_loss
        return losses

    losses["loss_mil"] = mil_loss
    return losses


def inverse_sigmoid(x, eps=1e-5):
    """Transforms a sigmoid vector back into logits."""

    x = x.clamp(min=0, max=1)
    x1 = x.clamp(min=eps)
    x2 = (1 - x).clamp(min=eps)
    return torch.log(x1 / x2)
