#!/usr/bin/python
'''
Created on Oct 23, 2013

@author: drnorris
'''

#from space import Space
from Space import *
#import Space, Galaxy, Star
import sys, os
#import space

MYNAME=sys.argv[0]
MYPATH=os.path.realpath(__file__)
MYDIR=os.path.dirname(os.path.abspath(__file__))
MYCWD=os.getcwd()

print "sys.argv[0] is: " + MYNAME
print "os.path.realpath(__file__) is: " + MYPATH
print "os.path.dirname(os.path.abspath(__fiel__)) is: " + MYDIR
print "os.getcwd() is: " + MYCWD

if __name__ == '__main__':
    mySpace = Space(360)
    mySpace.createGalaxies(3)
    for object in mySpace.getObjectList():
        print object
