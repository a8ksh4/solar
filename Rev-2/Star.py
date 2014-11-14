#!/usr/bin/python
'''
Created on Oct 23, 2013

@author: drnorris
'''


class Star():
    def __init__(self, position, velocity, mass):
        #self.myID = id
        self.position = position
        self.velocity = velocity
        self.forceApplied = (0.0, 0.0)
        self.mass = mass
        self.markDel = False
        massDistributions = []

    def markForDel(self):
        self.markDel = True

    def getStat(self, what = "static"):
        if what == "static":
            return (self.position, self.mass)
        if what == "dynamic":
            return (self.position, self.mass, self.velocity)
    
    def step(self, xdelta, ydelta):
        pass
    
    def getPos(self):
        return self.position
   
    def getRelPos(self, relToPos):
        relX = self.pos[0] - relToPos[0]
        relY = self.pos[1] - relToPos[1]
        return (relX, relY)
         
    def getVel(self):
        return self.velocity

    def getMass(self):
        return self.mass
