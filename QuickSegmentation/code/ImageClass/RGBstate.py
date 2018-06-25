import cv2
class RGBstate:
    def toBGR(self,img):
        return cv2.cvtColor(img, cv2.COLOR_RGB2BGR)

    def toRGB(self,img):
        return img

    def toGRAY(self,img):
        return cv2.cvtColor(img, cv2.COLOR_RGB2GRAY)

    def toHSV(self,img):
        return cv2.cvtColor(img,cv2.COLOR_RGB2HSV)


