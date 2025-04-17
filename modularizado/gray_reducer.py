
class GrayReducer:
    @staticmethod
    def reduce_levels(image, levels):
        factor = 256 // levels
        return (image // factor) * factor