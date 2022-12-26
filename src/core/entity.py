# import the transform class
from .transform import Transform
from .render.mesh import Mesh

class Entity:
    def __init__(self, x,y):
        self.transform = Transform(x,y)
        self.mesh = Mesh(32, (255,255,255))

    def update(self):
        pass

    def applyGravity(self):
        self.transform.position.y += 0.01


    