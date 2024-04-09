from pydantic import BaseModel

class ImagePath(BaseModel):
    path: str

class PicturesPath(BaseModel):
    picture_urls:list[str]