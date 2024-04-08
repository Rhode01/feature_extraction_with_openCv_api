from fastapi import FastAPI
from app import extract_features
from models import ImagePath

app = FastAPI()

@app.post("/feature_extraction")
async def feature_extraction(image_path: ImagePath):
    return await extract_features(image_path.path)
