from rocketclass import Rocket
from Worm import WormHole
from Asteroid import Asteroid1
import pygame, sys
from pygame.locals import *
 
pygame.init()

background = pygame.image.load("Supernova-Hunters-800x533.png")
Rocketbg = pygame.image.load("rocketbg.png")
RocketImage = pygame.transform.scale(Rocketbg,(41,62))
asteroid = pygame.image.load("asteroid-icon.png")
ast= pygame.transform.scale(asteroid, (50,50))
arrows = pygame.image.load("arrow-keys-clipart-8-buttons.png")
aa= pygame.transform.scale(arrows, (150,150))
starbg = pygame.image.load("stars-in-night-sky.png")
wormhole2 = pygame.image.load("wormhole.png")
wormhole1 = pygame.transform.scale(wormhole2,(70,70))
soundbg = pygame.image.load("Space-PNG-Clipart.png")
instrbg = pygame.image.load("space-png-1920.png")
    
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
GREEN = (177, 227, 102)
BRIGHT_GREEN = (205, 237, 157)
RED = (234, 53, 70)
BRIGHT_RED = (241,126,137)
BRIGHT_Blue = (135,212,223)
Blue = (67,188,205)



speed = 1
SCREENWIDTH = 800
SCREENHEIGHT = 500
size = (SCREENWIDTH, SCREENHEIGHT)
screen = pygame.display.set_mode(size)

ASTEROID_sprites_lists = pygame.sprite.Group()

Obs = Asteroid1(ast, 10, 10)
Obs1 = Asteroid1(ast, 10, 10)
Obs2 = Asteroid1(ast, 10, 10)
Obs3 = Asteroid1(ast, 10, 10)
Obs4 = Asteroid1(ast, 10, 10)
Obs5 = Asteroid1(ast, 10, 10)
Obs6 = Asteroid1(ast, 10, 10)
Obs7 = Asteroid1(ast, 10, 10)
Obs8 = Asteroid1(ast, 10, 10)
Obs9 = Asteroid1(ast, 10, 10)
Obs10 = Asteroid1(ast, 10, 10)
Obs11 = Asteroid1(ast, 10, 10)
Obs12 = Asteroid1(ast, 10, 10)
Obs13 = Asteroid1(ast, 10, 10)
Obs14 = Asteroid1(ast, 10, 10)
Obs15 = Asteroid1(ast, 10, 10)
Obs16 = Asteroid1(ast, 10, 10)
Obs17 = Asteroid1(ast, 10, 10)
Obs18 = Asteroid1(ast, 10, 10)
Obs19 = Asteroid1(ast, 10, 10)
Obs20 = Asteroid1(ast, 10, 10)
Obs21 = Asteroid1(ast, 10, 10)
Obs22 = Asteroid1(ast, 10, 10)
Obs23 = Asteroid1(ast, 10, 10)
Obs24 = Asteroid1(ast, 10, 10)
Obs25 = Asteroid1(ast, 10, 10)
Obs26 = Asteroid1(ast, 10, 10)
Obs27 = Asteroid1(ast, 10, 10)
Obs28 = Asteroid1(ast, 10, 10)
Obs29 = Asteroid1(ast, 10, 10)
Obs30 = Asteroid1(ast, 10, 10)
Obs31 = Asteroid1(ast, 10, 10)
Obs32 = Asteroid1(ast, 10, 10)
Obs33 = Asteroid1(ast, 10, 10)
Obs34 = Asteroid1(ast, 10, 10)
Obs35 = Asteroid1(ast, 10, 10)
Obs36 = Asteroid1(ast, 10, 10)
Obs37 = Asteroid1(ast, 10, 10)
Obs38 = Asteroid1(ast, 10, 10)
Obs39 = Asteroid1(ast, 10, 10)
Obs40 = Asteroid1(ast, 10, 10)
Obs41 = Asteroid1(ast, 10, 10)
Obs42 = Asteroid1(ast, 10, 10)
Obs43 = Asteroid1(ast, 10, 10)
Obs44 = Asteroid1(ast, 10, 10)
Obs45 = Asteroid1(ast, 10, 10)
Obs46 = Asteroid1(ast, 10, 10)

ASTEROID_sprites_lists.add(Obs,Obs1,Obs2,Obs3,Obs4,Obs5,Obs6,Obs7,Obs8,Obs9,Obs10,Obs11,Obs12,Obs13,Obs14,Obs15,Obs16,Obs17,Obs18,Obs19,Obs20,Obs21,Obs22,Obs23,Obs24,Obs25,Obs26,Obs27,Obs28,Obs29,Obs30,Obs31,Obs32,Obs33,Obs34,Obs35,Obs36,Obs37,Obs38,Obs39,Obs40,Obs41,Obs42,Obs43,Obs44,Obs45,Obs46)



ROCKET_sprites_lists = pygame.sprite.Group()
player = Rocket(RocketImage,1,1,5,0,5)
player.rect.x = 460
player.rect.y = 400
ROCKET_sprites_lists.add(player)

Worm_sprites_lists = pygame.sprite.Group()
Worm2 = WormHole(wormhole1,70,70)
Worm2.rect.x = 315
Worm2.rect.y = 135
Worm_sprites_lists.add(Worm2)
            
pygame.mixer.pre_init(frequency=44100, size=-16, channels=2, buffer=4096)
pygame.mixer.music.load("12. Marvin Gaye & Tammi Terrell - Ain't No Mountain High Enough.mp3")
pygame.mixer.music.play(-1)

effect = pygame.mixer.Sound('Rocket Thrusters-SoundBible.com-1432176431.wav')

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
        self.color = bg 
        self.bg = bg  
        self.fg = fg  
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
            self.bg = BRIGHT_RED

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
    stop_music()
    
def my_INSTRUCTIONS():
    global level
    level += 3

def my_next_level():
    global level
    if level == 3:
        level += 2
    else:
        level += 1
    
def my_previous_function():
    """A function that retreats to the previous level"""
    bg = RED
    global level
    if level == 3:
        level -=2
    elif level == 4:
        level -=3
        
    elif level == 5:
        level -=4
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
        for button in level4_buttons:
            if button.rect.collidepoint(pos):
                button.call_back()
    elif level == 5:
        for button in level5_buttons:
            if button.rect.collidepoint(pos):
                button.call_back()
                
def play_music():
    pygame.mixer.music.unpause()
def stop_music():
    pygame.mixer.music.pause()

level = 1
carryOn = True
clock = pygame.time.Clock()


fontTitle = pygame.font.Font('freesansbold.ttf', 50)
textSurfaceTitle = fontTitle.render('MQ Enterprise!', True, WHITE) 
textRectTitle = textSurfaceTitle.get_rect()
textRectTitle.center = (400,50)  



button_PLAY = Button("PLAY", (SCREENWIDTH/6, SCREENHEIGHT/4-50),my_play, bg=RED)
button_INSTRUCTIONS = Button("INSTRUCTIONS",(SCREENWIDTH/6, SCREENHEIGHT*2/4-50),my_INSTRUCTIONS, bg=RED, font_size = 12)
button_SETTINGS = Button("SOUND", (SCREENWIDTH/6, SCREENHEIGHT*3/4-50),my_next_function, bg=RED)
button_QUIT = Button("QUIT", (SCREENWIDTH/6, SCREENHEIGHT*4/4-50), my_quit_function, bg=RED)
button_ON = Button("ON", (SCREENWIDTH/5, SCREENHEIGHT/4), play_music,bg=RED)
button_OFF= Button("OFF", (SCREENWIDTH/5, SCREENHEIGHT*2/4),stop_music, bg=RED)
button_Previous2 = Button("Previous", (SCREENWIDTH/5, SCREENHEIGHT*3/4), my_previous_function,bg=RED)

#arrange button groups depending on level
level1_buttons = [button_PLAY,button_INSTRUCTIONS,button_SETTINGS, button_QUIT]
level2_buttons = [button_ON,button_OFF,button_Previous2]
level4_buttons = [button_Previous2]
#---------Main Program Loop----------

while carryOn:
    # --- Main event loop ---
    for event in pygame.event.get(): # Player did something
        if event.type == pygame.QUIT: # Player clicked close button
            carryOn = False
        elif event.type == pygame.MOUSEBUTTONDOWN: # Player clicked the mouse
            mousebuttondown(level)
            
    keys = pygame.key.get_pressed()
    if keys[pygame.K_LEFT]:
        player.rotLeft()
    if keys[pygame.K_RIGHT]:
        player.rotRight()
    if keys[pygame.K_UP]:
        effect.play()
        player.Thurst(2)
    if keys[pygame.K_DOWN]:
        player.moveBackward(1)
        
    if player.rect.x < 0 or player.rect.x > SCREENWIDTH and player.rect.y < 0 or player.rect.y > SCREENHEIGHT:
        player.rect.x = 460
        player.rect.y = 400
        player.speed = 0
    hits = pygame.sprite.spritecollide(player, ASTEROID_sprites_lists, False, pygame.sprite.collide_circle_ratio(0.95))
    Win = pygame.sprite.spritecollide(player, Worm_sprites_lists, False, pygame.sprite.collide_circle_ratio(0.95))
    if hits:
        level = 6
        print("you crashed")
        #carryOn = False
    elif Win:
        level == 1
        print("You Won!")
        carryOn = False

        my_next_level()
        
        player.reset()

        player.rect.x = 680
        player.rect.y = 450
        print("You won")
        carryOn = True
    
          
    # --- Game logic goes here
    player.update()

    # --- Draw code goes here
    screen.fill(WHITE)
    screen.fill(BLACK)
    screen.blit(starbg,(0,0))
    screen.blit(background, (0, 0))
    screen.blit(Rocketbg, (300,50))
    screen.blit(textSurfaceTitle,textRectTitle)

    # Draw buttons
    
    if level == 1: #main screen
        for button in level1_buttons:
            button.draw()
            
    elif level == 2: #settings
        screen.fill(WHITE)
        screen.blit(soundbg,(0,0))
        for button in level2_buttons:
            button.draw()
            
    elif level == 3: #game
        screen.blit(starbg,(0,0))
        ROCKET_sprites_lists.draw(screen)
        Obs.rect.x = 500
        Obs.rect.y = 380

        Obs1.rect.x =500
        Obs1.rect.y =300

        Obs2.rect.x =480
        Obs2.rect.y =260

        Obs3.rect.x =400
        Obs3.rect.y =300

        Obs4.rect.x =400
        Obs4.rect.y =380

        Obs5.rect.x =380
        Obs5.rect.y =270

        Obs6.rect.x =360
        Obs6.rect.y =230

        Obs7.rect.x =320
        Obs7.rect.y =200

        Obs8.rect.x =430
        Obs8.rect.y =200


        Obs9.rect.x =410
        Obs9.rect.y =170


        Obs10.rect.x =380
        Obs10.rect.y =140

        ASTEROID_sprites_lists.draw(screen)
        Worm_sprites_lists.draw(screen)
        
    elif level == 4: #instructions
        screen.blit(instrbg,(0,0))
        screen.blit(aa,(20,220))
        for button in level4_buttons:
            button.draw()
        font = pygame.font.Font('freesansbold.ttf', 30)
        text1 = font.render('INSTRUCTIONS',1,WHITE)
        screen.blit(text1,(300,20))
        
        font2 = pygame.font.Font('freesansbold.ttf', 20)
        text2 = font2.render('In this game the objective is to reach the wormhole',1,WHITE)
        screen.blit(text2,(20,100))
        
        text3 = font2.render('that is surrounded by orbiting meteorids. The player must follow',1,WHITE)
        screen.blit(text3,(20,130))

        text4 = font2.render('the designated path without touching the meteorids. If the players rocket',1,WHITE)
        screen.blit(text4,(20,160))

        text5 = font2.render('touches the path or the meteorids they will have to restart from the beginning',1,WHITE)
        screen.blit(text5,(20,190))

        text6 = font2.render('Top arrow key is thrust',1,WHITE)
        screen.blit(text6,(300,250))

        text7 = font2.render('Down arrow key moves rocket backwards',1,WHITE)
        screen.blit(text7,(300,275))

        text8 = font2.render('Right arrow key rotates rocket to the right',1,WHITE)
        screen.blit(text8,(300,300))

        text9 = font2.render('Left arrow key rotates the rocket to the left',1,WHITE)
        screen.blit(text9,(300,325))


    elif level == 5: #second level
        screen.blit(starbg,(0,0))
        ROCKET_sprites_lists.draw(screen)
        
        Obs.rect.x = 240
        Obs.rect.y = 210

        Obs1.rect.x = 50
        Obs1.rect.y = 200

        Obs2.rect.x =40
        Obs2.rect.y =245

        Obs3.rect.x =75
        Obs3.rect.y =175

        Obs4.rect.x = 110
        Obs4.rect.y = 150

        Obs5.rect.x =380
        Obs5.rect.y =180

        Obs6.rect.x =320
        Obs6.rect.y =200

        Obs7.rect.x =280
        Obs7.rect.y =200

        Obs8.rect.x =220
        Obs8.rect.y =180

        Obs9.rect.x = 725
        Obs9.rect.y = 410
        
        Obs10.rect.x =700
        Obs10.rect.y =375

        Obs11.rect.x =670
        Obs11.rect.y =340

        Obs12.rect.x = 740
        Obs12.rect.y = 450

        Obs13.rect.x = 580
        Obs13.rect.y = 460

        Obs14.rect.x = 540
        Obs14.rect.y = 430

        Obs15.rect.x = 500
        Obs15.rect.y = 405
        
        Obs16.rect.x = 460
        Obs16.rect.y = 375

        Obs17.rect.x = 420
        Obs17.rect.y = 350

        Obs18.rect.x = 380
        Obs18.rect.y = 325

        Obs19.rect.x = 340
        Obs19.rect.y = 300

        Obs20.rect.x = 300
        Obs20.rect.y = 285

        Obs21.rect.x = 260
        Obs21.rect.y = 300

        Obs22.rect.x = 220
        Obs22.rect.y = 340

        Obs23.rect.x = 180
        Obs23.rect.y = 375

        Obs24.rect.x = 140
        Obs24.rect.y = 380

        Obs25.rect.x = 100
        Obs25.rect.y = 360
        
        Obs26.rect.x = 60
        Obs26.rect.y = 340

        Obs27.rect.x = 20
        Obs27.rect.y = 315

        Obs28.rect.x = 20
        Obs28.rect.y = 285

        Obs29.rect.x = 425
        Obs29.rect.y = 200

        Obs30.rect.x = 460
        Obs30.rect.y = 225

        Obs31.rect.x = 500
        Obs31.rect.y = 250

        Obs32.rect.x = 540
        Obs32.rect.y = 275

        Obs33.rect.x = 580
        Obs33.rect.y = 300

        Obs34.rect.x = 620
        Obs34.rect.y = 325

        Obs35.rect.x = 200
        Obs35.rect.y = 235
        
        Obs36.rect.x = 350
        Obs36.rect.y = 200

        Obs37.rect.x = 160
        Obs37.rect.y = 245

        Obs38.rect.x = 160
        Obs38.rect.y = 130


        Obs39.rect.x = 200
        Obs39.rect.y = 115

        
        Obs40.rect.x = 230
        Obs40.rect.y = 100

        Obs41.rect.x = 270
        Obs41.rect.y = 100

        Obs42.rect.x = 310
        Obs42.rect.y = 90

        Obs43.rect.x = 350
        Obs43.rect.y = 100

        Obs44.rect.x = 385
        Obs44.rect.y = 115

        Obs45.rect.x = 380
        Obs45.rect.y = 140
        
        Obs46.rect.x = 430
        Obs46.rect.y = 250

        
        ASTEROID_sprites_lists.draw(screen)
        Worm_sprites_lists.draw(screen)

    elif level == 6:
        screen.fill(BLACK)
        font = pygame.font.Font('freesansbold.ttf', 50)
        text1 = font.render('GAME OVER',1,WHITE)
        screen.blit(text1,(250,200))
        
    # Update the screen with queued shapes
    pygame.display.flip()

    # --- Limit to 60 frames per second
    clock.tick(60)

pygame.quit()

