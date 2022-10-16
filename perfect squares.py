import numpy as np
import matplotlib.pyplot as plt
from PIL import Image, ImageDraw, ImageFont

width = 1920
height = 720
M = np.zeros([width,height])
im = Image.new('RGB', (width, height), (0, 0, 0)) #Setting up images' canvas size and background colour
draw = ImageDraw.Draw(im)

def is_integer_num(n):
    if isinstance(n, int):
        return True
    if isinstance(n, float):
        return n.is_integer()
    return False

for i in range(width):
    for j in range(height):
        k = np.sqrt((i)**2 + (j)**2)
        if is_integer_num(k) == True:
            value = 255
        else:
            value = 0
        draw.point([i, j], (value, value, value))

image_flip = im.transpose(Image.FLIP_TOP_BOTTOM)
image_flip.show()