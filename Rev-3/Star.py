

class Star():
    def __init__(self, position, velocity, mass):
        self.position = position
        self.velocity = velocity
        self.mass = mass

    def __str__(self):
        return str((self.mass, self.position, self.velocity))

    def __call__(self, position_delta):
        self.position += position_delta

