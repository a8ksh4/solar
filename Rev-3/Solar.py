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

def animate(half):
    fig, ax = plt.subplots()
    def getPosSize(stars):
        position, size = [], []
        for star in stars:
            sx, sv, ss = star
            position.append(sx)
            size.append(ss)
        #print position, size
        return position, size
    stars = [star for star in half]
    pos, size = getPosSize(stars)
    points, = ax.plot(pos, size, marker='o', linestyle='None')
    ax.set_xlim(0, half.size)
    ax.set_ylim(0, 11)
    for t in range(1000):
        half.update()
        pos, size = getPosSize(half)
        points.set_data(pos, size)
        plt.pause(0.01)

if __name__ == '__main__':
    half = Half(512)
    half.insertRandStars(5)
    half.printObjects()
   
    print "Num Stars is:", len(half)
    #graphVis( (s for s in half) )
    #graphVis(half)
    animate(half)

    #quad.printObjects()

    #for object in quad.getObjectList():
    #    print object

