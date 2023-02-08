import pygame, sys
# import entity class
from ..core.entity import Entity
from..core.collider import Collider
import time

entity = Entity(0, 0)
collider = Collider(-10,500,200,20)


def gameLoop(screen):
    entity.update(collider)
    entity.mesh.draw(screen, entity.transform.position)
    collider.debugDraw(screen)


class Game:
    def __init__(self, name):
        self.screen = None
        self.running = None
        self.name = name
        self.init()
        self.loop()

    def init(self):
        pygame.init()
        self.screen = pygame.display.set_mode((1000, 600))
        pygame.display.set_caption(self.name)

    def loop(self):
        self.running = True
        while self.running:
            self.screen.fill((0, 0, 0))  # erase everything on screen

            gameLoop(self.screen)
            pygame.display.flip()  # show the new content from instructions
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    running = False
                    pygame.quit()
                    sys.exit()
