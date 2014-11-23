#!/usr/bin/python
from Half import *
import sys, os
import numpy as np
import matplotlib.pyplot as plt

MYNAME=sys.argv[0]
MYPATH=os.path.realpath(__file__)
MYDIR=os.path.dirname(os.path.abspath(__file__))
MYCWD=os.getcwd()

print "sys.argv[0] is: " + MYNAME
print "os.path.realpath(__file__) is: " + MYPATH
print "os.path.dirname(os.path.abspath(__fiel__)) is: " + MYDIR
print "os.getcwd() is: " + MYCWD

def graphVis(stars):
    #x = np.array()
    #y = np.array()
    #size = np.array()
    #velo = np.array()
    position, size, velocity = [], [], []
    for star in stars:
        sx, sv, ss = star
        position.append(sx)
        size.append(ss)
        velocity.append(sv)
    print "Pos:", position
    print "Size:", size
    print "Velo:", velocity
    plt.scatter(position, size, velocity, alpha=0.5)
    plt.show()
    

if __name__ == '__main__':
    half = Half(512)
    half.insertRandStars(5)
    half.printObjects()
   
    print "Num Stars is:", len(half)
    #graphVis( (s for s in half) )
    graphVis(half)

    #quad.printObjects()

    #for object in quad.getObjectList():
    #    print object

