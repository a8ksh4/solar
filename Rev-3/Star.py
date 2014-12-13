

class Star():
    def __init__(self, position, velocity, mass, env_size, time_step):
        self.attrs = {}
        self.attrs['position'] = position
        self.attrs['velocity'] = velocity
        self.attrs['mass'] = mass
        self.env_size = env_size
        self.time_step = time_step

    def __str__(self):
        return str((self.attrs['mass'], 
                    self.attrs['position'], 
                    self.attrs['velocity']))

    def __getitem__(self, item=None):
        if item:
            return self.attrs[item]
        else:
            return self.attrs['mass'], \
                    self.attrs['position'], \
                    self.attrs['velocity']

    #def __call__(self, position_delta):
    #    self.position += position_delta

    def __call__(self, force):
        self.attrs['velocity'] += force*self.time_step
        self.attrs['position'] = (self.attrs['position'] + 
                         self.attrs['velocity'] * self.time_step) \
                            %self.env_size

