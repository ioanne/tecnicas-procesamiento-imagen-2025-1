import numpy as np

from fastapi import UploadFile
from PIL import Image


def read_image(upload: UploadFile) -> np.ndarray:
    image = Image.open(upload.file).convert("RGB")
    return np.array(image)


def rgb_to_hex(rgb: tuple[int, int, int]) -> str:
    return "#{:02X}{:02X}{:02X}".format(*rgb)