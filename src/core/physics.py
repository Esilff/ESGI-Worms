from .vector import Vector


class Physics:
    def __init__(self):
        self.position = Vector(0, 0)

        self.timeInAir = 0

    def position(self):
        return self.position()

    def update(self, collider):
        self.timeInAir -= 0.0005
        if (self.position.y + 32 <= collider.y):
            self.position.set_vector(self.position.x, (-9.81 / 2 * self.timeInAir) + self.position.y);
