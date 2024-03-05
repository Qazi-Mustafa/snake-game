import pygame
import time
import random
import os
 
snake_speed = 15
scaling = 20

length_screen = 1280
height_screen = 720

black = pygame.Color(0, 0, 0)
white = pygame.Color(255, 255, 255)
red = pygame.Color(255, 0, 0)
green = pygame.Color(0, 100, 0)


pygame.init()
 
bg = pygame.image.load("background.png")
bg = pygame.transform.scale(bg,(length_screen, height_screen))
pygame.display.set_caption('Qazi snake game')
game_window = pygame.display.set_mode((length_screen, height_screen))


fps = pygame.time.Clock()
 

snake_placement = [400, 100]
 

snake_size = [[400, 100],
              [180, 100],
              [160, 100],
              [140, 100]
              ]
fruit_placement = [random.randrange(1, (length_screen//scaling)) * scaling,
                  random.randrange(1, (height_screen//scaling)) * scaling]
 
fruit_spawn = True
 
d = "R"
change_to = d
 
Score = 0
if os.path.exists("hscore.txt"):
    with open("hscore.txt","r")as file:
        high_score = int(file.read())
else:
    high_score = 0

def show_score(choice, color, font, size):
    score_font = pygame.font.SysFont(font, size)
    score_surface = score_font.render('Score : ' + str(Score), True, color)
    score_rect = score_surface.get_rect()
    game_window.blit(score_surface, score_rect)
 

def game_over():
    if Score > high_score:
        with open("hscore.txt") as file:
            file.write(str(high_score))
    my_font = pygame.font.SysFont('Calibri', 50)
    game_over_surface = my_font.render(
        'Your Score is : ' + str(Score), True, red)
    game_over_rect = game_over_surface.get_rect()
    game_over_rect.midtop = (length_screen/2, height_screen/4)
    game_window.blit(game_over_surface, game_over_rect)
    pygame.display.flip()
    time.sleep(2)
    pygame.quit()
    quit()
 
 

while True:
    for event in pygame.event.get():
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_UP or event.key ==pygame.K_w:
                change_to = "U"
            if event.key == pygame.K_DOWN or event.key ==pygame.K_s:
                change_to = "D"
            if event.key == pygame.K_LEFT or event.key ==pygame.K_a:
                change_to = "L"
            if event.key == pygame.K_RIGHT or event.key ==pygame.K_d:
                change_to = "R"
    if change_to == "U" and d != "D":
        d = "U"
    if change_to == "D" and d != "U":
        d = "D"
    if change_to == "L" and d != "R":
        d = "L"
    if change_to == "R" and d != "L":
        d = "R"
    if d == "U":
        snake_placement[1] = snake_placement[1] -  scaling
    if d == "D":
        snake_placement[1] = snake_placement[1] + scaling
    if d == "L":
        snake_placement[0] = snake_placement[0] - scaling
    if d == "R":
        snake_placement[0] = snake_placement[0] + scaling
 

    snake_size.insert(0, list(snake_placement))
    if snake_placement[0] == fruit_placement[0] and snake_placement[1] == fruit_placement[1]:
        Score = Score + 10
        snake_speed = snake_speed + 0.5
        fruit_spawn = False
    else:
        snake_size.pop()
         
    if not fruit_spawn:
        fruit_placement = [random.randrange(1, (length_screen//scaling)) * scaling,
                          random.randrange(1, (height_screen//scaling)) * scaling]
         
    fruit_spawn = True
    game_window.fill(white)
    game_window.blit(bg,(0,0))

    for i in snake_size:
        pygame.draw.rect(game_window, green,
                         pygame.Rect(i[0], i[1], scaling, scaling))
    pygame.draw.rect(game_window, red, pygame.Rect(
        fruit_placement[0], fruit_placement[1], scaling, scaling))
 

    if snake_placement[0] < 0 or snake_placement[0] > length_screen-10:
        game_over()
    if snake_placement[1] < 0 or snake_placement[1] > height_screen-10:
        game_over()
 

    for i in snake_size[1:]:
        if snake_placement[0] == i[0] and snake_placement[1] == i[1]:
            game_over()

    
    
    show_score(1, black, 'Calibri', 50)
    pygame.display.update()
    fps.tick(snake_speed)