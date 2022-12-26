import src.game.game as Game
import pygame



game = Game.Game("Window")

def drawRedCircle():
    pygame.draw.circle(game.screen, (255, 0, 0), (320, 240), 50)

game.loop_func = drawRedCircle()