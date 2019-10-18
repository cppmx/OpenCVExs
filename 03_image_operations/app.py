import numpy as np
import cv2
import os

from pathlib import Path

IMAGE = os.path.join(Path(Path(__file__).parent.absolute()).parent.absolute(), 'assets', 'dextra_01.jpg')

img = cv2.imread(IMAGE, cv2.IMREAD_COLOR)

# reference specific pixels
px = img[55, 55]

# change a pixel
img[55, 55] = [255, 255, 255]

print(px)

# reference an ROI, or Region of Image
px = img[100:150, 100:150]
print(px)

# modify the ROI
img[100:150, 100:150] = [255, 255, 255]

# reference certain characteristics of our image
print(img.shape)
print(img.size)
print(img.dtype)

# Perform other operations
logo = img[37:111, 107:194]
img[0:74, 0:87] = logo

cv2.imshow(IMAGE, img)
cv2.waitKey(0)
cv2.destroyAllWindows()
