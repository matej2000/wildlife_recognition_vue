from contextlib import asynccontextmanager
from fastapi import FastAPI, UploadFile, File, HTTPException
from PIL import Image, UnidentifiedImageError
from io import BytesIO
from gpu_manager import GPUManager
from gpu_worker import GPUWorker


@asynccontextmanager
async def lifespan(app: FastAPI):
    app.state.gpu_manager = GPUManager()
    app.state.gpu_worker = GPUWorker(app.state.gpu_manager)
    await app.state.gpu_worker.start()
    yield
    await app.state.gpu_worker.stop()


app = FastAPI(lifespan=lifespan)


@app.post("/predict/{model_name}")
async def predict(model_name: str, file: UploadFile = File(...)):
    try:
        image = Image.open(BytesIO(await file.read()))
        image.load()
        image = image.convert("RGB")
    except (UnidentifiedImageError, OSError):
        raise HTTPException(status_code=400, detail="Invalid image")

    return await app.state.gpu_worker.submit(model_name, image)


@app.post("/detect")
async def detect(file: UploadFile = File(...)):
    try:
        image = Image.open(BytesIO(await file.read()))
        image.load()
        image = image.convert("RGB")
    except (UnidentifiedImageError, OSError):
        raise HTTPException(status_code=400, detail="Invalid image")

    return await app.state.model2.predict(image, conf=0.3, imgsz=1280)
