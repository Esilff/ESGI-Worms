from .vector import Vector


class Physics:
    def __init__(self):
        self.position = Vector(0, 0)

        self.timeInAir = 0

    def position(self):
        return self.position()

    def update(self, collider, dt):
        self.timeInAir += dt
        if (self.position.y + 32 <= collider.y):
            self.position.set_vector(-1 * self.position.x, -1 * (-9.81 / 2 * self.timeInAir) + self.position.y) # gravity
