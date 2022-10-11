#ismaeel bashir

#imports pygame and and other library
import pygame
import random
from superclass_boss import Boss


#creates the boss class
class waterBoss(Boss):

    #creates a constructor
    def __init__(self):

        #calls the super function to inherit parent class attributes
        super().__init__()

        #sets teh x pos of the boss
        self.rect.x = 1100

        #creates a variable to store the boss img
        self.bossimg = pygame.image.load("assets/water/bossimg.png")

        #blits the boss img to the pygame surface
        self.image.blit(self.bossimg, [0,0])





    #defines a function for the boss attack
    def attack(self, Fireball, fireballs, player, warnings, Warning_sign):

        ylist = [1, 161, 341, 521, 621]

        #checks if swimming is on
        if player.swimming == False:
        
            #gives a chance of 3 precent (per frame) for this happening
            if random.randrange(1,100) <= 5:

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

        else:

            #gives a chance of 3 precent (per frame) for this happening
            if random.randrange(1,100) <= 7:

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



    #defines block state function        
    def waterstate(self, water, player):


        #checks if boss health is below 75 percent
        if (self.max_health)*25/100 < self.target_health < (self.max_health)*75/100:

            #checks if block is 'raised' and its the first time being lowered
            if water.water_state == "lowered" and water.first_time == True:

                #calls the function to lower the block
                water.rise(player)

            #checks if it isnt the first time lowering or the block has been lowered
            else:

                #sets the fist time to False as it has just been lowered for the first time previously
                water.first_time = False

                #sets a variable to keep track of current time
                water.time_elapsed = pygame.time.get_ticks()

                #checks if the time elapsed is greater than the start time + variable for time change
                if water.time_elapsed > (water.dt + water.time_change * 1000):

                    #checks if the block has been lowered
                    if water.water_state == "raised":

                        #raises the block
                        water.lower(player)



        #checks if boss health is below 25 percent
        elif self.target_health < (self.max_health)*25/100:


            #checks if block is 'raised' and its the first time being lowered
            if water.water_state == "lowered" and water.first_time == False:

                #calls the function to lower the block
                water.rise(player)

            #checks if it isnt the first time lowering or the block has been lowered
            else:

                #sets the fist time to False as it has just been lowered for the first time previously
                water.first_time = True
                
                #sets a variable to keep track of current time
                water.time_elapsed = pygame.time.get_ticks()

                #checks if the time elapsed is greater than the start time + variable for time change
                if water.time_elapsed > (water.dt + water.time_change * 1000):

                    #checks if the block has been lowered
                    if water.water_state == "raised":

                        #raises the block
                        water.lower(player)
                

            
        


        

        
        

    
