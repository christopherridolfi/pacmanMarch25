import pygame,sys
import os
import time
pygame.init()
segment_width = 15
segment_height = 15
# Margin between each segment
segment_margin = 3
constant = 0
t=0
pygame.mixer.music.load("music.mp3")
pygame.mixer.music.set_volume(0.5)
pygame.mixer.music.play(-1)
while t == 0:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()
    screen = pygame.display.set_mode([800, 600])
    pygame.display.set_caption('Pacman')
    BLACK = (0, 0, 0)
    RED = (255, 0, 0)
    x = 0
    choiceman = pygame.image.load("chooserpac.png")
    rect1 = choiceman.get_rect()
    menu = pygame.transform.scale(choiceman, (800, 600))

    screen.fill(BLACK)
    screen.blit(menu, (0, 0))
    pygame.display.flip()

    done = False
    move = (0, 0)
    while not done:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit()
            if event.type == pygame.MOUSEBUTTONUP:
                import project1

                execfile(project1)
                os.system('python file.py')






