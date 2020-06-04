import pygame
from setup import setup
from pygame import mixer 
pygame.mixer.init()
from paddle import Paddle
from random import randint
from ball import Ball 
pygame.init()
# Define some colors
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
BLUE = (0, 0, 255)
GREEN = (0, 255, 0)
RED = (255, 0, 0)
# display setup 
SCREEN_WIDTH = 700
SCREEN_HEIGHT = 500
BALL_SIZE = 25
clock = pygame.time.Clock()
size = (700, 500)
screen = pygame.display.set_mode(size)
pygame.display.set_caption("Pong")
#varaiables
playerB = 0
playerA = 0
reactiontime = 100
AIvelocity=5
#paddle 
paddleA = Paddle(WHITE, 10, 100)
paddleA.rect.x = 20
paddleA.rect.y = 200


paddleB = Paddle(WHITE, 10, 100)
paddleB.rect.x = 670
paddleB.rect.y = 200

ball = Ball(WHITE, 10, 10)
ball.rect.x = 345
ball.rect.y = 195

player=setup()
print (player)

all_sprites_list = pygame.sprite.Group()
all_sprites_list.add(paddleA)
all_sprites_list.add(paddleB)
all_sprites_list.add(ball)

gameover = True  
while gameover == True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            gameover = False
    keys = pygame.key.get_pressed()
    if keys[pygame.K_k]:
        paddleB.moveup(5)
    if keys[pygame.K_m]:
        paddleB.movedown(5)
    
    
    
            
    all_sprites_list.update()
    # check if ball be bouncing against nonce walls
    if ball.rect.y <= 10:
        ball.velocity[1] = -ball.velocity[1]
    if ball.rect.y >= 490:
        ball.velocity[1] = -ball.velocity[1]
    #reset ball if point scored
    if ball.rect.x >= 700:
        playerA = playerA + 1
        ball.rect.x=345
        ball.rect.y=195
    if ball.rect.x <=10:
        playerB = playerB + 1
        ball.rect.x=345
        ball.rect.y=195
        
    #detect collision between ball and paddle
    if pygame.sprite.collide_mask(ball, paddleB) or pygame.sprite.collide_mask(ball, paddleA):
        ball.bounce()
        file = 'pong1.ogg'
        mixer.init()
        mixer.music.load(file)
        mixer.music.play()
    if player == 1:
        reactiontime = 100
        AIvelocity=5
    if player ==2:
        reactiontime = 200
        AIvelocity=7
    if player == 3:
        reactiontime = 300
        AIvelocity=10
        
    if ball.rect.x <= reactiontime:    
        if paddleA.rect.centery > ball.rect.y:
           paddleA.moveup(AIvelocity)
        if paddleA.rect.centery < ball.rect.y:
           paddleA.movedown(AIvelocity)
    
        
    
# fill screen
    screen.fill(BLACK)
    pygame.draw.line(screen, WHITE, [349, 0], [349, 500], 5)
    all_sprites_list.draw(screen)

    #display scores
    myfont = pygame.font.SysFont(None , 74)
    text = myfont.render(str(playerA), True , WHITE)
    screen.blit(text, (250, 10))
    
    myfont = pygame.font.SysFont(None , 74)
    text = myfont.render(str(playerB), True , WHITE)
    screen.blit(text, (420, 10))
    if playerB == 10 or playerA == 10:
        myfont = pygame.font.SysFont(None , 74)
        text = myfont.render("GAME OVER", True , WHITE)
        screen.blit(text, (300, 250))
        break
        
    pygame.display.flip()
    clock.tick(60)
pygame.quit()
    
    
    

