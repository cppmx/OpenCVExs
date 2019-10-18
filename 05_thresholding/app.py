import cv2
import numpy as np
import os

from pathlib import Path

IMAGE = os.path.join(Path(Path(__file__).parent.absolute()).parent.absolute(), 'assets', 'test_image_04.jpg')
img = cv2.imread(IMAGE)
grayscaled = cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)


def try1():
    retval, threshold = cv2.threshold(img, 12, 255, cv2.THRESH_BINARY)

    cv2.imshow('original', img)
    cv2.imshow('Threshold Try 1 - Binary', threshold)
    cv2.waitKey(0)
    cv2.destroyAllWindows()


def try2():
    retval, threshold = cv2.threshold(grayscaled, 10, 255, cv2.THRESH_BINARY)

    cv2.imshow('original', img)
    cv2.imshow('Threshold Try 2 - Grayscaled', threshold)
    cv2.waitKey(0)
    cv2.destroyAllWindows()


def try3():
    th = cv2.adaptiveThreshold(grayscaled, 255, cv2.ADAPTIVE_THRESH_GAUSSIAN_C, cv2.THRESH_BINARY, 115, 1)

    cv2.imshow('original', img)
    cv2.imshow('Adaptive threshold', th)
    cv2.waitKey(0)
    cv2.destroyAllWindows()


def try4():
    retval2,threshold2 = cv2.threshold(grayscaled, 125, 255, cv2.THRESH_BINARY + cv2.THRESH_OTSU)

    cv2.imshow('original', img)
    cv2.imshow('Otsu threshold', threshold2)
    cv2.waitKey(0)
    cv2.destroyAllWindows()


try1()
try2()
try3()
try4()
