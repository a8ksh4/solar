from phys import *
import numpy as np

class Star():
    def __init__(self, position, velocity, mass):
        self.attrs = {}
        self['pos'] = position
        self['vel'] = velocity
        self['mass'] = mass
        self.force = 0.0

    def __str__(self):
        return str(self.attrs)

    def __mul__(self, star, first=True):
        gmm = GrC * self['mass'] * star['mass']
        d1 = round(star['pos'] - self['pos'], -2)
        d2 = -1 * np.copysign(1, d1) * (world_size - abs(d1))
        f1, f2 = 0, 0
        if d1 != 0:
            f1 = gmm / d1
            f2 = gmm / d2
            self.force += f1
            self.force += f2
            if first:
                star.__mul__(self, False)
        #print gmm, d1, d2, f1, f2
        #print self.attrs, gmm, f1, f2

    def __setitem__(self, item, value):
        self.attrs[item] = value

    def __getitem__(self, item=None):
        if item:
            return self.attrs[item]
        else:
            return self['mass'], self['posn'], self['vely']

    #def __call__(self, position_delta):
    #    self.position += position_delta

    def __call__(self):
        #print self.attrs.items()
        self['vel'] += self.force*time_step/self['mass']
        self['pos'] = (self['pos'] + 
                                    self['vel'] * time_step) \
                                            %world_size
        self.force = 0

