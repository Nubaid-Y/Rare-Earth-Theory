import pygame
import math

class Button():
    def __init__(self,x,y,image, scale):
        width = image.get_width()
        height = image.get_height()
        self.image = pygame.transform.scale(image,(int(width*scale),int(height*scale)))
        self.rect = self.image.get_rect()
        self.rect.center = (x,y)
        self.clicked = False

    def draw(self,surface):
        action = False
        
        pos = pygame.mouse.get_pos()
        
        if self.rect.collidepoint(pos):
            if pygame.mouse.get_pressed()[0] == 1 and self.clicked == False:
                self.clicked = True
                action = True
                
        if pygame.mouse.get_pressed()[0] == 0:
            self.clicked = False

        surface.blit(self.image, (self.rect.x, self.rect.y))

        return action
    
    def movement(self, y):
        if self.rect.y < y:
            self.rect.y += 3

    def orbit(self,xcenter,ycenter,speed):
        x = self.rect.x
        y = self.rect.y

        x1 = x - xcenter
        y1 = y - ycenter

        radius = math.sqrt(x1**2+y1**2)
        angle = math.atan2(y1,x1)

        angle += speed

        self.rect.x = xcenter + radius * math.cos(angle)
        self.rect.y = ycenter + radius * math.sin(angle)