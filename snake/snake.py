import pygame
from random import randint 
displayheight = 600
displaywidth = 800

# define colors 
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
BLUE = (0, 0, 255)
GREEN = (0, 255, 0)
RED = (255, 0, 0)

#variables initialization
global collision
collision=0
#define class for snake 
class Snake:
    def __init__(self):
        self.x = 0
        self.y = 0
        self.change_x = 0
        self.change_y = 0
        self.color = WHITE
        self.width = 20
        self.height = 20
class Food:
    def __init__(self):
        self.x = 100
        self.y = 100
        self.width = 20
        self.height = 20
        self.color = GREEN
        
clock = pygame.time.Clock()
def makesnake():
    snake = Snake()
    return snake 
def main():
    collision_num = 0 
    global collision
    collision=0
    pygame.init()
    gamewindow = pygame.display.set_mode((displaywidth, displayheight))
    gameover = 1
    snake = makesnake()
    food = Food()
    snakelist = []

    while gameover == 1:
        gamewindow.fill(BLACK)
        pygame.draw.rect(gamewindow, food.color, (food.x, food.y, food.width, food.height))
        pygame.draw.rect(gamewindow, snake.color, (snake.x, snake.y, snake.width, snake.height))
#collision cheese 
       
                 
#moving the snake 
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                gameover = 0
            if event.type == pygame.KEYDOWN:
                
                if event.key == pygame.K_LEFT:
                    snake.change_x = -10
                    snake.change_y =0
                elif event.key == pygame.K_RIGHT:
                    snake.change_x = 10
                    snake.change_y =0
                elif event.key == pygame.K_UP:
                     snake.change_y = -10
                     snake.change_x =0
                elif event.key == pygame.K_DOWN:
                     snake.change_y = +10
                     snake.change_x =0
        snake.x += snake.change_x
        snake.y += snake.change_y
        snakehead = []
        snakehead.append(snake.x)
        snakehead.append(snake.y)
        snakelist.append(snakehead)
        if snake.x == food.x:
            if snake.y == food.y:
                collision = 1
            else:
                collision=0

        if collision==1:
            food.x = 20*randint(2,35)
            food.y = 20*randint(2,25)
            collision=0
            collision_num += 1
            
        if len(snakelist) > collision_num: 
            print ("true")
            del(snakelist[0])
            
        for i in snakelist:
            print (i)
            pygame.draw.rect(gamewindow, snake.color, [i[0], i[1], snake.width, snake.height])

        if snakelist ==[]:
            pygame.draw.rect(gamewindow, snake.color, [snake.x, snake.y, snake.width, snake.height])
            
        clock.tick(30)
        pygame.display.update()
main()
    

    
