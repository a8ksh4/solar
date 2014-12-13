from phys import *

class Star():
    def __init__(self, position, velocity, mass):
        self.attrs = {}
        self.attrs['pos'] = position
        self.attrs['vel'] = velocity
        self.attrs['mass'] = mass
        self.force = 0.0

    def __str__(self):
        return str((self.attrs['mass'], 
                    self.attrs['pos'], 
                    self.attrs['vel']))

    def __mul__(self, star):
        gmm = GrC * self.attrs['mass'] * star['mass']
        d1 = star['pos'] - self.attrs['pos']
        f1 = gmm / d1
        f2 = -1 * gmm / (world_size - d1)
        self.force += f1
        self.force += f2
        #print self.attrs, gmm, f1, f2

    def __getitem__(self, item=None):
        if item:
            return self.attrs[item]
        else:
            return self.attrs['mass'], \
                    self.attrs['posn'], \
                    self.attrs['vely']

    #def __call__(self, position_delta):
    #    self.position += position_delta

    def __call__(self):
        print self.attrs.items()
        self.attrs['vel'] += self.force*time_step/self.attrs['mass']
        self.attrs['pos'] = (self.attrs['pos'] + 
                                    self.attrs['vel'] * time_step) \
                                            %world_size
        self.force = 0

