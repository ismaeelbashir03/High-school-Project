#ismaeel bashir

#imports pygame and other modules
import pygame
import random

#creates a class for the fireballs
class Fireball(pygame.sprite.Sprite):

    #creates a constructor
    def __init__(self, x):

        #inherits the pygame sprite features
        pygame.sprite.Sprite.__init__(self)

        #height of fireball defined
        self.height = 100

        #width of fireball defined
        self.width = 100

        #creates a var holding the pygame surface
        self.image = pygame.Surface([self.width, self.height])

        #makes the colour black transparent
        self.image.set_colorkey((255,255,255))
        
        #creates a rectangular area for the class
        self.rect = self.image.get_rect()

        #defines the x pos
        self.rect.x = x

        #defines the y pos
        self.rect.y = 0

        #defines a raduis for collission
        self.radius = (self.width/2) * 0.3

        #creates a var for the fore ball image
        self.fireballimg = pygame.image.load("assets/corrupt/corruptballimg.png").convert_alpha()

        #blits the image to the fire ball surface
        self.image.blit(self.fireballimg, [0,0])

        #defines a velocity for the fireballs
        self.vel = 20

        


#defines a function which moves the fireballs
def move(fireballs, screen):

    #goes through each fireball in group
    for fireball in fireballs:


        #moves the x pos of the fireball
        fireball.rect.y += fireball.vel


#defines a function to see if fireball hits the end of screen
def kill(fireballs):

    #goes through each fireball
    for fireball in fireballs:

        #checks if fireball has reached the end of the screen
        if fireball.rect.y >= 700:

            #removes the fireball from the group
            fireballs.remove(fireball)

            
        

        
