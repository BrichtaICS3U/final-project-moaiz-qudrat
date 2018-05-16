import pygame
WHITE = (255, 255, 255)
 
class Asteroid1(pygame.sprite.Sprite):
    #This class represents a car. It derives from the "Sprite" class in Pygame.
 
    def __init__(self, picture, width, height):
        # Call the parent class (Sprite) constructor
        super().__init__()
 
        # Pass in the color of the car, and its x and y position, width and height.
        # Set the background color and set it to be transparent
        self.image = picture
        self.rect = self.image.get_rect()
        #self.image.fill(WHIT)
        self.image.set_colorkey(WHITE)
 
        #Initialise attributes of the car.
        self.width=width
        self.height=height

    def draw(self, screen):
        screen.blit(self.image,self.rect)
    
 
        # Draw the car (a rectangle!)

 
        # Instead we could load a proper picture of a car...
        # self.image = pygame.image.load("car.png").convert_alpha()
 
        # Fetch the rectangle object that has the dimensions of the image.
        
 
    
 
    
