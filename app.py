import cv2 as cv
import numpy as np
from utils import download_image,image_generator
from io import BytesIO
from PIL import Image
from fastapi.responses import StreamingResponse
from fastapi import HTTPException
def extract_features(image_path):
    image = download_image(image_path)
    image = np.asanyarray(image)

    gray_image = cv.cvtColor(image, cv.COLOR_BGR2GRAY)
    sift = cv.SIFT_create()

    keypoints, descriptors = sift.detectAndCompute(gray_image, None)

    image_with_keypoints = cv.drawKeypoints(gray_image, keypoints, None)
    
    image_with_keypoints_pil = Image.fromarray(image_with_keypoints)
    return StreamingResponse(image_generator(image_with_keypoints_pil), media_type="image/png")
def picture_features_comparison(img1, img2):
    img1 = np.asanyarray(img1)
    img2 = np.asanyarray(img2)
    gray1 = cv.cvtColor(img1,cv.COLOR_BGR2GRAY)
    gray2= cv.cvtColor(img2,cv.COLOR_BGR2GRAY)
    
    sift = cv.SIFT_create()
    bf = cv.BFMatcher()

    keypoints1, descriptors1 = sift.detectAndCompute(gray1,None)
    keypoints2, descriptors2 = sift.detectAndCompute(gray2,None)
    matches = bf.knnMatch(descriptors1, descriptors2, k=2)
    good_matches = []
    for m, n in matches:
        if m.distance < 0.75 * n.distance:
            good_matches.append([m])
    matched_img = cv.drawMatchesKnn(gray1,keypoints1,gray2,keypoints2,good_matches,None, flags=cv.DrawMatchesFlags_NOT_DRAW_SINGLE_POINTS)

    return matched_img
def compare_picture_features(image_paths):
    if len(image_paths) < 2:
         return{
             "info":"you need to provide two urls to compare picture features"
         }
    img1_url, img2_url = image_paths[:2]
    image1 = download_image(img1_url)
    image2 = download_image(img2_url)
    comparison = picture_features_comparison(image1, image2)
    comparison_pil = Image.fromarray(comparison)
    return StreamingResponse(image_generator(comparison_pil), media_type="image/png")

def make_picture_blackAndwhite(image_path):
    image = download_image(image_path)
    image = np.asanyarray(image)
    im_gray = cv.cvtColor(image, cv.COLOR_BGR2GRAY)
    (thresh, im_bw) = cv.threshold(im_gray, 128, 255, cv.THRESH_BINARY | cv.THRESH_OTSU)
    thresh = 127
    im_bw = cv.threshold(im_gray, thresh, 255, cv.THRESH_BINARY)[1]
    black_and_white = Image.fromarray(im_bw)
    return StreamingResponse(image_generator(black_and_white),media_type="image/png")

def make_picture_blur(image_path):
    image = download_image(image_path)
    image= np.asanyarray(image)
    kernel = np.ones((5,5), np.float32)/25
    dist = cv.filter2D(image, -1, kernel)
    blurred_pic = Image.fromarray(dist)
    return StreamingResponse(image_generator(blurred_pic), media_type="image/png")


def human_face_detection(image_url):
    try:
        image = download_image(image_url)
        image_np = np.asarray(image)
        image_np = cv.cvtColor(image_np, cv.COLOR_RGB2BGR)
        face_cascade = cv.CascadeClassifier(cv.data.haarcascades + 'haarcascade_frontalface_default.xml')
        gray_image = cv.cvtColor(image_np, cv.COLOR_BGR2GRAY)
        faces = face_cascade.detectMultiScale(gray_image, scaleFactor=1.1, minNeighbors=5)
        for (x, y, w, h) in faces:
            cv.rectangle(image_np, (x, y), (x+w, y+h), (255, 0, 0), 2)
        face_detected_image = Image.fromarray(cv.cvtColor(image_np, cv.COLOR_BGR2RGB))
        return StreamingResponse(image_generator(face_detected_image), media_type="image/png")
    except Exception as e:
        raise HTTPException(status_code=400, detail=f"Failed to detect faces: {str(e)}")


    