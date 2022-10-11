#ismaeel bashir

#imports pygame
import pygame

#creates a class for the fireballs
class Ball(pygame.sprite.Sprite):

    #creates a constructor
    def __init__(self, y):

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
        self.rect.x = 1500

        #defines the y pos
        self.rect.y = y

        #defines a raduis for collission
        self.radius = (self.width/2) * 0.3

        #defines a velocity for the fireballs
        self.vel = 20


    #defines a function to see if fireball hits the end of screen
    def kill(self, fireballs):

        #checks if fireball has reached the end of the screen
        if self.rect.x <= 0:

            #removes the fireball from the group
            fireballs.remove(self)


    #defines a function which moves the fireballs
    def move(self):

        #moves the x pos of the fireball
        self.rect.x -= self.vel
            
        

        
