# import the transform class
from .transform import Transform
from .physics import Physics
from .render.mesh import Mesh


class Entity:
    def __init__(self, x, y):
        self.transform = Transform(x, y)
        self.physics = Physics()
        self.mesh = Mesh(32, (255, 255, 255))

    def update(self, collider, dt):
        self.physics.update(collider, dt)
        self.transform.position = self.physics.position
        print(f"Velocity : {self.physics.velocity.x} ; {self.physics.velocity.y}")

