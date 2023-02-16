class Vector:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def add(self, vector):
        self.x += vector.x
        self.y += vector.y

    def substract(self, vector):
        self.x -= vector.x
        self.y -= vector.y

    def __add__(self, val):
        if isinstance(val, (int,float, complex)):
            return Vector(self.x + val, self.y + val)
        elif isinstance(val, Vector):
            return Vector(self.x + val.x, self.y + val.y)
        else:
            raise TypeError("Vectors and numbers are the only types that can be added to a Vector")

    def __sub__(self, val):
        if isinstance(val, (int,float, complex)):
            return Vector(self.x - val, self.y - val)
        elif isinstance(val, Vector):
            return Vector(self.x - val.x, self.y - val.y)
        else:
            raise TypeError("Vectors and numbers are the only types that can be subbed to a Vector")
    def __truediv__(self, val):
        if isinstance(val, (int, float, complex)):
            return Vector(self.x / val, self.y / val)
        else:
            raise TypeError("A number is required to divide vector values")

    def set_vector(self, x, y):
        self.x = x
        self.y = y
