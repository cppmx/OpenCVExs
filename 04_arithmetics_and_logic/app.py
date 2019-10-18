import cv2
import numpy as np
import os

from pathlib import Path

IMAGE_1 = os.path.join(Path(Path(__file__).parent.absolute()).parent.absolute(), 'assets', 'test_image_02.png')
IMAGE_2 = os.path.join(Path(Path(__file__).parent.absolute()).parent.absolute(), 'assets', 'test_image_03.png')
LOGO = os.path.join(Path(Path(__file__).parent.absolute()).parent.absolute(), 'assets', 'python_logo.png')

# 500 x 250
img1 = cv2.imread(IMAGE_1)
img2 = cv2.imread(IMAGE_2)
img3 = cv2.imread(LOGO)


def try_to_add_two_images():
    add = img1 + img2

    cv2.imshow('First try to add', add)
    cv2.waitKey(0)
    cv2.destroyAllWindows()


def add_two_images_correct_wayi_1():
    '''Add two images using the OpenCV add method

    The result is an too much white image, this is because colors are 0-255, where 255 is "full light."
    Thus, for example: (155,211,79) + (50, 170, 200) = 205, 381, 279...translated to (205, 255,255).
    '''
    add = cv2.add(img1, img2)

    cv2.imshow('Using the OpenCV add method',add)
    cv2.waitKey(0)
    cv2.destroyAllWindows()


def add_two_images_correct_wayi_2():
    '''add two images, and have each carry a different weight

    For the addWeighted method, the parameters are:
      - the first image
      - the weight
      - the second image
      - that weight
      - and then finally gamma, which is a measurement of light
    '''
    weighted = cv2.addWeighted(img1, 0.6, img2, 0.4, 0)
    cv2.imshow('Add weighted method',weighted)
    cv2.waitKey(0)
    cv2.destroyAllWindows()


def add_python_logo():
    # I want to put logo on top-left corner, So I create a ROI
    rows, cols, channels = img3.shape
    roi = img1[0:rows, 0:cols ]

    # Now create a mask of logo and create its inverse mask
    img2gray = cv2.cvtColor(img3, cv2.COLOR_BGR2GRAY)

    # add a threshold
    ret, mask = cv2.threshold(img2gray, 220, 255, cv2.THRESH_BINARY_INV)

    mask_inv = cv2.bitwise_not(mask)

    # Now black-out the area of logo in ROI
    img1_bg = cv2.bitwise_and(roi, roi, mask = mask_inv)

    # Take only region of logo from logo image.
    img2_fg = cv2.bitwise_and(img3, img3, mask = mask)

    dst = cv2.add(img1_bg, img2_fg)
    img1[0:rows, 0:cols ] = dst

    cv2.imshow('Logo on an image', img1)
    cv2.waitKey(0)
    cv2.destroyAllWindows()


try_to_add_two_images()
add_two_images_correct_wayi_1()
add_two_images_correct_wayi_2()
add_python_logo()
