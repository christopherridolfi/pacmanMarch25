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
BLUES = [(0,35,165), (0,32,154),(0,19,91),(0,25,120),(0,33,158),(0,31,150),(0,34,162),(0,21,102),(0,36,173)]
x = 0
WIDTH = 800#This is the Width of the window. This variable will be used later.
MIN = 0
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
"""I made this a class becasue I wanted to make multiple food icons and the class made it easier. I ended up making
three and it looks very good."""

allspriteslist = pygame.sprite.Group()#A list in where all my sprites will be added.
#if button is pressed then game starts
bg = pygame.image.load("images copy.png")#This is loading a background image.
rect = bg.get_rect()
bg = pygame.transform.scale(bg, (800, 600))#Making by background image 800,600

pacfood1 = Food(500,20,"cheeseburger.png")#creating my first food sprite using Food class.
pacfood2 = Food(450,384,"cheeseburger.png")#creating my second food sprite using Food class.
pacfood3 = Food(177,500,"cheeseburger.png")
allspriteslist.add(pacfood1)#adding my food sprite to allsprite list.

play = Pacman(100, 94,"Packman.png")#making my pacman sprite using pacman class.
allspriteslist.add(play)#adding my pacman sprite to allsprites list.

ghostsp = Ghost(400,260,"Ghost.png")
allspriteslist.add(ghostsp)#repeated code.


player_rot_speed = 250



pygame.mixer.music.load("music.mp3")#Loads an pm3
pygame.mixer.music.set_volume(0.5)#sets the volume level
pygame.mixer.music.play(-1)#plays the mp3 on an infinite loop.

move = (0,0)#values for moving
move2 = (0,0)#values for moving.
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

done = False#assigning done as False.


def checkForBlue(xchange, ychange, x_pos, y_pos):
    if xchange >= 0 and ychange >= 0:
        for i in range(0, xchange):
            color = bg.get_at((x_pos + i, y_pos))
            if color in BLUES:
                return True
        for i in range(0, ychange):
            color = bg.get_at((x_pos, y_pos + i))
            if color in BLUES:#checks if color variable matches with preset color Blue.
                return True
    if xchange <= 0 and ychange <= 0:
        for i in range(0, xchange, -1):
            color = bg.get_at((x_pos + i, y_pos))
            if color in BLUES:
                return True
        for i in range(0, ychange, -1):
            color = bg.get_at((x_pos, y_pos + i))
            if color in BLUES:#checks if color variable matches with preset color Blue.
                return True
    return False
"""This function finds the color of the x values in front of it and compares it with
the BLUE color value to see if you are touching a wall."""

curDirection = 0#setting curDirection to 0
while not done:
    move = (0, 0)  # values for moving

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()#stops code if you press QUIT
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_LEFT:#If statement will be activated once u press left arrow.
                curDirection = "L"

            if event.key == pygame.K_RIGHT:#activates when the right arrow is pressed.
                curDirection = "R"
                pygame.sprite.rotate(play,90)
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
        if not checkForBlue(-10, 0, play.rect.x, play.rect.y+12):
            move = (-10, 0)
    elif curDirection == "R":
        if not checkForBlue(10, 0, play.rect.x+25, play.rect.y+12):
            move = (10, 0)
    elif curDirection == "U":
        if not checkForBlue(0, -10, play.rect.x+12, play.rect.y):
            move = (0, -10)
    elif curDirection == "D":
        if not checkForBlue(0, 10, play.rect.x+12, play.rect.y+25):
            move = (0, 10)

    if pygame.sprite.collide_rect(ghostsp,play) and food == 1:
        import youlosep2#imports youlosep2 python file.
        execfile(youlosep2)#opens and reads the youlosep2 python file.
    """This peice of code is used so when the player has picked up a burger and touches a goast the pacman player wins.
    once you win the youlosep2 python file is imported and you can restart."""
    if pygame.sprite.collide_rect(ghostsp,play) and food !=1:#this peice of code is activated if the ghost sprite and pacman sprtie collide.
        import youlost
        execfile(youlost)
        os.system('youlost.py')


    if pygame.sprite.collide_rect(pacfood1,play) and food != 1:
        food = 1
        pygame.mixer.music.load("Home 14 (online-audio-converter.com).mp3")
        pygame.mixer.music.set_volume(0.5)
        pygame.mixer.music.play(0)
        wait = 1
        if wait == 1:
            pygame.mixer.music.load("music.mp3")
            pygame.mixer.music.play(-1)
    """This peice of code plays a sound effect when the play sprite and food sprite collide. This also
        makes the food variable 1 which is used so you can kill the ghost. This music plays through once and then
        replays the pacman song."""

    if pygame.sprite.collide_rect(ghostsp,play) and food !=1:
        import youlost
        execfile(youlost)
        os.system('youlost.py')
        """This peice of code brings you to the lost python file so it can run through its own code. I did this to keep
        the documents orginized."""

    if pygame.sprite.collide_rect(pacfood2,play) and food != 1:
        food = 1
        pygame.mixer.music.load("Home 14 (online-audio-converter.com).mp3")
        pygame.mixer.music.set_volume(0.5)
        pygame.mixer.music.play(0)
        wait = 1
        if wait == 1:
            pygame.mixer.music.load("music.mp3")
            pygame.mixer.music.play(-1)
    """This peice of code plays a sound effect when the play sprite and food sprite collide. This also
    makes the food variable 1 which is used so you can kill the ghost. This music plays through once and then
    replays the pacman song."""

    if pygame.sprite.collide_rect(pacfood3,play) and food != 1:
        food = 1
        pygame.mixer.music.load("Home 14 (online-audio-converter.com).mp3")
        pygame.mixer.music.set_volume(0.5)
        pygame.mixer.music.play(0)
        allspriteslist.remove(pacfood3)
        wait = 1
        if wait == 1:
            pygame.mixer.music.load("music.mp3")
            pygame.mixer.music.play(-1)

    play.rect = play.rect.move(move)
    ghostsp.rect = ghostsp.rect.move(move2)
    time.sleep(0.09)

    """This is repeated code of when the pacman sprite collides with the food sprite. I am making three food and pacman
    collitions becasue I want there to be an even chance of winning."""

    if play.rect.x >= WIDTH:
        play.rect.x = 0
    if play.rect.x <= MIN:
        play.rect.x = 800
        """This peice of code puts the play sprite at the opposite end of the map when it leaves the map.
        It is like a loop. I did this so it would resemble the real pacman game. I did this going left to right
        and right to left."""

    screen.fill(BLACK)#This fills the screen with the colour black.
    screen.blit(bg, (0, 0))#This fills the screen with my backround photo at 0,0 coordinates.
    screen.blit(ghostsp.image, ghostsp.rect)#This draws the ghost sprite.
    screen.blit(pacfood1.image, pacfood1.rect)#This draws the pacman food
    screen.blit(pacfood2.image, pacfood2.rect)#repeated code.
    screen.blit(pacfood2.image, pacfood2.rect)
    screen.blit(pacfood3.image,pacfood3.rect)
    screen.blit(play.image, play.rect)
    allspriteslist.draw(screen)#This draws all the sprites.
    pygame.display.flip()#updates the screen.

#(rgb value)
   # continue moving
#else:
    #bounce back a little bit






#pygame.Surface.get_at(x,y)
#screen.get_at(x,y)
#touching sprite pygame.sprite.collide