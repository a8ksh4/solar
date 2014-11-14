'''
Created on Oct 23, 2013

@author: drnorris
'''

from Star import *
import random
import phys
#from phys import *


class Quad():
    def __init__(self, size, bottomLeft = (0, 0), level=0, pos=None):
        self.bottomLeft = bottomLeft     #absolute location, not relative
        self.width = size
        self.halfWidth = self.width/2
        self.center = (self.bottomLeft[0] + self.halfWidth, self.bottomLeft[1] + self.halfWidth)  #abs, not rel
        self.mass = 0
        self.centerOfMass = self.center   #absolute center, not relative
        self.starLimit = 10
        self.starLimitOffset = 2
        self.stars = []
        self.childStarCount = 0
        self.childNodes = {}
        self.childNodeCOMs = {}    #list of mass centers for each child. 
        self.massTotal = 0
        self.level = level
        self.pos = pos
        random.seed(a=0)


    def update(self):
        # Game Flow:  Calculte mass of every quad, then calculate center of mass for every quad. 
        # Pass the mass centers of every quad to every other quad (using listMassCenters to get 
        # lists from each quad to pass). Once stars have applied force, step their position and
        # check if they need to be moved to a new quad.  Refactor quads as needed. Repeat.
        self.calcMass()
        self.calcCenterOfMass()
        self.calcPassForceOnStars()
        self.listMassCenters()


    def listMassCenters(self):
        if self.childStarCount != 0:
            for key in self.childNodes.keys():
                self.childNodeCOMs[key] = self.childNodes[key].listMassCenters
            returnVal = [i for i in self.childNodeCOMs[key] for key in self.childNodes.keys()]
            print returnVal
            return returnVal
        else:
            return ((self.centerOfMass, self.mass), )
    
    
    def passMassCenters(self, massCenters):
        if self.childStarCount != 0:
            for key in self.childNodes.keys():
                self.childNodes[key]([self.childNodeCOMs[k] for k in self.childNodeCOMs.keys if k != key])
        else:
            for c in range(len(self.stars)):
                massCentersToPass = massCenters
                for d in range(len(self.stars)):
                    massCentersToPass.append(self.stars[d].getStat())
                self.star.calcForce(massCentersToPass)
            

    def step(self):
        misplacedStars = []
        if self.childStarCount != 0:
            for key in self.childNodes.keys():
                misplacedStars = self.childNodes.step()
        else:
            for c in range(len(self.stars)):
                newLoc = self.stars[c].step()
                if (newLoc[0] < self.bottomLeft[0] or newLoc[0] > self.bottomLeft[0] + self.width) or (newLoc[1] < self.bottomLeft[1] or newLoc[1] > self.bottomLeft[1] + self.width):
                    misplacedStars.append(self.stars[c])
                    self.stars[c].markForDel()
        for c in range(len(self.stars)):
            if self.stars[c].markDel == True:
                del self.stars[c]
            

    def calcPassForceOnStars(self, massCenters):
        if self.childStarCount != 0:
                for key in self.childNodes.keys():
                    self.childNodes[key].calcPassForceOnStars([ massCenter for massCenters in self.childNodes[copy].listMassCenters() for copy in self.childNodes.keys() if copy != key ])
        else:
            if len(self.stars) > 0:
                for c in range(len(self.stars)):
                    self.stars[c].clearForce()
                for massCenter in massCenters + [ self.stars[i].getStat("static") for i in range(len(self.stars)) ]
                    for c in range(len(self.stars)):
                        self.stars[c].addForceFrom(massCenter)


    def calcCenterOfMass(self):
        if len(self.stars) == 0:
            if self.childStarCount == 0:
                self.centerOfMass = (self.bottomLeft[0] + self.halfWidth, self.bottomLeft[1] + self.halfWidth)
                return
            else:
                for key in self.childNodes.keys():
                    self.childNodes[key].calcCenterOfMass()
                self.centerOfMass = phys.calcCenterOfMass([((self.childNodes[k].centerOfMass), self.childNodes[k].mass) for k in self.childNodes.keys()], self.mass)
                
        else:
            self.centerOfMass = phys.calcCenterOfMass([i.getStat("static") for i in self.stars], self.mass)

 
    def calcMass(self):
        self.mass = 0
        if len(self.stars) == 0:
            for key in self.childNodes.keys():
                self.mass += self.childNodes[key].calcMass()
        else:
            for count in range(len(self.stars)):
                self.mass += self.stars[count].getMass()
        return self.mass

    
    def insertRandStars(self, count):
        for c in range(count):
            pos = (random.randint(0, self.width), random.randint(0, self.width))
            vel = (0, 0)
            mass = 1
            star = Star(pos, vel, mass)
            self.addStar(star)


    def addStar(self, star):
        #print "in addstar lvl " + str(self.level)
        if self.childStarCount == 0:
            #print "in addstar childc==0"
            self.stars.append(star)
            if len(self.stars) > self.starLimit + self.starLimitOffset:
                #print "in addstar childc split"
                self.split()
        else:
            self.addStarToChild(star)


    def addStarToChild(self, star):
            #print "in addstartochild - csc is: " + str(self.childStarCount)
            self.childStarCount += 1
            #print "csc is: " + str(self.childStarCount)
            if star.getPos()[0] < self.bottomLeft[0] + self.halfWidth:
                if star.getPos()[1] < self.bottomLeft[1] + self.halfWidth:
                    self.childNodes["sw"].addStar(star)
                else:
                    self.childNodes["nw"].addStar(star)
            else:
                if star.getPos()[1] < self.bottomLeft[1] + self.halfWidth:
                    self.childNodes["se"].addStar(star)
                else:
                    self.childNodes["ne"].addStar(star)


    def split(self):
        if self.width <= 2:
            pass
        else:
            for quad in ("sw", "nw", "se", "ne"):
                if quad not in self.childNodes:
                    if quad == "sw":
                        newBottomLeft = self.bottomLeft
                    elif quad == "nw":
                        newBottomLeft = (self.bottomLeft[0], self.bottomLeft[1] + self.halfWidth)
                    elif quad == "se":
                        newBottomLeft = (self.bottomLeft[0] + self.halfWidth, self.bottomLeft[1])
                    else:
                        newBottomLeft = (self.bottomLeft[0] + self.halfWidth, self.bottomLeft[1] + self.halfWidth)

                    self.childNodes[quad] = Quad(self.halfWidth, newBottomLeft, self.level + 1, quad)

            for star in self.stars:
                self.addStarToChild(star)
            self.stars = []


    def unsplit(self):
        for node in self.childNodes.keys():
            for star in self.childNodes[node].remStars():
                self.stars.append(star)
        self.childStarCount = 0


    def remStars(self):
        if len(self.stars) > 0:
            stars = self.stars
            self.stars = []
            return stars
        else:
            stars = []
            for key in self.childNodes.keys():
                for star in self.childNodes[key].remStars():
                    stars.append(star)
            self.childStarCount = 0
            return stars


    def printObjects(self):
        print "level: " + str(self.level) +\
              " Quad: " + str(self.pos) +\
              " self.stars: " + str(len(self.stars)) +\
              " self.cStars: " + str(self.childStarCount) + \
              " self.m: " + str(self.mass) +\
              " self.bL " + str(self.bottomLeft) +\
              " self.w " + str(self.width) +\
              " self.cOM: " + str(self.centerOfMass)
        if self.centerOfMass[0] < self.bottomLeft[0] or self.centerOfMass[0] > self.bottomLeft[0] + self.width:
            print "COM out of bounds X"
        if self.centerOfMass[1] < self.bottomLeft[1] or self.centerOfMass[1] > self.bottomLeft[1] + self.width:
            print "COM out of bounds Y"
        if len(self.stars) == 0:
            for key in self.childNodes.keys():
                self.childNodes[key].printObjects()
        else:
            pass
            #print self.stars


    def getObjectList(self):
        objects = []
        for star in self.stars:
            objects.append(star)
        for key in self.childNodes.keys():
            for star in self.childNodes[key].getObjectList():
                objects.append(star)
        return objects


    def getObjectCount(self):
        #print "in getobjcount - len self.stars is: " + str(len(self.stars))
        if len(self.stars) == 0:
            return self.childStarCount
        else:
            return len(self.stars)

