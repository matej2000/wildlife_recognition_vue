import torch
from ultralytics import YOLO
from torchvision import transforms
import cv2
import base64


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

        annotated_image = results[0].plot()

        success, buffer = cv2.imencode(".jpg", annotated_image)

        if not success:
            raise RuntimeError("Could not encode annotated image")

        image_base64 = base64.b64encode(buffer).decode("utf-8")

        return {
            "predictions": results[0].summary(),
            "annotated_image": image_base64,
        }
