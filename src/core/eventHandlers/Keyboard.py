import pygame

class Keyboard:
    instance = None

    def __init__(self):
        self.key_pressed = pygame.key.get_pressed()

    def __call__(self, *args, **kwargs):
        if self.instance is None:
            self.instance = super().__new__(self)
        return self.instance

    def update(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
            else:
                self.key_pressed = pygame.key.get_pressed()

    def get_key_down(self, key):
        return self.key_pressed[key]
