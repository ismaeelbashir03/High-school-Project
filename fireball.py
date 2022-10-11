#ismaeel bashir

#imports pygame
import pygame
from superclass_ball import Ball

#creates a class for the fireballs
class Fireball(Ball):

    #creates a constructor
    def __init__(self, y):

        #calls super function to inherit parent class attributes
        super().__init__(y)

        #creates a var for the fore ball image
        self.fireballimg = pygame.image.load("assets/fire/fireballimg.png").convert_alpha()

        #blits the image to the fire ball surface
        self.image.blit(self.fireballimg, [0,0])





         
        

