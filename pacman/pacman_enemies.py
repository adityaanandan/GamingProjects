import pygame 
import sys 
from settings import* 
BLUE = (0, 0, 255)
class Enemy:
  def __init__(self, app, pos, number): 
    self.app = app
    self.grid_pos = pos
    self.starting_pos = [pos.x, pos.y]
    self.pix_pos = self.get_pix_pos()
    self.radius = int(self.app.cell_width//2.3)
    self.number = number
    self.color = BLUE
    self.direction = vec(0, 0)
    self.personality = self.set_personality()
    self.target = None
    self.speed = self.set_speed()
    def draw(self):
        pygame.draw.circle(self.app.screen, self.color,
                           (int(self.pix_pos.x), int(self.pix_pos.y)), self.radius)

