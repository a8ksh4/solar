#!/usr/bin/python
'''
Created on Oct 23, 2013

@author: drnorris
'''

from Quad import *
import sys, os

MYNAME=sys.argv[0]
MYPATH=os.path.realpath(__file__)
MYDIR=os.path.dirname(os.path.abspath(__file__))
MYCWD=os.getcwd()

#print "sys.argv[0] is: " + MYNAME
#print "os.path.realpath(__file__) is: " + MYPATH
#print "os.path.dirname(os.path.abspath(__fiel__)) is: " + MYDIR
#print "os.getcwd() is: " + MYCWD

if __name__ == '__main__':
    quad = Quad(360, (0,0), 0)
    quad.insertRandStars(100)
    quad.update()
    print "getObjectCount is: " + str(quad.getObjectCount())

    quad.printObjects()

    #for object in quad.getObjectList():
    #    print object
