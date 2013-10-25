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
    
    def step(self, xmag, ymag):
        pass
    
    def getPos(self):
        return self.position
    
    def getVel(self):
        return self.velocity
    
    
class Galaxy():
    def __init__(self, position, velocity, centerMass):
        self.position = position
        self.velocity = velocity
        self.centerMass = centerMass
        self.stars = []
        massDistributions = []
        
    def calcGridMassdistribution(self):
        pass
        
    def genStarDistribution(self, count):
        for c in range(count):
            self.stars.append(Star(c, starPos, starVel))
        pass
    
    
class Space():
    def __init__(self, size):
        self.size = size
        self.galaxys = []
        self.massMaps = []
    
    def createGalaxies(self, count):
        for c in range(couunt):
                    

if __name__ == '__main__':
    pass