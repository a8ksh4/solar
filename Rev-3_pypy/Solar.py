#!/usr/bin/python
from Half import *
from phys import *
import sys, os
import numpy as np

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

def animate(half):
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
    ax.set_ylim(0, star_max_mass+1)
    ax.set_yscale('log')
    #while True:
    for t in range(world_iters):
        half.update()
        #half.normalize()
        pos, size = getPosSize(half)
        points.set_data(pos, size)

if __name__ == '__main__':
    half = Half()
    half.insertRandStars(90)
    #half.insertStar(1000, 0, 900)
    #half.insertStar(1500, 0, 1)
    half.printObjects()
   
    print "Num Stars is:", len(half)
    #graphVis( (s for s in half) )
    #graphVis(half)
    #animate(half)
    for t in range(world_iters):
        half.update()
    half.printObjects()


    #quad.printObjects()

    #for object in quad.getObjectList():
    #    print object

