import pygame
from random import randint
from noncepaddle import Paddle
from nonceball import Ball
pygame.init()
# define colors 
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
BLUE = (0, 0, 255)
GREEN = (0, 255, 0)
RED = (255, 0, 0)
SCREEN = (700, 500)
gamewindow = pygame.display.set_mode(SCREEN)
clock = pygame.time.Clock()
# initialize the specific sprites 
paddle = Paddle(WHITE, 100, 10)
paddle.rect.x = 150
paddle.rect.y = 480
ball = Ball(WHITE, 10, 10)
ball.rect.x = randint(0,680)
ball.rect.y = 20

all_sprites_list = pygame.sprite.Group()
all_sprites_list.add(paddle)
all_sprites_list.add(ball)
# main game loop 
gameover = 1
while gameover == 1:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            gameover = 0
    if event.type == pygame.KEYDOWN: 
        if event.key == pygame.K_LEFT:
            paddle.moveleft(5)
        elif event.key == pygame.K_RIGHT:
            paddle.moveright(5)


    if ball.rect.y >= 480:
        ball.rect.x = randint(10, 400)
        ball.rect.y = 10

    if ball.rect.y<=5:
       ball.velocity=-ball.velocity
       ball.rect.x = randint(10, 400)

    
        
 # detect collision    
    if pygame.sprite.collide_mask(ball, paddle):
        ball.bounce()
    
    all_sprites_list.update() 
 # draw sprites + background   
    gamewindow.fill(BLACK)
    all_sprites_list.draw(gamewindow)
    pygame.display.flip()
    clock.tick(60)
pygame.quit()
       
