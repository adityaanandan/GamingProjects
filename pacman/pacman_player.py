import pygame 
from pacman_settings import* 
vec = pygame.math.Vector2()
class Player: 
  def__init__(self, app, pos):
    self.velocity = 2 
    self.starting_point = [pos.x, pos.y] 
    self.direction = vec(1,0)
    self.pix_pos = self.get_pix_pos()
    self.grid_pos = pos 
    self.stored_direction(self)
  def pac_move(self, direction): 
    self.stored_direction = direction
  def draw_pac:
    pygame.draw.circle(self.app.screen, PLAYER_COLOUR, (int(self.pix_pos.x), int(self.pix_pos.y)), self.app.cell_width//2-2)
  def get_pix_pos(self):
    
    

    
    
    
      
    
    
