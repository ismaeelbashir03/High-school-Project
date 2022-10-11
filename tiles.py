#ismaeel bashir

import pygame

#tile class

class Tile(pygame.sprite.Sprite):

    #creates the contructor
    def __init__(self, x, y, tilesize):

        #inherits the sprite class
        pygame.sprite.Sprite.__init__(self)

        #sets the player img to a pygame surface for the level
        self.image = pygame.Surface([tilesize, tilesize])

        #sets the rect area for the level
        self.rect = self.image.get_rect()

        #creates coordinated for the level
        self.rect.x = x
        self.rect.y = y

        #creates a var for the tile images
        tileimg = pygame.image.load("assets/general/black.png").convert()

        #sets the variable to be the levels surface
        self.image.blit(tileimg, [0,0])


