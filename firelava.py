#ismaeel bashir


#imoprts files
import pygame

#lava class

#creates a class for lava
class Lava(pygame.sprite.Sprite):

    #creates a constructor
    def __init__(self):

        #inherits pygame sprite attributes
        pygame.sprite.Sprite.__init__(self)

        #creates a surface for lava
        self.image = pygame.Surface([1400, 700])

        #gets the lava image
        self.lavaimg = pygame.image.load("assets/fire/lava.png")

        #blits lava image to surface
        self.image.blit(self.lavaimg, [0,0])

        #makes the colour black transparent
        self.image.set_colorkey((0,0,0))

        #gets the rect of the surface
        self.rect = self.image.get_rect()

        #defines the x pos
        self.rect.x = 0

        #defines the y pos
        self.rect.y = 700

        #defines the rise speed
        self.risespeed = 10

        #defines the timer
        self.time_elapsed = 0

        #defines var for recording time
        self.dt = 0

        #defines rise timer
        self.risetimer = 1

    #defines function to rise lava
    def rise(self):


        #gets time
        self.time_elapsed = pygame.time.get_ticks()

        #checks if 1 second has passed
        if self.time_elapsed > self.dt + (self.risetimer)*1000:

            #increments lava y pos by rise speed
            self.rect.y -= self.risespeed

            #records time
            self.dt = pygame.time.get_ticks()
