from typing import Final



class Vector:
    def __init__(self, x,y) :
        self.x = x
        self.y = y


    def add(self, vector):
        self.x += vector.x
        self.y += vector.y

    def substract(self, vector):
        self.x -= vector.x
        self.y -= vector.y


