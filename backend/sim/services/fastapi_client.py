# services/fastapi_client.py

import httpx

FASTAPI_URL = "http://ml-service:8001"


def call_fastapi(model, image):
    url = f"{FASTAPI_URL}/predict/{model}"
    files = {"file": (image.name, image, image.content_type)}

    try:
        response = httpx.post(url, files=files, timeout=120.0)
        response.raise_for_status()
        return response.json()

    except httpx.HTTPError as e:
        return {"error": str(e)}
