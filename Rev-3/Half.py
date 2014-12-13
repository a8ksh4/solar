from Star import *
import random
#import phys

class Half():
    def __init__(self, size, origin=0, level=0, pos=None):
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
            yield (star['position'], star['velocity'], star['mass'])

    def update(self):
        self.total_mass = sum([x['mass'] for x in self.stars])
        self.mass_center = sum([x['mass']*x['position'] \
                                    for x in self.stars]) / self.total_mass
        for star in self.stars:
            pos, mass = star['position'], star['mass']
            mass_d_1 = abs(pos - self.mass_center)
            mass_d_2 = abs(self.size - pos + self.mass_center)
            mass_distance = min(mass_d_1, mass_d_2)
            force = self.total_mass / (mass_distance * mass_distance)
            star(force)

    def addStar(self, star):
        self.stars.append(star)

    def subStar(self, star):
        self.stars.remove(star)

    def insertRandStars(self, count=5):
        for num in range(count):
            pos = random.randint(0, self.size)
            vel = random.randint(0, 10)
            mass = random.randint(0, 10)
            self.addStar(Star(pos, vel, mass, self.size, self.t_step))

    def printObjects(self):
        for star in self.stars:
            print star
