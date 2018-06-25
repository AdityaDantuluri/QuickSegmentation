import cv2
class GRAYstate:

    def toBGR(self,img):
        return cv2.cvtColor(img, cv2.COLOR_GRAY2BGR)

    def toRGB(self,img):
        return cv2.cvtColor(img, cv2.COLOR_GRAY2RGB)

    def toGRAY(self,img):
        return img

    def toHSV(self,img):
        return cv2.cvtColor(cv2.cvtColor(img, cv2.COLOR_GRAY2BGR),cv2.COLOR_BGR2HSV)

        


