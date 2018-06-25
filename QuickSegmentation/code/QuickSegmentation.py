import cv2
import numpy
from pathlib2 import Path
from ImageClass.Image import *
from ImageClass.RGBstate import *
def showMe(img, n):
    cv2.imshow('', img)
    cv2.waitKey(n)


basePath = './images'
trainPath = basePath+'/train'
path = trainPath+'/100075.jpg'
img = cv2.imread(path)

nImg = Image()
nImg.getFromClient(img)
nImg.toRGB()
nImg.show()
