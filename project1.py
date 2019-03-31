import pygame,sys#This imports pygame and sys which I will use later in my code.
import time
import os
pygame.init()#This initiates Pygame.
segment_width = 15#Makes my segment width 15 pixels.
segment_height = 15#makes my segement height 15 pixels
# Margin between each segment
segment_margin = 3
constant = 0
food = 0#A variable Used later in my code.
timeplay = 0#A variable Used later in my

screen = pygame.display.set_mode([800, 600])#makes my screen a 800,600 pixels.
pygame.display.set_caption('Pacman')#makes the window name Pacman
BLACK = (0, 0, 0)
RED = (255, 0, 0)#defining colour values.
BLUE = (0,35,165)
x = 0

class Pacman(pygame.sprite.Sprite):#This is my first Class. IT is made for my pacman sprite.
    def __init__(self,x,y,pac):#inititates the class.
        #calls x,y
        super().__init__()

        # Set height, width
        self.image = pygame.image.load(pac)#loads the image of my sprite.
        self.image = pygame.transform.scale(self.image,(25,25))#transforms the size of the image.
        # Make our top-left corner the passed-in location.
        self.rect = self.image.get_rect()#allows me to manipulate my sprite.
        self.rect.x = x#x values.
        self.rect.y = y#y values.
        self.rot = 0

class Ghost(pygame.sprite.Sprite):#This is my second sprite which is the ghost.
    def __init__(self,x,y,file):
        super().__init__()

        # Set height, width
        self.image = pygame.image.load(file)
        self.image = pygame.transform.scale(self.image, (28, 28))

        # Make our top-left corner the passed-in location.
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y


class Food(pygame.sprite.Sprite):#This is a food sprite that will be eaten by pacman sprite.
    def __init__(self,x,y,button):
        super().__init__()
        self.image = pygame.image.load(button)
        self.image = pygame.transform.scale(self.image,(20,20))
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y #repeated code.

allspriteslist = pygame.sprite.Group()#A list in where all my sprites will be added.
#if button is pressed then game starts
bg = pygame.image.load("images copy.png")#This is loading a background image.
rect = bg.get_rect()
bg = pygame.transform.scale(bg, (800, 600))#Making by background image 800,600

pacfood1 = Food(500,20,"cheeseburger.png")#creating my first food sprite using Food class.
pacfood2 = Food(450,384,"cheeseburger.png")#creating my second food sprite using Food class.

allspriteslist.add(pacfood1)#adding my food sprite to allsprite list.

play = Pacman(100, 94,"Packman.png")#making my pacman sprite using pacman class.
allspriteslist.add(play)#adding my pacman sprite to allsprites list.

ghostsp = Ghost(400,260,"Ghost.png")
allspriteslist.add(ghostsp)#repeated code.


player_rot_speed = 250



pygame.mixer.music.load("music.mp3")
pygame.mixer.music.set_volume(0.5)
pygame.mixer.music.play(-1)

move = (0,0)
move2 = (0,0)
"""
done = False

while not done:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_LEFT:
                move = (-10, 0)
            if event.key == pygame.K_RIGHT:
                move = (10, 0)
            if event.key == pygame.K_UP:
                move = (0,-10)
            if event.key == pygame.K_DOWN:
                move = (0, 10)
            if event.key == pygame.K_w:
                move2 = (0,-10)
            if event.key == pygame.K_s:
                move2 = (0,10)
            if event.key == pygame.K_a:
                move2 = (-10,0)
            if event.key == pygame.K_d:
                move2 = (10,0)

    play.rect = play.rect.move(move)
    ghostsp.rect = ghostsp.rect.move(move2)
    time.sleep(0.09)"""

done = False


def checkForBlue(xchange, ychange, x_pos, y_pos):
    for i in range(0, xchange):
        color = bg.get_at((x_pos + i, y_pos))
        if color == BLUE:
            return True
    for i in range(0, ychange):
        color = bg.get_at((x_pos, y_pos + i))
        if color == BLUE:
            return True
    return False


curDirection = 0
while not done:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_LEFT:
                curDirection = "L"
            if event.key == pygame.K_RIGHT:
                curDirection = "R"
            if event.key == pygame.K_UP:
                curDirection = "U"
            if event.key == pygame.K_DOWN:
                curDirection = "D"
            if event.key == pygame.K_w:
                move2 = (0, -10)
            if event.key == pygame.K_s:
                move2 = (0, 10)
            if event.key == pygame.K_a:
                move2 = (-10, 0)
            if event.key == pygame.K_d:
                move2 = (10, 0)
    if curDirection == "L":
        if not checkForBlue(-10, 0, play.rect.x, play.rect.y):
            move = (-10, 0)
    elif curDirection == "R":
        if not checkForBlue(10, 0, play.rect.x, play.rect.y):
            move = (10, 0)
    elif curDirection == "U":
        if not checkForBlue(0, -10, play.rect.x, play.rect.y):
            move = (0, -10)
    elif curDirection == "D":
        if not checkForBlue(0, 10, play.rect.x, play.rect.y):
            move = (0, 10)
    if pygame.sprite.collide_rect(ghostsp,play) and food ==1:
        import youlosep2
        execfile(youlosep2)
    if pygame.sprite.collide_rect(ghostsp,play) and food !=1:
        import youlost
        execfile(youlost)
        os.system('youlost.py')
    if pygame.sprite.collide_rect(pacfood1,play):
        food = 1
        pygame.mixer.music.load("Home 14 (online-audio-converter.com).mp3")
        pygame.mixer.music.set_volume(0.5)
        pygame.mixer.music.play(0)
        wait = 1
        if wait == 1:
            pygame.mixer.music.load("music.mp3")
            pygame.mixer.music.play(-1)

    if pygame.sprite.collide_rect(ghostsp,play) and food !=1:
        import youlost
        execfile(youlost)
        os.system('youlost.py')

    if pygame.sprite.collide_rect(pacfood2,play):
        food = 1
        pygame.mixer.music.load("Home 14 (online-audio-converter.com).mp3")
        pygame.mixer.music.set_volume(0.5)
        pygame.mixer.music.play(0)
        wait = 1
        if wait == 1:
            pygame.mixer.music.load("music.mp3")
            pygame.mixer.music.play(-1)

    play.rect = play.rect.move(move)
    ghostsp.rect = ghostsp.rect.move(move2)
    time.sleep(0.09)

    screen.fill(BLACK)
    screen.blit(bg, (0, 0))
    screen.blit(ghostsp.image, ghostsp.rect)
    screen.blit(pacfood1.image, pacfood1.rect)
    screen.blit(pacfood2.image, pacfood2.rect)
    screen.blit(pacfood2.image, pacfood2.rect)
    screen.blit(play.image, play.rect)
    allspriteslist.draw(screen)
    pygame.display.flip()

#(rgb value)
   # continue moving
#else:
    #bounce back a little bit






#pygame.Surface.get_at(x,y)
#screen.get_at(x,y)
#touching sprite pygame.sprite.collide