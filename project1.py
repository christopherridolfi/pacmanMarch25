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
flipstop = 0
screen = pygame.display.set_mode([800, 600])#makes my screen a 800,600 pixels.
pygame.display.set_caption('Pacman')#makes the window name Pacman
BLACK = (0, 0, 0)
RED = (255, 0, 0)#defining colour values.
BLUES = [(0,35,165),(0,35,168),(0,35,168),(0,31,150),(0,19,91),(0,32,154),(0,25,120),(0,29,141),(0,33,158),(0,31,150),(0,34,162),(0,21,102),(0,36,173),(0,20,96)]
#The BLUES variable contains multiple color values that are used to make sure the pacman sprite doesn't go through the colour.
x = 0
WIDTH = 770#This is the x value that I use for the screen loop effect when going right to left.
MIN = 10#this is the x value that I use for the screen loop effect when going left to right.
class Pacman(pygame.sprite.Sprite):#This is my first Class. IT is made for my pacman sprite.
    def __init__(self,x,y,pac):#inititates the class.
        #calls x,y
        super().__init__()

        # Set height, width
        self.image = pygame.image.load(pac)#loads the image of my sprite.
        self.image = pygame.transform.scale(self.image,(24,24))#transforms the size of the image.
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
allspriteslist.add(pacfood2)#adding my second food sprite to allsprites list.
allspriteslist.add(pacfood3)#repeated code but for a different variable.

play = Pacman(100, 94,"Packman.png")#making my pacman sprite using pacman class.
allspriteslist.add(play)#adding my pacman sprite to allsprites list.

ghostsp = Ghost(400,260,"Ghost.png")
allspriteslist.add(ghostsp)#repeated code.


player_rot_speed = 250#player speed.



pygame.mixer.music.load("music.mp3")#Loads an pm3
pygame.mixer.music.set_volume(0.5)#sets the volume level
pygame.mixer.music.play(-1)#plays the mp3 on an infinite loop.

move = (0,0)#values for moving
move2 = (0,0)#values for moving.


done = False#assigning done as False.


def checkForBlue(xchange, ychange, x_pos, y_pos):
    if xchange >= 0 and ychange >= 0:
        for i in range(0, xchange):
            color = bg.get_at((x_pos + i, y_pos))
            if color in BLUES:
                return True
        for i in range(0, ychange):
            color = bg.get_at((x_pos, y_pos + i))
            if color in BLUES:#checks if color variable matches with my RGB balues defined in that variable..
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
"""This function finds the color of the x and y values in front of the spirte and then it compares it with
the BLUE color value to see if you are touching a wall. This is done so the pacman sprite can't go through walls."""

curDirection = 0#setting curDirection to 0
footcounter = 0
while not done:
    move = (0, 0)  # values for moving

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()#stops code if you press QUIT
        if event.type == pygame.KEYDOWN:

            if event.key == pygame.K_LEFT:#If statement will be activated once you press left arrow.
                curDirection = "L"
                footcounter = 0#makes sure the sprite does not flip in a loop. It makes sure it only flips once.
            if event.key == pygame.K_RIGHT:#activates when the right arrow is pressed.
                curDirection = "R"
                footcounter = 0#repeated code.
            if event.key == pygame.K_UP:
                curDirection = "U"
            if event.key == pygame.K_DOWN:
                curDirection = "D"
            if event.key == pygame.K_w:#press w to move the ghost.
                move2 = (0, -10)
            if event.key == pygame.K_s:
                move2 = (0, 10)
            if event.key == pygame.K_a:
                move2 = (-10, 0)
            if event.key == pygame.K_d:
                move2 = (10, 0)


    if curDirection == "R":
        if not checkForBlue(10, 0, play.rect.x+25, play.rect.y+12):
            if footcounter == 0:
                if flipstop >= 1:
                    play.image = pygame.transform.flip(play.image, True, False)#flips the play sprite horizontaly.
                    footcounter += 1#adds 1 to footcounter variable so it doesn't flip continously.
                    flipstop +=1#adds 1 to flipstop variable to the sprite doesn flip right when you start moving.
            move = (10, 0)
    if curDirection == "L":
        if not checkForBlue(-10, 0, play.rect.x, play.rect.y + 12):
            move = (-10, 0)
            if footcounter == 0:
                play.image = pygame.transform.flip(play.image, True,False)  # make it run through once without flip.
                footcounter += 1#Adds 1 to footcounter variable.
                flipstop+=1#Adds 1 to flipstop variable

    elif curDirection == "U":
        if not checkForBlue(0, -10, play.rect.x+12, play.rect.y):
            move = (0, -10)
    elif curDirection == "D":
        if not checkForBlue(0, 10, play.rect.x+11, play.rect.y+24):
            move = (0, 10)

    if pygame.sprite.collide_rect(ghostsp,play) and food == 1:
        import youlosep2#imports youlosep2 python file.
        exec(open("youlosep2.py").read())#opens and reads the youlosep2 python file.
        os.system("python file.py")
    if pygame.sprite.collide_rect(ghostsp,play) and food !=1:#this peice of code is activated if the ghost sprite and pacman sprtie collide.
        import youlost#imports youlost python file.
        exec(open("youlost.py").read())#opens and reads the youlost python file.
        os.system('python file.py')#brings you to the file.

    """This peice of code brings you to the "lost" python file so it can run through its own code. I did this to keep
           the documents orginized."""

    if pygame.sprite.collide_rect(pacfood1,play) and food != 1:
        food = 1
        pygame.mixer.music.load("Home 14 (online-audio-converter.com).mp3")
        pygame.mixer.music.set_volume(0.5)
        pygame.mixer.music.play(0)
        pygame.sprite.Sprite.kill(pacfood1)
        allspriteslist.remove(pacfood1)
        wait = 1
        if wait == 1:
            pygame.mixer.music.load("music.mp3")
            pygame.mixer.music.play(-1)

    """This peice of code plays a sound effect when the play sprite and food sprite collide. This also
        makes the food variable 1 which is used so you can kill the ghost. This music plays through once and then
        replays the pacman song."""


    if pygame.sprite.collide_rect(pacfood2,play) and food != 1:#activates when pacfood2 touches play sprite.
        food = 1
        pygame.mixer.music.load("Home 14 (online-audio-converter.com).mp3")#This loads the sound effect.
        pygame.mixer.music.set_volume(0.5)#sets the volumee
        pygame.mixer.music.play(0)#Plays through the mp3 once.
        wait = 1
        allspriteslist.remove(pacfood2)
        if wait == 1:#I made this so the theme song does not cut of the mp3. As it was doing this during my testing.
            pygame.mixer.music.load("music.mp3")#redloads the music.mp3
            pygame.mixer.music.play(-1)#plays it in an infinite loop.


    if pygame.sprite.collide_rect(pacfood3,play) and food != 1:#repeated code
        food = 1
        pygame.mixer.music.load("Home 14 (online-audio-converter.com).mp3")
        pygame.mixer.music.set_volume(0.5)
        pygame.mixer.music.play(0)
        allspriteslist.remove(pacfood3)
        wait = 1
        if wait == 1:
            pygame.mixer.music.load("music.mp3")
            pygame.mixer.music.play(-1)

    play.rect = play.rect.move(move)#moves the play sprite.
    ghostsp.rect = ghostsp.rect.move(move2)#moves the ghost sprite.
    time.sleep(0.09)#creates the cool stagger effect that pacman is known for.

    """This is repeated code of when the pacman sprite collides with the food sprite. I am making three food and pacman
    collitions becasue I want there to be an even chance of winning."""

    if play.rect.x >= WIDTH:#if pacman sprite is going of screen it teleports you to the other side. I did this to be like original game.
        play.rect.x = 20#it brings the sprite to these x coordinates.
    if play.rect.x <= MIN:#Same as above but a
        play.rect.x = 750#it brings the sprite to these x coordinates.


    if ghostsp.rect.x >= WIDTH:#if pacman sprite is going of screen it teleports you to the other side.
        ghostsp.rect.x = 20#it brings the sprite to these x coordinates.
    if ghostsp.rect.x <= MIN:#Same as above but a
        ghostsp.rect.x = 750#it brings the sprite to these x coordinates.

    elif ghostsp.rect.y == 0:
        ghostsp.rect.y = 550

    elif ghostsp.rect.y == 570:
        ghostsp.rect.y =- 0

    screen.fill(BLACK)#This fills the screen with the colour black.
    screen.blit(bg, (0, 0))#This fills the screen with my backround photo at 0,0 coordinates.
    screen.blit(ghostsp.image, ghostsp.rect)#This makes the ghost sprite appear on screen..
    screen.blit(play.image, play.rect)
    allspriteslist.draw(screen)#This draws all the sprites in the allsprites list on the screen.
    pygame.display.flip()#updates the screen.