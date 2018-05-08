# Menu template with button class and basic menu navigation
# Adapted from http://www.dreamincode.net/forums/topic/401541-buttons-and-sliders-in-pygame/
from rocketclass import Rocket
import pygame, sys
pygame.init()

background = pygame.image.load("Supernova-Hunters-800x533.png")
RocketImage = pygame.image.load("rocket.png")
# Define some colours

BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
GREEN = (177, 227, 102)
BRIGHT_GREEN = (205, 237, 157)
RED = (234, 53, 70)
BRIGHT_RED = (241,126,137)
BRIGHT_Blue = (135,212,223)
Blue = (67,188,205)
Jibril = (88,88,79)


SCREENWIDTH = 800
SCREENHEIGHT = 500
size = (SCREENWIDTH, SCREENHEIGHT)
screen = pygame.display.set_mode(size)

ALL_sprites_lists = pygame.sprite.Group()
player = Rocket(RocketImage,30,40,5)
ALL_sprites_lists.add(player)

#pygame.mixer.pre_init(frequency=44100, size=-16, channels=2, buffer=4096)
#pygame.mixer.music.load()
#pygame.mixer.music.play(-1)


class Button():
    """This is a class for a generic button.
    
       txt = text on the button
       location = (x,y) coordinates of the button's centre
       action = name of function to run when button is pressed
       bg = background colour (default is white)
       fg = text colour (default is black)
       size = (width, height) of button
       font_name = name of font
       font_size = size of font
    """
    def __init__(self, txt, location, action, bg=WHITE, fg=BLACK, size=(100, 40), font_name="Segoe Print", font_size=16):
        self.color = bg  # the static (normal) color
        self.bg = bg  # actual background color, can change on mouseover
        self.fg = fg  # text color
        self.size = size

        self.font = pygame.font.SysFont(font_name, font_size)
        self.txt = txt
        self.txt_surf = self.font.render(self.txt, 1, self.fg)
        self.txt_rect = self.txt_surf.get_rect(center=[s//2 for s in self.size])

        self.surface = pygame.surface.Surface(size)
        self.rect = self.surface.get_rect(center=location)

        self.call_back_ = action

    def draw(self):
        self.mouseover()

        self.surface.fill(self.bg)
        self.surface.blit(self.txt_surf, self.txt_rect)
        screen.blit(self.surface, self.rect)

    def mouseover(self):
        """Checks if mouse is over button using rect collision"""
        self.bg = self.color
        pos = pygame.mouse.get_pos()
        if self.rect.collidepoint(pos):
            self.bg = BRIGHT_RED  # mouseover color

    def call_back(self):
        """Runs a function when clicked"""
        self.call_back_()
        
def my_shell_function():
    """A generic function that prints something in the shell"""
    print('Fire the nukes!')

def my_next_function():
    """A function that advances to the next level"""
    global level
    level += 1

def my_play():
    global level
    level += 2

def my_INSTRUCTIONS():
    global level
    level += 3
    
def my_previous_function():
    """A function that retreats to the previous level"""
    bg = RED
    global level
    if level == 3:
        level -=2
    elif level == 4:
        level -=3
    else:
        level -= 1

def my_quit_function():
    """A function that will quit the game and close the pygame window"""
    pygame.quit()
    sys.exit()

def mousebuttondown(level):
    """A function that checks which button was pressed"""
    pos = pygame.mouse.get_pos()
    if level == 1:
        for button in level1_buttons:
            if button.rect.collidepoint(pos):
                button.call_back()
    elif level == 2:
        for button in level2_buttons:
            if button.rect.collidepoint(pos):
                button.call_back()
    elif level == 3:
        for button in level3_buttons:
            if button.rect.collidepoint(pos):
                button.call_back()
    elif level == 4:
        for button in level3_buttons:
            if button.rect.collidepoint(pos):
                button.call_back()
                
def play_music():
    pygame.mixer.music.unpause()
def stop_music():
    pygame.mixer.music.pause()

level = 1
carryOn = True
clock = pygame.time.Clock()

#create button objects
fontTitle = pygame.font.Font('freesansbold.ttf', 50)
textSurfaceTitle = fontTitle.render('MQ Enterprise!', True, WHITE) 
textRectTitle = textSurfaceTitle.get_rect()
textRectTitle.center = (400,50)  



button_PLAY = Button("PLAY", (SCREENWIDTH/6, SCREENHEIGHT/4-50), my_play, bg=RED)
button_INSTRUCTIONS = Button("INSTRUCTIONS",(SCREENWIDTH/6, SCREENHEIGHT*2/4-50),my_INSTRUCTIONS, bg=RED)
button_SETTINGS = Button("SOUND", (SCREENWIDTH/6, SCREENHEIGHT*3/4-50),my_next_function, bg=GREEN)
button_QUIT = Button("QUIT", (SCREENWIDTH/6, SCREENHEIGHT*4/4-50), my_quit_function, bg=Blue)
button_ON = Button("ON", (SCREENWIDTH/5, SCREENHEIGHT/4), play_music,bg=GREEN)
button_OFF= Button("OFF", (SCREENWIDTH/5, SCREENHEIGHT*2/4),stop_music, bg=GREEN)
button_Previous2 = Button("Previous", (SCREENWIDTH/5, SCREENHEIGHT*3/4), my_previous_function,bg=RED)

#arrange button groups depending on level
level1_buttons = [button_PLAY,button_INSTRUCTIONS,button_SETTINGS, button_QUIT]
level2_buttons = [button_ON,button_OFF,button_Previous2]
level3_buttons = [button_Previous2]
level4_buttons = [button_Previous2]
#---------Main Program Loop----------


while carryOn:
    # --- Main event loop ---
    for event in pygame.event.get(): # Player did something
        if event.type == pygame.QUIT: # Player clicked close button
            carryOn = False
        elif event.type == pygame.MOUSEBUTTONDOWN: # Player clicked the mouse
            mousebuttondown(level)

    # --- Game logic goes here

    # --- Draw code goes here
    screen.fill(WHITE)
    screen.blit(background, (0, 0))
    screen.blit(RocketImage, (400,100))
    screen.blit(textSurfaceTitle,textRectTitle)
    

    # Clear the screen to white
    

    # Draw buttons
    if level == 1:
        for button in level1_buttons:
            button.draw()
    elif level == 2:
        for button in level2_buttons:
            button.draw()
    elif level == 3:
        screen.fill(WHITE)
        for button in level3_buttons:
            ALL_sprites_lists.draw(screen)
            button.draw()      
    elif level == 4:
        screen.fill(WHITE)
        for button in level4_buttons:
            button.draw()
            

    # Update the screen with queued shapes
    pygame.display.flip()

    # --- Limit to 60 frames per second
    clock.tick(60)

pygame.quit()

