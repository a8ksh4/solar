'''
Created on Oct 23, 2013

@author: drnorris
'''

import Galaxy

class Space():
    def __init__(self, size):
        self.size = size
        self.galaxys = []
        self.massMaps = []

    def createGalaxies(self, count):
        for c in range(count):
            self.galaxys.append(Galaxy((self.size / 2, c * self.size / count), (0,0), 10))

    def getObjectList(self):
        list = ()
        for galaxy in range(len(self.galaxys)):
            list.append(self.galaxys[galaxy].getStatic())
            for starStatic in self.galaxys[galaxy].getStarStatics()
                list.append(starStatic)

        return list
