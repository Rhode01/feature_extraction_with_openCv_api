from fastapi import FastAPI
from app import extract_features, compare_picture_features,make_picture_blackAndwhite, make_picture_blur, human_face_detection
from models import ImagePath,PicturesPath

app = FastAPI()

@app.post("/feature_extraction")
def feature_extraction(image_path: ImagePath):
    return extract_features(image_path.path)

@app.post("/feature_comparison")
def picture_comparison(image_paths:PicturesPath):
    return compare_picture_features(image_paths.picture_urls)

@app.post("/black_and_white")
def make_picture_bw(image_path:ImagePath):
    return make_picture_blackAndwhite(image_path.path)

@app.post("/blur_picture")
def blur_picture(image_path: ImagePath):
    return make_picture_blur(image_path.path)

@app.post("/face_detection")
def face_detection(image_path:ImagePath):
    return human_face_detection(image_path.path)