#ismaeel bashir

#imports files
import pygame


#creates a class for portals
class Portal(pygame.sprite.Sprite):

    #createsa  constructor
    def __init__(self, x, y, types):

        #inherits pygame attributes
        pygame.sprite.Sprite.__init__(self)

        #defines height
        self.height = 100

        #defines width
        self.width = 50

        #cretaes pygame surface
        self.image = pygame.Surface([self.width, self.height])

        #makes the colour black transparent
        self.image.set_colorkey((0,0,0))

        #creates a rect from the surface
        self.rect = self.image.get_rect()

        #defines the x pos
        self.rect.x = x

        #defines the y pos
        self.rect.y = y

        #defines portal type
        self.type = types

        #defines counters
        self.corrupt_count = 0
        self.fire_count = 0
        self.water_count = 0
        self.earth_count = 0

        #creates lists for images
        self.corruptimages = ["assets/main/corruptedportal5.png", "assets/main/corruptedportal4.png", "assets/main/corruptedportal3.png", "assets/main/corruptedportal2.png", "assets/main/corruptedportal1.png", "assets/main/corruptedportal0.png"]
        self.earthimages = ["assets/main/earthportal5.png", "assets/main/earthportal4.png", "assets/main/earthportal3.png", "assets/main/earthportal2.png", "assets/main/earthportal1.png", "assets/main/earthportal0.png"]
        self.waterimages = ["assets/main/waterportal5.png", "assets/main/waterportal4.png", "assets/main/waterportal3.png", "assets/main/waterportal2.png", "assets/main/waterportal1.png", "assets/main/waterportal0.png"]
        self.fireimages = ["assets/main/fireportal5.png", "assets/main/fireportal4.png", "assets/main/fireportal3.png", "assets/main/fireportal2.png", "assets/main/fireportal1.png", "assets/main/fireportal0.png"]

        #checks if type is water
        if types == "water":

            #blits water image to screen
            self.portalimage = pygame.image.load("assets/main/waterportal5.png").convert_alpha()

        #checks if type is fire
        elif types == "fire":

            #blits fire image
            self.portalimage = pygame.image.load("assets/main/fireportal5.png").convert_alpha()    

        #checks if type is earth
        elif types == "earth":

            #blits earth image
            self.portalimage = pygame.image.load("assets/main/earthportal5.png").convert_alpha()

        #checks if type is corruption
        elif types == "corrupt":

            #blits the corruption image
            self.portalimage = pygame.image.load("assets/main/corruptedportal5.png")


        #blits defined image
        self.image.blit(self.portalimage, [0,0])



    #definesa  function for opening portal
    def open(self, player):

        #checks if type is corrupt and player is in range
        if self.type == "corrupt" and player.rect.x > 1070 and player.rect.y < 500:

            #checks if counter is below 6
            if self.corrupt_count < 6:

                #sets animation
                self.image.blit(pygame.image.load(self.corruptimages[self.corrupt_count]), [0,0])

                #increments counter by 1
                self.corrupt_count += 1
        
        #checks if type is corrupt and player is out of range
        elif self.type == "corrupt" and player.rect.x <= 1070 or player.rect.y >= 500:

            #sets counter to 5 if over 5
            if self.corrupt_count > 5:
                self.corrupt_count = 5


            #checks if counter is above 0
            if self.corrupt_count > 0:
                

                #clears the surface from old frame

                #sets a pygame surface for the player        
                self.image = pygame.Surface([self.width,self.height])

                #makes the colour black transparent
                self.image.set_colorkey((0,0,0))

                #sets the animation
                self.image.blit(pygame.image.load(self.corruptimages[self.corrupt_count]), [0,0])

                #increments counter by -1
                self.corrupt_count -= 1




        #checks if type is earth and player is in range
        if self.type == "earth" and player.rect.x < 330 and player.rect.y > 500:

            #checks if counter is below 6
            if self.earth_count < 6:

                #sets animation
                self.image.blit(pygame.image.load(self.earthimages[self.earth_count]), [0,0])

                #increments counter by 1
                self.earth_count += 1




        #checks if type is earth and player is out of range
        elif self.type == "earth" and player.rect.x >= 330 or player.rect.y <= 500:

            #sets counter to 5 oif over 5
            if self.earth_count > 5:
                self.earth_count = 5

            #checks if counter is above zero
            if self.earth_count > 0:
                
                #clears the surface from old frame

                #sets a pygame surface for the player        
                self.image = pygame.Surface([self.width,self.height])

                #makes the colour black transparent
                self.image.set_colorkey((0,0,0))

                #sets animation
                self.image.blit(pygame.image.load(self.earthimages[self.earth_count]), [0,0])

                #increments counter by -1
                self.earth_count -= 1




        #checks if type is fire and player is in range
        if self.type == "fire" and player.rect.x < 330 and player.rect.y <= 500:

            #checks if counter is below 6
            if self.fire_count < 6:

                #sets animation
                self.image.blit(pygame.image.load(self.fireimages[self.fire_count]), [0,0])

                #increments counter by 1
                self.fire_count += 1

            


        #checks if type is fire and player is out of range
        elif self.type == "fire" and player.rect.x >= 330 or player.rect.y> 500:

            #sets counter to 5 if counter is over 5
            if self.fire_count > 5:
                self.fire_count = 5


            #checks if counter is abive zero
            if self.fire_count > 0:
                
                #clears the surface from old frame

                #sets a pygame surface for the player        
                self.image = pygame.Surface([self.width,self.height])

                #makes the colour black transparent
                self.image.set_colorkey((0,0,0))

                #sets animation
                self.image.blit(pygame.image.load(self.fireimages[self.fire_count]), [0,0])

                #increments counter by -1
                self.fire_count -= 1



        
        #checks if type is water and player is in range
        if self.type == "water" and player.rect.x > 1070 and player.rect.y > 500:         

            #checks if counter is below 6
            if self.water_count < 6:

                #sets animation
                self.image.blit(pygame.image.load(self.waterimages[self.water_count]), [0,0])

                #increments by 1
                self.water_count += 1





        #checks if type is water and player is out of range
        elif self.type == "water" and player.rect.x <= 1070 or player.rect.y<= 500:

            #sets counter to 5 if over 5
            if self.water_count > 5:
                self.water_count = 5

            #checks if counter is above zero
            if self.water_count > 0:
                
                #clears the surface from old frame

                #sets a pygame surface for the player        
                self.image = pygame.Surface([self.width,self.height])

                #makes the colour black transparent
                self.image.set_colorkey((0,0,0))

                #sets animation
                self.image.blit(pygame.image.load(self.waterimages[self.water_count]), [0,0])

                #increments by -1
                self.water_count -= 1


            





                
