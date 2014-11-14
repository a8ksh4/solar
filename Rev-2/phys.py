'''
Created on Oct 23, 2013

@author: drnorris
'''

import math

g = 6.674 * math.pow(10,-11) # Gravitational constant
su = 1.989 * math.pow(10, 30) # Mass of our Sun, using this as a reference for other stars of different sizes.
au = 149597871
#planet_diameter = math.random.randrange(2000,140000)
sr = 6.955 * math.pow(10,8) #Solar Radii in meters, Don't forget that this number needs to be divided by 1000 for our scale.
em = 6.972*math.pow(10,24) # Earth's mass, in kg

def calcPull(massOne, massTwo, massOnePos, massTwoPos):
    distance = math.sqrt( math.pow(math.abs(massOnePos[0] - massTwoPos[0]), 2) + math.pow(math.abs(massOnePos[1] - massTwoPos[1]), 2))
    force = g * massOne * massTwo / math.pow(distance, 2)
    return force

def calcNewVel(currentVelocity, objectMass, forceApplied, stepInterval):
    pass


def calcCenterOfMass(objects, totalMass=None):
    if totalMass == None:
        totalMass = 0
        for obj in objects:
            print "phys.ccom obj: " + str(obj)
            totalmass += obj[1]
    print "phys.ccom totalMass: " + str(totalMass)

    wxtmp = 0  #weighted relative x temp variable
    wytmp = 0  #weighted relative y temp variable
    for obj in objects:
        print "phys.ccom obj: " + str(obj)
        objX = float(obj[0][0])
        objY = float(obj[0][1])
        objM = obj[1]

        wxtmp += objX * objM
        wytmp += objY * objM
    realX = wxtmp / totalMass
    realY = wytmp / totalMass
    centerOfMass = (realX, realY)

    return centerOfMass

