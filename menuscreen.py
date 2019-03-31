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
    menu = pygame.image.load("menu.jpg")
    rect1 = menu.get_rect()
    menu = pygame.transform.scale(menu, (800, 600))
    class Menu(pygame.sprite.Sprite):
        def __init__(self,x,y,button):
            super().__init__()
            self.image = pygame.image.load(button)
            self.image = pygame.transform.scale(self.image,(300,300))
            self.rect = self.image.get_rect()
            self.rect.x = x
            self.rect.y = y

    go = Menu(250,200,"button13.png")
    allspriteslist = pygame.sprite.Group()
    allspriteslist.add(go)

    screen.fill(BLACK)
    screen.blit(menu, (0, 0))
    allspriteslist.draw(screen)
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








#pygame.Surface.get_at(x,y)
#screen.get_at(x,y)
#touching sprite pygame.sprite.collide