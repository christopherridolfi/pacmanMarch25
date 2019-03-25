import pygame
pygame.init()
screen = pygame.display.set_mode([800, 600])
BLACK = (0, 0, 0)
RED = (255, 0, 0)
x = 0
bg = pygame.image.load("images.png")
bg = pygame.transform.scale(bg, (800, 600))

while x == 0:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            x = True

    screen.fill(BLACK)
    screen.blit(bg,(0, 0))
    pygame.display.flip()