import pygame, sys
#import entity class
from ..core.entity import Entity

entity = Entity(0,0)

def gameLoop(screen):
    entity.mesh.draw(screen, entity.transform.position)

class Game :
    def __init__(self, name):
        self.name = name

        
        self.init()
        self.loop()

    def init(self):
        pygame.init()
        self.screen = pygame.display.set_mode((640,320))
        pygame.display.set_caption(self.name)

    def loop(self):
        self.running = True
        while self.running:
            self.screen.fill((0, 0, 0)) #erase everything on screen

            gameLoop(self.screen)
            entity.transform.position.y += 0.01

            pygame.display.flip() #show the new content from instructions
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    running = False
                    pygame.quit()
                    sys.exit()






    
        
