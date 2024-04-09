import cv2 as cv
import numpy as np
from utils import download_image
from io import BytesIO
from PIL import Image
from fastapi.responses import StreamingResponse

def extract_features(image_path):
    image = download_image(image_path)
    image = np.asanyarray(image)

    gray_image = cv.cvtColor(image, cv.COLOR_BGR2GRAY)
    sift = cv.SIFT_create()

    keypoints, descriptors = sift.detectAndCompute(gray_image, None)

    image_with_keypoints = cv.drawKeypoints(gray_image, keypoints, None)
    
    image_with_keypoints_pil = Image.fromarray(image_with_keypoints)
    def image_generator():
            img_byte_arr = BytesIO()
            image_with_keypoints_pil.save(img_byte_arr, format="PNG")
            yield img_byte_arr.getvalue()
    return StreamingResponse(image_generator(), media_type="image/png")
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

    def image_generator():
            img_byte_arr = BytesIO()
            comparison_pil.save(img_byte_arr, format="PNG")
            yield img_byte_arr.getvalue()

    return StreamingResponse(image_generator(), media_type="image/png")

    
