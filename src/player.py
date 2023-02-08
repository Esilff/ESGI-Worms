import pygame

class Character:
    def __init__(self, x, y, width, height, speed, gravity, jump_strength):
        # Position et dimensions du personnage
        self.x = x
        self.y = y
        self.width = width
        self.height = height

        # Vitesse et gravité du personnage
        self.speed = speed
        self.gravity = gravity

        # Force du saut du personnage
        self.jump_strength = jump_strength

        # Créer un rectangle de collision pour le personnage
        self.rect = pygame.Rect(x, y, width, height)

    def move_left(self):
        # Déplacer le personnage vers la gauche
        self.x -= self.speed

    def move_right(self):
        # Déplacer le personnage vers la droite
        self.x += self.speed

    def jump(self):
        # Appliquer une force de saut au personnage
        self.y -= self.jump_strength

    def apply_gravity(self):
        # Appliquer la gravité au personnage
        self.y += self.gravity

    def check_collision(self, platform):
        # Vérifier si le personnage entre en collision avec une plateforme
        if self.rect.colliderect(platform.rect):
            # Si oui, mettre à jour la position du personnage pour qu'il soit au-dessus de la plateforme
            self.rect.bottom = platform.rect.top
            self.y = self.rect.y