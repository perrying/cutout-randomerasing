import random
from PIL import Image, ImageChops
class Cutout(object):
    def __init__(self, size=16, ratio=0.5):
        self.size = size
        self.p = ratio

    def __call__(self, img):
        if random.random() < self.p:
            x, y = img.size
            cx = random.randint(0, x)
            cy = random.randint(0, y)
            xmin, ymin = max(cx-self.size/2, 0), max(cy-self.size/2, 0)
            xmax, ymax = min(cx+self.size/2, x), min(cy+self.size/2, y)
            mask = Image.new("RGB", (xmax-xmin, ymax-ymin))
            mask = mask.point(lambda _: random.randint(0, 255))
            img.paste(mask, (xmin, ymin))
        return img
