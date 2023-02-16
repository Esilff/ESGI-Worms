from .vector import Vector


class Physics:
    def __init__(self):
        self.position = Vector(0, 0)
        self.lastPosition = Vector(0,0)
        self.velocity = Vector(0,0)
        self.initialVelocity = Vector(0,0)
        self.acceleration = Vector(0,0)
        self.timeInAir = 0
        self.gravity = 9.81
        self.dt = 1;
        self.currentTime = 0
        self.lastTime = 0

    def position(self):
        return self.position

    def update(self, collider, dt):
        self.lastPosition = self.position
        self.position.set_vector(self.velocity.x * self.dt + self.position.x,
                                 (self.gravity / 2 * self.dt ** 2) + self.velocity.y * self.dt + self.position.y)  # gravity
        self.velocity = (self.velocity - self.initialVelocity) / 2
        if (self.position.y + 32 <= collider.y):
            self.gravity = 9.81
        else:
            self.gravity = 0

    def add_force(self, vector):
        if (self.velocity == Vector(0,0)):
            self.initialVelocity = vector
        self.velocity.add(vector)
