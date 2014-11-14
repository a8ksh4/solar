'''
Created on Oct 23, 2013

@author: drnorris
'''

#import Galaxy
from Galaxy import *

class Space():
    def __init__(self, size):
        self.size = size
        self.galaxys = []
        self.massMaps = []

    def createGalaxies(self, count):
        for c in range(count):
            xpos = self.size / 2
            ypos = c * self.size / count
            self.galaxys.append(Galaxy((xpos, ypos), (0,0), 10))
            self.galaxys[c].createStars(4)

    def getObjectList(self):
        list = []
        for galaxy in range(len(self.galaxys)):
            list.append(self.galaxys[galaxy].getStat("static"))
            for star in self.galaxys[galaxy].getStarStats("static"):
                list.append(star)

        return(list)
