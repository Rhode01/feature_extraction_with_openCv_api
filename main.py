import numpy as np
from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
import urllib.request
from PIL import Image
from io import BytesIO
import cv2 as cv
app = FastAPI()

class ImagePath(BaseModel):
    path: str

def download_image(url_or_path):
    try:
        if url_or_path.startswith("http"):  
            response = urllib.request.urlopen(url_or_path)
            image_data = response.read()
        else:  
            with open(url_or_path, "rb") as f:
                image_data = f.read()
        return image_data
    except Exception as e:
        raise HTTPException(status_code=400, detail=f"Failed to download image: {str(e)}")

def feature_extraction(image):
    gray_image = cv.cvtColor(image, cv.COLOR_BGR2GRAY)
    sift = cv.SIFT_create()
    keypoints, descriptors = sift.detectAndCompute(gray_image, None)
    image_with_keypoints = cv.drawKeypoints(gray_image, keypoints, None)
    return image_with_keypoints

@app.post("/feature_extraction")
async def extract_features(image_path: ImagePath):
    try:
        image_data = download_image(image_path.path)
        image_array = np.asarray(bytearray(image_data), dtype=np.uint8)
        image = cv.imdecode(image_array, cv.IMREAD_COLOR)
        features_image = feature_extraction(image)
        _, img_encoded = cv.imencode('.png', features_image)
        img_bytes = img_encoded.tobytes()
        return {"image_features": img_bytes}
    except Exception as e:
        return e