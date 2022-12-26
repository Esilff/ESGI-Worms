from .vector import Vector

class Transform:
    def __init__(self, x,y):
        self.position = Vector(x,y);
        self.rotation = 0