#!/usr/bin/python
'''
Created on Oct 23, 2013

@author: drnorris
'''

from Star import *
import random
import math

class Galaxy():
    def __init__(self, position, velocity, centerMass):
        self.position = position
        self.velocity = velocity
        self.centerMass = centerMass
        self.stars = []
        massDistributions = []
        random.seed(a=0)

    def seq(start, stop, step=1):
        n = int(round((stop - start)/float(step)))
        if n > 1:
            return([start + step*i for i in range(n+1)])
        else:
            return([])

    def getStat(self, what):
        if what == "static":
            return (self.__class__.__name__,self.position, self.centerMass)
        if what == "dynamic":
            return (self.__class__.__name__,self.position, self.centerMass, self.velocity)

    def getDiameter():
        largest = 0
        for star in range(len(self.stars))
            for pos in self.stars[star].getPos():
                if pos > largest:
                    largest = pos

    def createStars(self, count):
        for c in range(count):
            xpos = random.gauss(1, 1)
            ypos = random.gauss(1, 1)
            self.stars.append(Star(c, (xpos, ypos), (0, 0), 1))

    def getStarStats(self, what):
        list = []
        for star in range(len(self.stars)):
            list.append(self.stars[star].getStat(what))
        return list
        
    def calcMassDist(self, dtype, granularity):
        extent = math.ceil(getDiameter())
        if dtype == "radial":
            pass
        if dtype == "grid":
            gap = granularity/2
            for xloc in seq(-extent, extent, granularity):
                for yloc in seq(-extent, extent, granularity):
                    for star in 

#[x * 0.1 for x in range(0, 10)]

