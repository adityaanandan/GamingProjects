import pygame 
import sys 
from settings import* 
# main class for the app 
class App:
    def __init__(self):
        self.screen = pygame.display.set_mode((WIDTH, HEIGHT))
        def load(): 
          self.background = pygame.image.load('pacman background.png')
          self.background = pygame.transform.scale(self.background, MAZE_WIDTH, MAZE_HEIGHT)
        def playing_draw(self):
          self.screen.fill(BLACK)
          self.screen.blit(self.background, (TOP_BOTTOM_BUFFER//2, TOP_BOTTOM_BUFFER//2))
          pygame.display.update()

    
