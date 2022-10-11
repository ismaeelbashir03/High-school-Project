#ismaeel bashir

#imports pygame and and other library
import pygame
import random
from superclass_boss import Boss


#creates the boss class
class earthBoss(Boss):

    #creates a constructor
    def __init__(self):

        #calls super function to inherit parent class attributes
        super().__init__()

        #creates a variable to store the boss img
        self.bossimg = pygame.image.load("assets/earth/bossimg.png")

        #blits the boss img to the pygame surface
        self.image.blit(self.bossimg, [0,0])





    #defines block state function        
    def blockstate(self, block):


        #checks if boss health is below 75 percent
        if (self.max_health)*25/100 < self.target_health < (self.max_health)*75/100:

            #checks if block is 'raised' and its the first time being lowered
            if block.block_state == "raised" and block.first_time == True:

                #calls the function to lower the block
                block.lower()

            #checks if it isnt the first time lowering or the block has been lowered
            else:

                #sets the fist time to False as it has just been lowered for the first time previously
                block.first_time = False

                #sets a variable to keep track of current time
                block.time_elapsed = pygame.time.get_ticks()

                #checks if the time elapsed is greater than the start time + variable for time change
                if block.time_elapsed > (block.dt + block.time_change * 1000):

                    #checks if the block has been lowered
                    if block.block_state == "lowered":

                        #raises the block
                        block.rise()



        #checks if boss health is below 25 percent
        elif self.target_health < (self.max_health)*25/100:


            #checks if block is 'raised' and its the first time being lowered
            if block.block_state == "raised" and block.first_time == False:

                #calls the function to lower the block
                block.lower()

            #checks if it isnt the first time lowering or the block has been lowered
            else:

                #sets the fist time to False as it has just been lowered for the first time previously
                block.first_time = True
                
                #sets a variable to keep track of current time
                block.time_elapsed = pygame.time.get_ticks()

                #checks if the time elapsed is greater than the start time + variable for time change
                if block.time_elapsed > (block.dt + block.time_change * 1000):

                    #checks if the block has been lowered
                    if block.block_state == "lowered":

                        #raises the block
                        block.rise()
                

            
        


            


        

        

        
        

    
