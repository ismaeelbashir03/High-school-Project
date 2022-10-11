#ismaeel bashir

#imports files
import pygame

#creates class for water
class Water(pygame.sprite.Sprite):

    #cretaes constructor
    def __init__(self):

        #inherits pygame attributes
        pygame.sprite.Sprite.__init__(self)

        #sets a surface
        self.image = pygame.Surface([1400, 700])

        #sets an image
        self.waterimg = pygame.image.load("assets/water/water.jpg")

        #blits the image to surface
        self.image.blit(self.waterimg, [0,0])

        #gets a rect from surface
        self.rect = self.image.get_rect()

        #sets x pos
        self.rect.x = 0

        #sets y pos
        self.rect.y = 0

        #sets alpha
        self.alpha = 0

        #sets rise speed
        self.risespeed = 10

        #sets water state
        self.water_state = "lowered"

        #sets first time
        self.first_time = True

        #sets time elapsed
        self.time_elapsed = 0

        #sets dt
        self.dt = 0

        #sets time change
        self.time_change = 15

        #sets image alpha
        self.image.set_alpha(self.alpha)


    #defines function to rise water
    def rise(self, player):

        #sets player swimming to true
        player.swimming = True

        #checks if alpha is below 100
        if self.alpha < 100:

            #increments alpha by rise speed
            self.alpha += self.risespeed

            #sets alpha
            self.image.set_alpha(self.alpha)

        #checks if alpah is 100
        elif self.alpha == 100:

            #sets alpha
            self.image.set_alpha(self.alpha)

            #sets water state to raised
            self.water_state = "raised"

            #records time
            self.dt = pygame.time.get_ticks()

    #defines a function to lower water
    def lower(self, player):

        #sets player swimming to false
        player.swimming = False

        #checks iof alpha is greater than zero
        if self.alpha > 0:

            #increments alpha by rise speed
            self.alpha -= self.risespeed

            #sets alpha
            self.image.set_alpha(self.alpha)

        #chercks if alpha is 0
        elif self.alpha == 0:

            #sets alpha
            self.image.set_alpha(self.alpha)

            #sets water state to lowered
            self.water_state = "lowered"

            
