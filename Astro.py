#!/usr/bin/python
'''
Created on Oct 23, 2013

@author: drnorris
'''

#from space import Space
import sys, os
#import space

MYNAME=sys.argv[0]
MYPATH=os.path.realpath(__file__)
MYDIR=os.path.dirname(os.path.abspath(__file__))
MYCWD=os.getcwd()

print MYNAME
print MYPATH
print MYDIR
print MYCWD

if __name__ == '__main__':
    mySpace = Space(360)
    mySpace.createGalaxies(3)
    print mySpace.getObjectList()
