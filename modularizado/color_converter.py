import cv2


class ColorConverter:
    @staticmethod
    def rgb_to_bgr(image):
        return cv2.cvtColor(image, cv2.COLOR_RGB2BGR)
