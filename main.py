from fastapi import FastAPI
from app import extract_features, compare_picture_features
from models import ImagePath,PicturesPath

app = FastAPI()

@app.post("/feature_extraction")
def feature_extraction(image_path: ImagePath):
    return extract_features(image_path.path)

@app.post("/feature_comparison")
def picture_comparison(image_paths:PicturesPath):
    return compare_picture_features(image_paths.picture_urls)