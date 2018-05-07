import pygame
Rocket1 = ("rocket.png")
class Rocket(pygame.sprite.Sprite):

    def __init__(self,color,width,height,speed):

        super().__init__()

        self.image = pygame.Surface([width, height])
        self.image.fill(Rocket1)
        self.image.set_colorkey(Rocket1)

        self.width = width
        self.height =height
        self.color = color
        self.speed = speed

        pygame.draw.rect(self.image, self.color, [0,0, self.width, self.height])

        self.rect = self.image.get_rect()

    def moveRight(self, pixels):
        self.rect.x += pixels

    def moveLeft (self, pixels):
        self.rect.x -= pixels

    def moveForward(self, speed):
        self.rect.y -= self.speed * speed / 20
 
    def moveBackward(self, speed):
        self.rect.y += self.speed * speed / 20
 
    def changeSpeed(self, speed):
        self.speed = speed
 
    def repaint(self, color):
        self.color = color
        pygame.draw.rect(self.image, self.color, [0, 0, self.width, self.height])

