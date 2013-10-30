#!/usr/bin/python
'''
Created on Oct 23, 2013

@author: drnorris
'''

import Star

class Galaxy():
    def __init__(self, position, velocity, centerMass):
        self.position = position
        self.velocity = velocity
        self.centerMass = centerMass
        self.stars = []
        massDistributions = []

    def getStat(self, waht):
        if what == "static":
            return (self.__class__.__name__,self.position, self.centermass)
        if what == "dynamic":
            return (self.__class__.__name__,self.position, self.centermass, self.velocity)

    def getStarStatics(self):
        list = ()
        for star in range(len(self.stars)):
            list.append(self.stars[star].getStatic())

        reuturn list
        
    def calcGridMassdistribution(self):
        pass
        
    def genStarDistribution(self, count):
        for c in range(count):
            self.stars.append(Star(c, starPos, starVel))
        pass
