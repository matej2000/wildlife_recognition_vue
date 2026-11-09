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
                self.main_transform(x).unsqueeze(0).to(self.device), conf=0, **kwargs
            )

        # annotated_image = results[0].plot()

        # success, buffer = cv2.imencode(".jpg", annotated_image)

        # if not success:
        #     raise RuntimeError("Could not encode annotated image")

        # image_base64 = base64.b64encode(buffer).decode("utf-8")
        class_mappings = {
            2: "Red deer",
            1: "Wild boar",
            5: "Mustelid",
            6: "Fox",
            7: "Badger",
            4: "Bird",
            8: "Bear",
            3: "Roe deer",
            9: "Chamois",
            0: "Squirrel",
        }
        result = results[0]
        detections = []

        for b in result.boxes[:50]:
            box = b.xyxy[0].detach().cpu().tolist()
            score = b.conf[0].detach().cpu().item()
            label = int(b.cls[0].detach().cpu().item())

            detections.append(
                {
                    "label": result.names[label],
                    "score": score,
                    "box": box,
                }
            )

        return {
            "image_width": 640,
            "image_height": 640,
            "detections": detections,
            # "annotated_image": image_base64,
        }
