import cv2
class HSVstate(object):
    def toBGR(self,img):
        return cv2.cvtColor(img, cv2.COLOR_HSV2BGR)

    def toRGB(self,img):
        return cv2.cvtColor(img, cv2.COLOR_HSV2RGB)

    def toGRAY(self,img):
        return cv2.cvtColor(cv2.cvtColor(img, cv2.COLOR_HSV2RGB), cv2.COLOR_RGB2GRAY)

    def toHSV(self,img):
        return img


