import cv2
import numpy
import ImageClass
import Strategies
class Hub(object):
    getImageStrat = None;
    simplificationStrat = None;
    img = None

    def __init__(self):
        self.getImageStrat = Strategies.GetImage_Basic()
    
    def setGet(self, strat):
        self.getImageStrat = strat

    def setSimp(self, strat):
        self.simplificationStrat = strat




        
    def run(self):
        self.img = self.getImageStrat.get()
        self.img.show()