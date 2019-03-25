import pygame
pygame.init()
screen = pygame.display.set_mode([800, 600])
BLACK = (0, 0, 0)
RED = (255, 0, 0)
x = 0
bg = pygame.image.load("images.png")
bg = pygame.transform.scale(bg, (800, 600))
class Pacman(pygame.sprite.Sprite):
    def __init__(self,x,y,pac):
        #calls x,y
        super().__init__()

        # Set height, width
        self.image = pygame.image.load(pac)
        self.image = pygame.transform.scale(self.image,(28,28))
        # Make our top-left corner the passed-in location.
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y

class Ghost(pygame.sprite.Sprite):
    def __init__(self,x,y,file):
        super().__init__()

        # Set height, width
        self.image = pygame.image.load(file)

        # Make our top-left corner the passed-in location.
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y


play = Pacman(100, 94, "Packman.png")
allspriteslist = pygame.sprite.Group()
allspriteslist.add(play)

while x == 0:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            x = True

    screen.fill(BLACK)
    screen.blit(bg,(0, 0))

    allspriteslist.draw(screen)
    pygame.display.flip()



#pygame.Surface.get_at(x,y)
#screen.get_at(x,y)