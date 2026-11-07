import torch
from wdmilfast.wildlife_detector_mil import WildlifeDetectorMIL, load_yolo
from torchvision import transforms


class WDMilFastManager:
    def __init__(
        self,
        num_classes=10,
        model_path="wdmilfast/model_4.pth",
        yolo_model_path="MDV6-yolov9e.pt",
        yolo_base="ultralytics",
        classifier="convnext",
        yolo_th=0.6,
    ):
        self.device = "cpu"
        self.model = self.load(
            num_classes, model_path, yolo_model_path, yolo_base, classifier, yolo_th
        )
        self.num_classes = num_classes
        self.model_path = model_path
        self.yolo_model_path = yolo_model_path
        self.yolo_base = yolo_base
        self.classifier = classifier
        self.yolo_th = yolo_th
        self.main_transform = transforms.Compose(
            [
                transforms.Resize((640, 640)),
                transforms.ToTensor(),
            ]
        )

    def load(
        self, num_classes, model_path, yolo_model_path, yolo_base, classifier, yolo_th
    ):
        model = WildlifeDetectorMIL(
            num_classes,
            yolo_model_path,
            yolo_base,
            classifier,
            yolo_th,
        )
        model.load_state_dict(torch.load(model_path), strict=False)
        model.yolo = load_yolo(yolo_model_path, yolo_base)
        model.resnet.eval()
        return model

    def unmount(self):
        self.model.to("cpu")
        self.device = "cpu"

    def mount(self):
        self.model.to("cuda")
        self.device = "cuda"

    def predict(self, x):
        with torch.inference_mode():
            results = self.model(
                self.main_transform(x).unsqueeze(0).to(self.device),
                self.model.resnet_transform(x).unsqueeze(0).to(self.device),
            )
        return results
