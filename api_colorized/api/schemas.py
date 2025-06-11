from pydantic import BaseModel
from typing import List


class ColorReplacement(BaseModel):
    original_color: List[int]  # [R, G, B]
    new_color: List[int]       # [R, G, B]


class ReplacementRequest(BaseModel):
    replacements: List[ColorReplacement]
    tolerance: int = 0
    filename: str = "modified_image.png"
