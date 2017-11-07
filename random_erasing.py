import math
import random
from PIL import Image
class RandomErasing(object):
    def __init__(self, s_min=0.02, s_max=0.4, r_min=1/3., r_max=3, ratio=0.5):
        self.s_min = s_min
        self.s_max = s_max
        self.r_min = r_min
        self.r_max = r_max
        self.ratio = ratio

    def __call__(self, img):
        if random.random() < self.ratio:
            x, y = img.size
            S = x * y
            while True:
                scale = (self.s_min + random.random() * (self.s_max - self.s_min)) * S
                a_ratio = self.r_min + random.random() * (self.r_max - self.r_min)
                H = math.sqrt(a_ratio * scale)
                W = math.sqrt(scale/a_ratio)
                xmin, ymin = random.randint(0, x), random.randint(0, y)
                if xmin + W <= x and ymin + H <= y:
                    break
            xmax, ymax = min(xmin+W, x), min(ymin+H, y)
            mask = Image.new("RGB", (int(round(xmax-xmin)), int(round(ymax-ymin))))
            mask = mask.point(lambda _: random.randint(0, 255))
            img.paste(mask, (xmin, ymin))

        return img
