import pygame
class Collider:
    def __init__(self,x,y, width, height):
        self.x = x
        self.y = y
        self.width = width
        self.height = height

    def debugDraw(self, screen):
        pygame.draw.rect(screen, (255,0,0), (self.x, self.y, self.width, self.height))
