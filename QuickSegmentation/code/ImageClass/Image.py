import cv2
import numpy
from RGBstate import *
from BGRstate import *
from HSVstate import *
from GRAYstate import *

class Image:
    OriginalImage = numpy.zeros((1,1,3), numpy.uint8)
    CurrentImage = numpy.zeros((1,1,3), numpy.uint8)

    isRGB = RGBstate()
    isBGR = GRAYstate()
    isGRAY = HSVstate()
    isHSV = BGRstate()
    imageState = BGRstate()

    def __init__(self):
        self.isRGB = RGBstate()
        self.isGRAY = GRAYstate()
        self.isHSV = HSVstate()
        self.isBGR = BGRstate()
    
    def setImageState(self,imState):
        self.imageState = imState

    #Not that imshow uses BGR standard, as such RGB image will display as if they were BRG images. 
    def toRGB(self):
        self.CurrentImage = self.imageState.toRGB(self.CurrentImage)
        self.imageState = self.isRGB

    def toGRAY(self):
        img =self.get()
        self.CurrentImage = self.imageState.toGRAY(img)
        self.imageState = self.isGRAY

    def toHSV(self):
        self.CurrentImage = self.imageState.toHSV(self.CurrentImage)
        self.imageState = self.isHSV

    def toBGR(self):
        self.CurrentImage = self.imageState.toBGR(self.CurrentImage)
        self.imageState = self.isBGR

    def get(self):
        return self.CurrentImage

    def getOriginal(self):
        return self.OriginalImage
    
    def show(self,n = 0):
        cv2.imshow('', self.CurrentImage)
        cv2.waitKey(n)

    def getFromFile(self,path, imS = BGRstate()):
        ##CURRENTLY NOT WORKING
        self.OriginalImage = cv2.imread(path)
        self.CurrentImage = self.OriginalImage
        self.imageState = imS

    def getFromClient(self,img, imS = BGRstate()):
        self.OriginalImage = img
        self.CurrentImage = self.OriginalImage
        self.imageState = imS