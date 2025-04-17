import cv2
import urllib.request
import numpy as np


class ImageLoader:
    def __init__(self, image_path):
        self.image_path = image_path

    def load_color(self):
        return cv2.imread(self.image_path)

    def load_grayscale(self):
        return cv2.imread(self.image_path, cv2.IMREAD_GRAYSCALE)


class URLImageLoader:
    def __init__(self, image_url):
        self.image_url = image_url
        self.image_bytes = self._fetch_image_bytes()

    def _fetch_image_bytes(self):
        response = urllib.request.urlopen(self.image_url)
        image_bytes = bytearray(response.read())
        return np.asarray(image_bytes, dtype=np.uint8)

    def load_color(self):
        return cv2.imdecode(self.image_bytes, cv2.IMREAD_COLOR)

    def load_grayscale(self):
        return cv2.imdecode(self.image_bytes, cv2.IMREAD_GRAYSCALE)
