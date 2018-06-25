import cv2
import ImageClass
class GetImage_Basic():
    def get(self, file = '/100075.jpg'):
        basePath = './images'
        trainPath = basePath+'/train'
        path = trainPath+ file
        img = cv2.imread(path)
        nImg = ImageClass.Image()
        nImg.getFromClient(img)
        return nImg

