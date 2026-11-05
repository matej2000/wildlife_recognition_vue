import torch
from ultralytics import YOLO
import asyncio
from starlette.concurrency import run_in_threadpool
from torchvision import transforms


class YOLOManager:
    def __init__(self, model_path="model1/MDV6-yolov9e.pt"):
        self.model_path = model_path
        self.model = None
        self.lock = asyncio.Lock()
        self.main_transform = transforms.Compose(
            [
                transforms.Resize((640, 640)),
                transforms.ToTensor(),
            ]
        )

    async def load(self):
        self.model = await run_in_threadpool(self._load_model)

    def _load_model(self):
        model = YOLO(self.model_path, verbose=False)
        model.to("cuda")
        return model

    async def predict(self, image, **kwargs):
        async with self.lock:
            return await run_in_threadpool(self._predict, image, kwargs)

    def _predict(self, x, kwargs):
        with torch.inference_mode():
            results = self.model(self.main_transform(x).unsqueeze(0), **kwargs)
        return [result.summary() for result in results]
