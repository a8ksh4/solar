

class Star():
    def __init__(self, position, velocity, mass):
        self.position = position
        self.velocity = velocity
        self.mass = mass

    def __str__(self):
        return (self.mass, self.position, self.velocity)

    def __call__(self, position_delta):
        self.position += position_delta

    def getPos(self):
        return self.position

    def getRelPos(self, relToPos):
        relX = self.pos[0] - relToPos[0]
        relY = self.pos[1] - relToPos[1]
        return (relX, relY)

    def getVel(self):
        return self.velocity

    def getMass(self):
        return self.mass

