#ismaeel bashir


#imports files
import pygame
import random

#particle effect

#creates a class for particles
class Particle():
     #creates a constructor
    def __init__(self, x, y):

        #defines the x pos as passed in value
        self.x = x

        #defines th y pos as passed in value
        self.y = y

        #sets lifetime to initally 0
        self.lifetime = 0

        #sets the x vel as a random range
        self.xvel = random.randrange(-3, 3)*5

        #sets the y vel as random range
        self.yvel = random.randrange(-10, 10)*5


    #defines a function to draw particles
    def draw(self, screen, particles):

        #increments life time
        self.lifetime += 1

        #checks if lifetime is below 20 (only appears for 20 seconds)
        if self.lifetime < 20:

            #increments x by x vel
            self.x += self.xvel

            #increments y by y vel
            self.y += self.yvel

            #draws a circle at x and y pos
            pygame.draw.circle(screen, (255,255,0), (self.x,self.y), 2)

        #checks if 20 seconds has passed
        else:

            #removes particle from group
            particles.remove(self)





