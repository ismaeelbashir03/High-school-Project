#ismaeel bashir

#imports pygame and and other library
import pygame
import random
from superclass_boss import Boss



#creates the boss class
class fireBoss(Boss):

    #creates a constructor
    def __init__(self):

        #calls super class to inherit parent class attributes
        super().__init__()

        #creates a variable to store the boss img
        self.bossimg = pygame.image.load("assets/fire/bossimg.png")

        #blits the boss img to the pygame surface
        self.image.blit(self.bossimg, [0,0])




    #defines a function for the boss attack
    def attack(self, Fireball, fireballs, player, warnings, Warning_sign):

        ylist = [1, 161, 341, 521, 621]


        
        #gives a chance of 3 precent (per frame) for this happening
        if random.randrange(1,100) <= 3:

            #creates a random y coordinate
            random_y = random.choice(ylist)

            #creates an instance of warning
            warning = Warning_sign(random_y)

            #adds warning to group
            warnings.add(warning)

            #createa an instance of fireball class with random y
            fireball = Fireball(random_y)

            #adds the instance to a group
            fireballs.add(fireball)


            

        #returns values
        return fireballs, warnings



        

        
        

    
