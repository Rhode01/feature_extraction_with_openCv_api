import requests
from PIL import Image
from io import BytesIO

def download_image(url_or_path):
    try:
        if url_or_path.startswith("http"):
            response = requests.get(url_or_path)
            image = Image.open(BytesIO(response.content))
        else:
            with open(url_or_path, "rb") as f:
                image = Image.open(f)
        return image
    except Exception as e:
        raise ValueError(f"Failed to download image: {str(e)}")
