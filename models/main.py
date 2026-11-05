from contextlib import asynccontextmanager
from fastapi import FastAPI, UploadFile, File, HTTPException
from PIL import Image, UnidentifiedImageError
from io import BytesIO
from model1.yolo_manager import YOLOManager


@asynccontextmanager
async def lifespan(app: FastAPI):
    app.state.yolo = YOLOManager()
    await app.state.yolo.load()
    yield


app = FastAPI(lifespan=lifespan)


@app.post("/predict")
async def predict(file: UploadFile = File(...)):
    try:
        image = Image.open(BytesIO(await file.read()))
        image.load()
        image = image.convert("RGB")
    except (UnidentifiedImageError, OSError):
        raise HTTPException(status_code=400, detail="Invalid image")

    return await app.state.yolo.predict(image, conf=0.5, imgsz=640)


@app.post("/detect")
async def detect(file: UploadFile = File(...)):
    try:
        image = Image.open(BytesIO(await file.read()))
        image.load()
        image = image.convert("RGB")
    except (UnidentifiedImageError, OSError):
        raise HTTPException(status_code=400, detail="Invalid image")

    return await app.state.yolo.predict(image, conf=0.3, imgsz=1280)
