import cv2


class EdgeDetector:
    @staticmethod
    def detect_edges(image, low_threshold=50, high_threshold=250):
        return cv2.Canny(image, low_threshold, high_threshold)