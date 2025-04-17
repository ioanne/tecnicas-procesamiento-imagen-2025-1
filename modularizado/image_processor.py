from color_converter import ColorConverter
from gray_reducer import GrayReducer
from edge_detector import EdgeDetector
from image_loader import ImageLoader, URLImageLoader
from image_saver import ImageSaver


class ImageProcessor:
    def __init__(self, filename, name):
        # imagen en local
        self.loader = ImageLoader(filename)
        self.saver = ImageSaver()
        self.name = name
        self._load_images()

    def _load_images(self):
        self.color_image = self.loader.load_color()
        self.gray_image = self.loader.load_grayscale()

    def convert_and_save_bgr(self):
        bgr_image = ColorConverter.rgb_to_bgr(self.color_image)
        self.saver.save(bgr_image, f'{self.name}_bgr.jpg', title="Imagen Original")

    def save_grayscale(self):
        self.saver.save(self.gray_image, f'{self.name}_escala_gris.jpg', cmap='gray', title="Escala de Grises")

    def reduce_grayscale_levels(self, levels_list=None):
        levels_list = levels_list or [2, 4, 8, 16, 32, 64, 128, 256]
        for levels in levels_list:
            reduced_image = GrayReducer.reduce_levels(self.gray_image, levels)
            self.saver.save(reduced_image, f'{self.name}_escala_gris-{levels}.jpg', cmap='gray', title=f"{levels} niveles de grises")

    def detect_and_save_edges(self):
        edges = EdgeDetector.detect_edges(self.gray_image)
        self.saver.save(edges, f'{self.name}_imagen_bordes.jpg', cmap='gray', title="Bordes Canny")

    def processor(self, params: dict):
        if params.get("convert_and_save_bgr"):
            self.convert_and_save_bgr()
        if params.get("save_grayscale"):
            self.save_grayscale()

        reduce_params = params.get("reduce_grayscale_levels")
        if isinstance(reduce_params, list):
            self.reduce_grayscale_levels(reduce_params)
        elif reduce_params:
            self.reduce_grayscale_levels()

        if params.get("detect_and_save_edges"):
            self.detect_and_save_edges()


class ImageProcessorURL(ImageProcessor):
    def __init__(self, filename, name):
        self.name = name
        self.loader = URLImageLoader(filename)
        self.saver = ImageSaver()
        self._load_images()
