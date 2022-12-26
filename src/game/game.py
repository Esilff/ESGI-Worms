import pygame, sys

class Game :
    def __init__(self, name):
        self.name = name
        self.loop_func = None
        self.init()
        self.loop()

    def init(self):
        pygame.init()
        self.screen = pygame.display.set_mode((640,320))
        pygame.display.set_caption(self.name)

    def loop(self):
        self.running = True
        while self.running:
            self.screen.fill((0, 0, 0))
            if self.loop_func :
                self.loop_func
            pygame.display.flip()
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    running = False
                    pygame.quit()
                    sys.exit()






    
        
