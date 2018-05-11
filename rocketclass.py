import pygame

WHITE = (255, 255, 255)

class Rocket(pygame.sprite.Sprite):

    def __init__(self,picture,width,height,speed):

        super().__init__()

        self.image = picture
        #resize image to width, height
        self.rect = self.image.get_rect()
        #self.image.set_colorkey(Rocket1)

        self.width = width
        self.height =height
        #self.color = color
        self.speed = speed

        speed == 10

        #pygame.draw.rect(self.image, WHITE, [0,0, self.width, self.height])

        #self.rect = self.image.get_rect()

    def draw(self, screen):
        screen.blit(self.image, self.rect)
        
    def moveRight(self, pixels):
        self.rect.x += pixels

    def moveLeft (self, pixels):
        self.rect.x -= pixels

    def Thurst(self, pixels):
        self.rect.y -= pixels
 
    def moveBackward(self, pixels):
        self.rect.y += pixels
 
    def changeSpeed(self, speed):
        self.speed = speed
 
    def repaint(self, color):
        print("repaint")
        #self.color = color
        #pygame.draw.rect(self.image, self.color, [0, 0, self.width, self.height])

