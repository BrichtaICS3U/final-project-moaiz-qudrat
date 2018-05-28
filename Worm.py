import pygame
WHITE = (255, 255, 255)
 
class WormHole(pygame.sprite.Sprite):
    #This class represents a car. It derives from the "Sprite" class in Pygame.
 
    def __init__(self, picture, width, height):
        # Call the parent class (Sprite) constructor
        super().__init__()
 
        # Pass in the color of the car, and its x and y position, width and height.
        # Set the background color and set it to be transparent
        
        self.width=width
        self.height=height

        self.image = picture
        self.rect = self.image.get_rect()
        self.radius = 15
        pygame.image = (self.image, self.rect.center, self.radius)
         
        
        #self.image.fill(WHIT)
        self.image.set_colorkey(WHITE)
 
        #Initialise attributes of the car.
       

    def draw(self, screen):
        screen.blit(self.image,self.rect)
    
 
