#!/usr/bin/python
'''
Created on Oct 23, 2013

@author: drnorris
'''


class Star():
    def __init__(self, myID, position, velocity, mass):
        self.myID = id
        self.position = position
        self.velocity = velocity
        self.mass = mass
        massDistributions = []

    def getStat(self, what):
        if what == "static":
            return (self.__class__.__name__, self.position, self.mass)
        if what == "dynamic":
            return (self.__class__.__name__, self.position, self.mass, self.velocity)
    
    def step(self, xdelta, ydelta):
        pass
    
    def getPos(self):
        return self.position
    
    def getVel(self):
        return self.velocity
