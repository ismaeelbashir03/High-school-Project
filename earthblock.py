#ismaeel bashir

#imports pygame
import pygame

##createsa  class for the block
class Block(pygame.sprite.Sprite):

    #creates a constructor
    def __init__(self):

        #inherits pygame sprite class
        pygame.sprite.Sprite.__init__(self)

        #defines a surface for the sprite
        self.image = pygame.Surface([50, 700])

        #defines image for block
        self.blockimg = pygame.image.load("assets/earth/block.png")
        
        #blits image to surfaace of block
        self.image.blit(self.blockimg, [0,0])

        #makes the color black transparent
        self.image.set_colorkey((255,255,255))

        #creates a variable for the rectangualr area of the surface
        self.rect = self.image.get_rect()

        #sets the x pos
        self.rect.x = 1070

        #sets the y pos
        self.rect.y = -700

        #creates a var for the time taken to lower the block
        self.blockspeed = 20

        #creates a bool for the block state
        self.block_state = "raised"

        #creates a var for time since block lowered
        self.time_elapsed = 0

        #creates a var for the difference in time (used for calculation to check when to raise block)
        self.dt = 0

        #creates a bool to make sure block is lowered only once within range
        self.first_time = True

        #creates a var for the time taken between raising the block and it being lowered
        self.time_change = 15


    #defines a function for lowering the block
    def lower(self):
            
        #checks if the y pos of the block is smaller than zero (it is still raised)
        if self.rect.y < 0:

            #increments the y pos by the block speed var
            self.rect.y += self.blockspeed

        #checks if the y pos is zero
        elif self.rect.y == 0:

            #sets the block to 'lowered'
            self.block_state = "lowered"

            #sets the time when the block was lowered (used fot time calculation)
            self.dt = pygame.time.get_ticks()


    #defines a function for raising the block 
    def rise(self):

        #checks if the y pos is between -700 and 0
        if -700 <= self.rect.y <= 0:

            #increments the y pos by the block speed
            self.rect.y -= self.blockspeed

        #checks if the y pos is -700
        if self.rect.y == -700:

            #sets the block state to 'raised'
            self.block_state = "raised"
            
