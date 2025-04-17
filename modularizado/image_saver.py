import os

import matplotlib.pyplot as plt


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