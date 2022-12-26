import pygame

class Mesh:
    def __init__(self, size, color):
        self.size = size
        self.color = color

    def draw(self, screen, position):
        pygame.draw.rect(screen, self.color, (position.x, position.y, self.size, self.size))