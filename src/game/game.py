import pygame, sys
# import entity class
from ..core.entity import Entity
from..core.collider import Collider
from ..core.eventHandlers.Keyboard import Keyboard

entity = Entity(0, 0)
collider = Collider(-10,500,200,20)


def gameLoop(screen, dt):

    if Keyboard().get_key_down(pygame.K_s):
        entity.mesh.set_color((0,255,255))
    if Keyboard().get_key_down(pygame.K_z):
        entity.mesh.set_color((255,255,0))
    entity.update(collider, dt)
    entity.mesh.draw(screen, entity.transform.position)
    collider.debugDraw(screen)

class Game:
    def __init__(self, name):
        self.screen = None
        self.running = None
        self.name = name
        self.clock = pygame.time.Clock()
        self.dt = 0
        self.FPS_LIMIT = 60
        self.init()
        self.loop()

    def init(self):
        pygame.init()
        self.screen = pygame.display.set_mode((1000, 600))
        pygame.display.set_caption(self.name)
        self.clock.tick(self.FPS_LIMIT)

    def loop(self):
        self.running = True
        while self.running:
            self.dt = self.clock.tick(self.FPS_LIMIT) / 1000
            self.screen.fill((0, 0, 0))  # erase everything on screen
            gameLoop(self.screen, self.dt)
            pygame.display.flip()  # show the new content from instructions
            Keyboard().update()
