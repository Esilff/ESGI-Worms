from .vector import Vector


class Physics:
    def __init__(self):
        self.position = Vector(0, 0)
        
        self.timeInAir = 0

    def position(self):
        return self.position()

    def update(self):
        self.timeInAir -= 0.001
        self.position.set_vector(self.position.x, (-9.81 / 2 * self.timeInAir) + self.position.y);
