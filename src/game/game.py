import pygame

class Game :
    def __init__(self, name):
        self.name = name
        self.init()
        self.loop()

    def init(self):
        pygame.init()
        self._screen = pygame.display.set_mode((640,320))
        pygame.display.set_caption(self.name)

    def loop(self):
        self.running = True
        while self.running:
            self._screen.fill((0, 0, 0))
            pygame.draw.circle(self._screen, (255, 0, 0), (320, 240), 50)
            pygame.display.flip()
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    running = False
        pygame.quit()
