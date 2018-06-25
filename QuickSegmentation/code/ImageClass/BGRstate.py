import cv2
class BGRstate(object):
    def toBGR(self,img):
        return img

    def toRGB(self,img):
        return cv2.cvtColor(img, cv2.COLOR_BGR2RGB)

    def toGRAY(self,img):
        return cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

    def toHSV(self,img):
        return cv2.cvtColor(img,cv2.COLOR_BGR2HSV)


