from Star import *
from phys import * 
import random
#import phys

class Half():
    def __init__(self, size=world_size, origin=0, level=0):
        self.origin = origin
        self.size = size
        self.midpoint = origin + size/2
        self.halves = []
        self.stars = []
        self.t_step = time_step
        self.energy = 0
        self.level = level

    def __add__(self, star):
        #add a star into the half object
        self.stars.append(star)

    def __sub__(self, star):
        #rem a star from the half object
        self.stars.remove(star)

    def __len__(self):
        #return number of stars in half object
        return len(self.stars)

    def __iter__(self):
        #yield star attrs for each star
        for star in self.stars:
            yield star

    def __call__(self):
        self.checkSplit()
        self.pull()
        self.update()

    def checkSplit(self):
        if self.halves and sum([len(h) for h in self.halves]) < split_range[0]:
            #Unsplit
            for half in self.halves:
                self.stars += half.stars
            self.halves = []
        elif not self.halves and len(self.stars) > split_range[1]:
            #Split
            half_size = self.size / 2
            new_level = self.level + 1
            for origin in self.origin, self.midpoint:
                self.halves.append(half(half_size, origin, level))
            for star in self.stars:
                if star['pos'] < self.midpoint:
                    self.halves[0] += star
                else:
                    self.halves[1] += star
            self.stars = []

    def pull(self):
        if self.halves:
            self.stars = []
            for half in self.halves:
                self.stars += half.pull()

        
        out = self.stars[0].copy()
        for star in self.stars[1:]:
            out + star
        return [out,]
        
    def update(self, s_list=[]):
        if self.halves:
            for half in halves:
                stars = ((s for s in self.stars + s_list if not s in half))
                half.update(stars)
        else:
            for star in self.stars:
                for other in self.stars:
                    if other is not star:
                        star * other
                for other in s_list:
                    star * other
            for star in self.stars:
                star()

    def insertStar(self, pos, vel, mass):
        self.addStar(Star(pos, vel, mass))

    def insertRandStars(self, count=5):
        for num in range(count):
            pos = float(random.randint(0, self.size/2))
            vel = float(random.randint(0, 200))
            mass = float(random.randint(1, star_max_mass))
            self + Star(pos, vel, mass)

    def printObjects(self, max_level=999):
        if self.level < max_level:
            if self.halves:
                for half in self.halves:
                    half.printObjects(max_level)
            else:
                for star in self.stars:
                    print star
        else:
            for star in self.stars:
                print star
