
import pygame, math

WHITE = (255, 255, 255)

class Rocket(pygame.sprite.Sprite):

    def __init__(self,picture,width,height,speed,angle,turnRate):

        super().__init__()

        
        self.image = picture
        self.mask = pygame.mask.from_surface(self.image)
        #resize image to width, height
        self.rect = self.image.get_rect()
        self.radius = 15
        pygame.image = (self.image, self.rect.center, self.radius)
        #self.image.set_colorkey(Rocket1)

        self.width = width
        self.height =height
        #self.color = color
        self.speed = speed
        self.original = picture
        self.angle = angle
        
        self.turnRate = turnRate

        speed == 10

        #pygame.draw.rect(self.image, WHITE, [0,0, self.width, self.height])

        #self.rect = self.image.get_rect()
    def rotRight(self):
        self.angle -= self.turnRate
        if self.speed == 0:
            self.speed = self.turnRate
        while self.angle < 0:
            self.angle += 360
        self.image = pygame.transform.rotate(self.original,self.angle)

    def rotLeft(self):
        self.angle += self.turnRate
        if self.speed == 0:
            self.speed = self.turnRate
        while self.angle < 0:
            self.angle -= 360
        self.image = pygame.transform.rotate(self.original,self.angle)

    def draw(self, screen):
        screen.blit(self.image, self.rect)
        

    def Thurst(self, pixels):
        self.rect.y -= math.cos(math.radians((self.angle)))*10
        self.rect.x -= math.sin(math.radians((self.angle)))*10
 
    def moveBackward(self, pixels):
        self.rect.y += math.cos(math.radians((self.angle)))*10
        self.rect.x += math.sin(math.radians((self.angle)))*10
 
    def changeSpeed(self, speed):
        self.speed = speed
 
    def repaint(self, color):
        print("repaint")
        #self.color = color
        #pygame.draw.rect(self.image, self.color, [0, 0, self.width, self.height])

