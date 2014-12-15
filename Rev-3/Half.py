from Star import *
from phys import * 
import random
#import phys

class Half():
    def __init__(self, size=world_size, origin=0, level=0, pos=None):
        self.origin = origin
        self.size = size
        self.stars = []
        self.t_step = time_step
        self.energy = 0

    def __add__(self, star):
        self.addStar(star)

    def __sub__(self, star):
        self.subStar(star)

    def __len__(self):
        return len(self.stars)

    def __iter__(self):
        for star in self.stars:
            yield (star['pos'], star['vel'], star['mass'])

    def normalize(self):
        max_size = max([s['mass'] for s in self.stars])
        for star in self.stars:
            if star['mass'] == max_size:
                pos_offset = star['pos']
                vel_offset = star['vel']
                break
        for star in self.stars:
            star['pos'] = (star['pos'] - pos_offset) % world_size
            star['vel'] -= vel_offset

    def update(self):
        self.energy = 0
        for star in self.stars:
            for other in self.stars:
                if star is other:
                    continue
                star * other
        for star in self.stars:
            star()
            self.energy += 0.5 * star['mass'] * pow(star['vel'], 2)

    def addStar(self, star):
        self.stars.append(star)

    def subStar(self, star):
        self.stars.remove(star)

    def insertStar(self, pos, vel, mass):
        self.addStar(Star(pos, vel, mass))

    def insertRandStars(self, count=5):
        for num in range(count):
            pos = float(random.randint(0, self.size/2))
            vel = float(random.randint(0, 200))
            mass = float(random.randint(1, star_max_mass))
            self.addStar(Star(pos, vel, mass))

    def printObjects(self):
        for star in self.stars:
            print star
