from Star import *
from phys import * 
import random
#import phys

class Half():
    def __init__(self, size=world_size, origin=0, level=0, pos=None):
        self.origin = origin
        self.size = size
        self.stars = []
        self.t_step = .1

    def __add__(self, star):
        self.addStar(star)

    def __sub__(self, star):
        self.subStar(star)

    def __len__(self):
        return len(self.stars)

    def __iter__(self):
        for star in self.stars:
            yield (star['pos'], star['vel'], star['mass'])

    def update(self):
        for star in self.stars:
            for other in self.stars:
                if star is other:
                    continue
                star * other
        for star in self.stars:
            star()
    #def update(self):
    #    self.total_mass = sum([x['mass'] for x in self.stars])
    #    self.mass_center = sum([x['mass']*x['pos'] \
    #                                for x in self.stars]) / self.total_mass
    #    for star in self.stars:
    #        pos, mass = star['pos'], star['mass']
    #        mass_d_1 = abs(pos - self.mass_center)
    #        mass_d_2 = abs(self.size - pos + self.mass_center)
    #        mass_distance = min(mass_d_1, mass_d_2)
    #        force = self.total_mass / (mass_distance * mass_distance)
    #        star(force)

    def addStar(self, star):
        self.stars.append(star)

    def subStar(self, star):
        self.stars.remove(star)

    def insertRandStars(self, count=5):
        for num in range(count):
            pos = float(random.randint(0, self.size))
            vel = float(random.randint(0, 10))
            mass = float(random.randint(1, star_max_mass))
            self.addStar(Star(pos, vel, mass))

    def printObjects(self):
        for star in self.stars:
            print star
