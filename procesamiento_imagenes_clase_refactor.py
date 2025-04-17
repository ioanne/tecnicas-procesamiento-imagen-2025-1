import cv2
import matplotlib.pyplot as plt
import os


class ImageLoader:
    def __init__(self, image_path):
        self.image_path = image_path

    def load_color(self):
        return cv2.imread(self.image_path)

    def load_grayscale(self):
        return cv2.imread(self.image_path, cv2.IMREAD_GRAYSCALE)


class ImageSaver:
    def __init__(self, output_dir='images'):
        self.output_dir = output_dir
        os.makedirs(output_dir, exist_ok=True)

    def save(self, image, filename, cmap=None, title=None):
        path = os.path.join(self.output_dir, filename)
        plt.imshow(image, cmap=cmap)
        plt.axis('off')
        if title:
            plt.title(title)
        plt.savefig(path)
        plt.close()


class ColorConverter:
    @staticmethod
    def rgb_to_bgr(image):
        return cv2.cvtColor(image, cv2.COLOR_RGB2BGR)


class GrayReducer:
    @staticmethod
    def reduce_levels(image, levels):
        factor = 256 // levels
        return (image // factor) * factor


class EdgeDetector:
    @staticmethod
    def detect_edges(image, low_threshold=50, high_threshold=250):
        return cv2.Canny(image, low_threshold, high_threshold)


class ImageProcessor:
    def __init__(self, loader, saver):
        self.loader = loader
        self.saver = saver

    def process(self):
        # Cargar imágenes
        color_image = self.loader.load_color()
        gray_image = self.loader.load_grayscale()

        # Convertir y guardar imagen BGR
        bgr_image = ColorConverter.rgb_to_bgr(color_image)
        self.saver.save(bgr_image, 'naranja_2_bgr.jpg', title="Imagen Original")

        # Guardar imagen en escala de grises
        self.saver.save(gray_image, 'naranja_escala_gris.jpg', cmap='gray', title="Escala de Grises")

        # Reducir niveles de grises y guardar
        for levels in [2, 4, 8, 16, 32, 64, 128, 256]:
            reduced_image = GrayReducer.reduce_levels(gray_image, levels)
            self.saver.save(reduced_image, f'naranja_escala_gris-{levels}.jpg', cmap='gray', title=f"{levels} niveles de grises")

        # Detección de bordes
        edges = EdgeDetector.detect_edges(gray_image)
        self.saver.save(edges, 'imagen_bordes.jpg', cmap='gray', title="Bordes Canny")


if __name__ == '__main__':
    print("Ejecutando esto")
    loader = ImageLoader('naranja_2.jpg')
    saver = ImageSaver()
    processor = ImageProcessor(loader, saver)
    processor.process()
