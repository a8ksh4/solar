from Star import *
import random
#import phys

class Half():
    def __init__(self, size, origin=0, level=0, pos=None):
        self.origin = origin
        self.size = size
        self.stars = []

    def __add__(self, star):
        self.addStar(star)

    def __sub__(self, star):
        self.subStar(star)

    def __len__(self):
        return len(self.stars)

    def __iter__(self):
        for star in self.stars:
            yield (star.position, star.velocity, star.mass)

    def update(self):
        for star in half:
            for star in half:
                pass

    def addStar(self, star):
        self.stars.append(star)

    def subStar(self, star):
        self.stars.remove(star)

    def insertRandStars(self, count=5):
        for num in range(count):
            pos = random.randint(0, self.size)
            vel = random.randint(0, 10)
            mass = random.randint(-10, 10)
            self.addStar(Star(pos, vel, mass))

    def printObjects(self):
        for star in self.stars:
            print star
