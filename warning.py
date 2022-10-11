#ismaeel bashir

#imports file
import pygame

#creates warning class
class Warning_sign(pygame.sprite.Sprite):

    #creates constructor
    def __init__(self, y):

        #inherits pygame attributes
        pygame.sprite.Sprite.__init__(self)

        #sets pygame surface
        self.image = pygame.Surface([100,106])
        
        #sets var for image
        self.warningimg = pygame.image.load("assets/general/warning.png") 

        #blits image to screen
        self.image.blit(self.warningimg, [0,0])

        #sets black to transparent
        self.image.set_colorkey((0,0,0))

        #gets rect of surface
        self.rect = self.image.get_rect()

        #defines x pos
        self.rect.x = 1100

        #defines y pos
        self.rect.y = y

        #defines dt
        self.dt = pygame.time.get_ticks()

        #defines time till kill
        self.time_kill = 2

        #defines timer
        self.time_elapsed = 0


    #defines function to kill warning
    def kill(self, warnings):

        #gets time
        self.time_elapsed = pygame.time.get_ticks()

        #checks if time has passed from time_kill
        if self.dt + (self.time_kill)*1000 < self.time_elapsed:

            #gest sprite list of group
            sprite_list = warnings.sprites()

            #gets each sprite in group
            for sprite in sprite_list:

                #checks if self is sprite
                if self == sprite:

                    #removes self from group
                    warnings.remove(self)
        

