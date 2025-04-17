from image_processor import ImageProcessor, ImageProcessorURL


if __name__ == '__main__':
    params = {
        "convert_and_save_bgr": True,
        "save_grayscale": False,
        "reduce_grayscale_levels": [],
        "detect_and_save_edges": False
    }

    processor = ImageProcessor('naranja_2.jpg', name="naranja")
    processor.processor(params)

    url = "https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcTLWh-E-5rCitwZiTaKzesMB6kupUh0TRu1FQ&s"
    processor2 = ImageProcessorURL(url , name="banana")
    processor2.processor(params)

    url = "https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcQVO_QiPMeeNOKNtcedvMgKv7oV0GQVV0v0Cw&s"
    processor2 = ImageProcessorURL(url , name="kiwi")
    processor2.processor(params)
