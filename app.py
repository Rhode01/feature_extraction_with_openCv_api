import cv2 as cv
from utils import download_image

def extract_features(image_path):
    image = download_image(image_path)
    gray_image = cv.cvtColor(image, cv.COLOR_BGR2GRAY)
    sift = cv.SIFT_create()
    keypoints, descriptors = sift.detectAndCompute(gray_image, None)
    image_with_keypoints = cv.drawKeypoints(gray_image, keypoints, None)
    return image_with_keypoints
