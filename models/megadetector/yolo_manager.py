import torch
from ultralytics import YOLO
from torchvision import transforms


class YOLOManager:
    def __init__(self, model_path="megadetector/MDV6-yolov9e.pt"):
        self.model_path = model_path
        self.model = self._load_model()
        self.main_transform = transforms.Compose(
            [
                transforms.Resize((640, 640)),
                transforms.ToTensor(),
            ]
        )
        self.device = "cpu"

    def _load_model(self):
        model = YOLO(self.model_path, verbose=False)
        return model

    def mount(self):
        self.model.to("cuda")
        self.device = "cuda"

    def unmount(self):
        self.model.to("cpu")
        self.device = "cpu"

    def predict(self, x, **kwargs):
        with torch.inference_mode():
            results = self.model(
                self.main_transform(x).unsqueeze(0).to(self.device), **kwargs
            )
        return [result.summary() for result in results]
