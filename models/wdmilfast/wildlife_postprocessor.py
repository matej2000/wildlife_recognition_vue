from torch import nn
from wdmilfast.mil_loss import mil_score
import torch
import torchvision


class WildlifeMilPostProcessor(nn.Module):
    def __init__(
        self,
        num_classes,
        yolo_shape,
        classifier_shape,
        threshold,
        in_fmt,
        out_fmt="xywh",
    ):
        super(WildlifeMilPostProcessor, self).__init__()
        self.num_classes = num_classes
        self.yolo_shape = yolo_shape
        self.classifier_shape = classifier_shape
        self.threshold = threshold
        self.in_fmt = in_fmt
        self.out_fmt = out_fmt

    def forward(
        self,
        outputs,
        og_shape0=4608,
        og_shape1=2592,
        sparse=False,
        joint_probability=False,
    ):
        _, conf_scores = mil_score(
            outputs, joint_probability=joint_probability, sparse=sparse
        )
        scores, topk_indexes = torch.topk(
            conf_scores.view(conf_scores.shape[0], -1), 50, dim=1
        )
        topk_boxes = topk_indexes // conf_scores.shape[2]
        labels = topk_indexes % conf_scores.shape[2]

        boxes = torch.gather(
            torch.stack(outputs["boxes"]).to(torch.device("cuda")),
            1,
            topk_boxes.unsqueeze(-1).repeat(1, 1, 4),
        )
        bbox_pred = torchvision.ops.box_convert(
            boxes, in_fmt=self.in_fmt, out_fmt=self.out_fmt
        )

        scale_x = og_shape0 / self.yolo_shape[0]
        scale_y = og_shape1 / self.yolo_shape[1]
        bbox_pred *= (
            torch.tensor([scale_x, scale_y]).to(torch.device("cuda")).repeat(1, 2)
        )

        results = []
        for i in range(scores.shape[0]):
            mask = scores[i] > self.threshold
            results.append(
                {
                    "boxes": bbox_pred[i][mask],
                    "scores": scores[i][mask],
                    "labels": labels[i][mask],
                }
            )
        return results
