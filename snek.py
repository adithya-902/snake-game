
import random
import sys
import pygame

from pygame.locals import*

pygame.init()

clock = pygame.time.Clock()



win_size = [500, 500]

pygame.display.set_caption("Snek")
window = pygame.display.set_mode((win_size[0],win_size[1]))

block_size = 10


#colours
black = pygame.Color(0,0,0)
white = pygame.Color(255,255,255)
red = pygame.Color(255,0,0)
green = pygame.Color(0,255,0)
blue = pygame.Color(0,0,255)

def vars():
    global head_pos, snake_bod, direction, food_pos, food_spawn, score, fps
    direction = "RIGHT"
    head_pos = [200,200]
    snake_bod = [[200,200]]
    food_pos = [random.randrange(1, (win_size[0] // block_size )) * block_size, random.randrange(1, (win_size[1] // block_size ))* block_size]
    food_spawn = True
    score = 0
    fps = 60
    
def show_score(choice, color, font, size):
    score_font = pygame.font.SysFont(font, size)
    score_surface = score_font.render("Score: " + str(score), True, color)
    score_rect = score_surface.get_rect()

    if choice == 1:
        score_rect.midtop = (win_size[0]/10, 15)
    else:
        score_rect.midtop = (win_size[0]/2, win_size[1]/2)

    window.blit(score_surface, score_rect)

vars()
#game loop

while True:
    for event in pygame.event.get():
        if event.type == QUIT:
            pygame.quit()
            sys.exit()

        if event.type == KEYDOWN:
            if event.key == K_UP and direction != "DOWN":
                direction = "UP"
            if event.key == K_LEFT  and direction != "RIGHT":
                direction = "LEFT"
            if event.key == K_DOWN  and direction != "UP":
                direction = "DOWN"
            if event.key == K_RIGHT  and direction != "LEFT":
                direction = "RIGHT"

    if direction == "RIGHT":
        head_pos[0] += block_size
    if direction == "LEFT":
        head_pos[0] -= block_size
    if direction == "UP":
        head_pos[1] -= block_size
    if direction == "DOWN":
        head_pos[1] += block_size

    if head_pos[0] < 0:
        head_pos[0] = win_size[0] - block_size
    if head_pos[0] > win_size[0] - block_size:
        head_pos[0] = 0
    if head_pos[1] < 0:
        head_pos[1] = win_size[1] - block_size
    if head_pos[1] > win_size[1] - block_size:
        head_pos[1] = 0

    snake_bod.insert(0,list(head_pos))
    if head_pos[0] == food_pos[0] and head_pos[1] == food_pos[1]:
        score +=1
        food_spawn = False
        fps += 100
    else:
        snake_bod.pop()


    if  not food_spawn:
        food_pos = [random.randrange(1, (win_size[0] // block_size )) * block_size, random.randrange(1, (win_size[1] // block_size ))* block_size]
        food_spawn = True

    #game window
    window.fill(black)
    for pos in snake_bod:
        pygame.draw.rect(window, green, Rect(pos[0] , pos[1] ,block_size , block_size ))

    pygame.draw.rect(window, red, Rect(food_pos[0], food_pos[1], block_size, block_size))

    for block in snake_bod[1:]:
        if head_pos[0] == block[0] and head_pos[1] == block[1]:
            vars()

    show_score(1,white, 'Comic Sans MS', 25) 
    pygame.display.update()
    clock.tick(fps)


