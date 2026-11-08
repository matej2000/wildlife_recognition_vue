from torch import nn
import torch
from torchvision.ops import roi_align
from ultralytics import YOLO, RTDETR
from torchvision import transforms
from torchvision.models import convnext_small, ConvNeXt_Small_Weights


def load_yolo(weights, yolo_base):
    if yolo_base == "ultralytics":
        model = YOLO(weights, verbose=False)
    elif yolo_base == "pytorch":
        model = torch.hub.load(
            "ultralytics/yolov5", "custom", path=weights, force_reload=True
        )
    elif yolo_base == "ultralytics-rtdetr":
        model = RTDETR(weights)
    else:
        raise ValueError(f"Unknown yolo_base: {yolo_base}")
    for param in model.model.parameters():
        param.requires_grad = False
    return model


class WildlifeDetectorMIL(nn.Module):
    def __init__(
        self,
        num_classes,
        yolo_weights="MDV6b-yolov9e.pt",
        yolo_base="ultralytics",
        classifier="convnext",
        yolo_th=0.6,
    ):
        super(WildlifeDetectorMIL, self).__init__()
        print(classifier, num_classes, yolo_weights, yolo_base)
        self.num_classes = num_classes
        self.yolo = load_yolo(yolo_weights, yolo_base)
        self.yolo_th = yolo_th
        self.yolo_transform = transforms.Compose(
            [
                transforms.Resize((640, 640)),
            ]
        )

        if classifier == "resnet50":
            self.resnet = torch.hub.load(
                "pytorch/vision:v0.10.0", "resnet50", pretrained=True
            )
            self.input_w = 224
            self.input_h = 224
            self.hidden_dim = 1024
            self.hidden_dim2 = 512
            self.resnet_transform = transforms.Compose(
                [
                    transforms.Resize((self.input_w, self.input_h)),
                    transforms.Normalize(
                        mean=[0.485, 0.456, 0.406], std=[0.229, 0.224, 0.225]
                    ),
                ]
            )

            self.resnet = nn.Sequential(
                self.resnet.conv1,
                self.resnet.bn1,
                self.resnet.relu,
                self.resnet.maxpool,
                self.resnet.layer1,
                self.resnet.layer2,
                self.resnet.layer3,
            )
        elif classifier == "convnext":
            self.resnet = convnext_small(ConvNeXt_Small_Weights.DEFAULT)
            self.resnet = nn.Sequential(*list(self.resnet.features.children())[:6])
            self.input_w = 224
            self.input_h = 224
            self.hidden_dim = 384
            self.hidden_dim2 = 768
            self.resnet_transform = ConvNeXt_Small_Weights.DEFAULT.transforms()
        else:
            raise Exception("Classifier not supported!")

        self.avg_pool = nn.AdaptiveAvgPool2d((1, 1))
        self.fc1_det = nn.Sequential(
            nn.Linear(self.hidden_dim, self.hidden_dim2),
            nn.ReLU(),
            nn.Dropout(0.5),
            nn.Linear(self.hidden_dim2, num_classes),
        )
        self.fc1_clas = nn.Sequential(
            nn.Linear(self.hidden_dim, self.hidden_dim2),
            nn.ReLU(),
            nn.Dropout(0.5),
            nn.Linear(self.hidden_dim2, num_classes),
        )

    def forward(self, x1, x2):
        objects = self.yolo(x1, verbose=False, conf=0)
        features = self.resnet(x2)
        roi_pooled = roi_align(
            features,
            [x.boxes.xyxy for x in objects],
            output_size=(7, 7),
            spatial_scale=features.shape[-1] / 640,
        )
        roi_pooled = self.avg_pool(roi_pooled).squeeze(2, 3)
        batches = x1.shape[0]
        pred_logits = self.fc1_clas(roi_pooled).view(batches, 300, 10)
        det_logits = self.fc1_det(roi_pooled).view(batches, 300, 10)

        boxes = [x.boxes.xyxy for x in objects]
        scores = [x.boxes.conf for x in objects]
        outputs = {
            "boxes": boxes,
            "obj_confs": scores,
            "pred_logits": pred_logits,
            "det_logits": det_logits,
        }
        return outputs
