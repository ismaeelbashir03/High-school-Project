#import pygame library
import pygame
import mysql.connector

#creates player class
class Player(pygame.sprite.Sprite):

    

    #creates constructor
    def __init__(self, x, y):
        
        #inherits pygame sprite class
        pygame.sprite.Sprite.__init__(self)

        #defines players height (used in collsion)
        self.height = 53

        #defines players width
        self.width = 21
        
        #sets a pygame surface for the player        
        self.image = pygame.Surface([self.width,self.height])

        #makes the colour black transparent
        self.image.set_colorkey((255,255,255))

        #creates a rect area for the player
        self.rect = self.image.get_rect()
        
        #defines the players x pos
        self.rect.x = x

        #defines the players y pos
        self.rect.y = y

        #defines is running
        self.isrunning = False

        #defines the direction
        self.direction = "right"

        #defines the animation counts
        self.rcount = 0
        self.lcount = 0

        #defines  the players max speed
        self.maxspeed = 25

        #defines players minimum speed
        self.minspeed = 8

        #defines the players velocity 
        self.vel = self.minspeed

        #defines jump state
        self.isjumping = False

        #defines if player has landed
        self.haslanded = False

        #defines a bool for swimming
        self.swimming = False

        #defines sql statement for getting save
        self.sql_getsave = "SELECT earthunlock, waterunlock, fireunlock FROM player WHERE active = 1"

        #defines bool for unlocking elements

        #creates an instacne of database connection
        mydb = mysql.connector.connect(
            host = "localhost",
            user = "root",
            passwd = "",
            charset  = "utf8",
            database = "Bushi"
            )

        #cretaes an instance of cursor
        mycursor = mydb.cursor()

        #executes sql get save statement
        mycursor.execute(self.sql_getsave)

        #loops for lines in results
        for x in mycursor:

            #sets each line as a var
            self.elementunlock = x

        #commits and closes the database
        mydb.commit()
        mycursor.close()
        mydb.close()

       
        #checks if index 0 of var is set to 1(true)
        if self.elementunlock[0] == 1:

            #unlocks parallel element to true
            self.earthunlock = True

        else:

            #locks the parallel element
            self.earthunlock = False

        #checks if index 1 of var is set to 1(true)
        if self.elementunlock[1] == 1:

            #unlocks parallel element to true
            self.waterunlock = True

        else:

            #locks the parallel element
            self.waterunlock = False

        #checks if index 2 of var is set to 1(true)
        if self.elementunlock[2] == 1:

            #unlocks parallel element to true
            self.fireunlock = True

        else:

            #locks the parallel element
            self.fireunlock = False
        

        #defines animation coutn for jump
        self.jcount = 0

        #defines jump height
        self.jumpheight = 8

        #defines jump start
        self.jumpstart = False

        #defines jump multiplier
        self.jumpmult = 6

        #defines the y value change of jump
        self.yval = self.jumpheight

        #defines gravit for player
        self.gravity = 10

        #defines animation count for attack
        self.acount = 0

        #defines if attacking
        self.isattacking = False

        #defines the attack count for makeing sure you only hit once per press
        self.firstattack = 0

        #defines damage dealt
        self.damage = 20

        #defines the jumptime timer var
        self.jumptimer = 0

        #defines the time till next jump is allowed (seconds)
        self.timetilljump = 0.5
        
        #defines a raduis for collision with fireball
        self.raduis = 10

        #defines elemental status
        self.element = "none"

        #defines an alpha for the lement images
        self.alpha = 0

        #defines animation speed for element symbols
        self.animatespeed = 50

        #defines a var for swim speed and sets it to the minimum speed of player
        self.swimspeed = self.minspeed

        #defines bool for checking if symbol needs to be shown
        self.show = False

        #imports files with animations for jumping left
        self.jumpR = ["assets/animation/jr1.png","assets/animation/jr1.png","assets/animation/jr2.png","assets/animation/jr3.png","assets/animation/jr4.png"]

        #imports files with animations for jumping right
        self.jumpL = ["assets/animation/jl1.png","assets/animation/jl1.png","assets/animation/jl2.png","assets/animation/jl3.png","assets/animation/jl4.png"]

        #imports files with animations for running left
        self.runL = ["assets/animation/l1.png", "assets/animation/l2.png", "assets/animation/l3.png", "assets/animation/l4.png", "assets/animation/l5.png", "assets/animation/l6.png"]

        #imports files with animations for running right
        self.runR = ["assets/animation/r1.png", "assets/animation/r2.png", "assets/animation/r3.png", "assets/animation/r4.png", "assets/animation/r5.png", "assets/animation/r6.png"]

        #imports the files for attack animation
        self.attackR = ["assets/player/ar1.png", "assets/player/ar2.png", "assets/player/ar3.png", "assets/player/ar4.png"]

        #imports attack animation for left
        self.attackL = ["assets/player/al1.png", "assets/player/al2.png", "assets/player/al3.png", "assets/player/al4.png"]

        #imports symbol images for elements
        self.fireimg = pygame.image.load("assets/general/fire.png").convert()
        self.waterimg = pygame.image.load("assets/general/water.png").convert()
        self.earthimg = pygame.image.load("assets/general/earth.png").convert()

        self.smallfireimg = pygame.image.load("assets/general/firesmall.png").convert()
        self.smallwaterimg = pygame.image.load("assets/general/watersmall.png").convert()
        self.smallearthimg = pygame.image.load("assets/general/earthsmall.png").convert()

        
        #initially sets the transparency of each image to 0
        self.earthimg.set_alpha(0)
        self.fireimg.set_alpha(0)
        self.waterimg.set_alpha(0)

        #sets a var for the sound when changing element
        self.elementsound = pygame.mixer.Sound("assets/general/change.wav")





    #creates function for idle animation
    def animation(self):
    

        #checks if player is not running
        if self.isrunning == False and self.isattacking == False and self.isjumping == False and self.haslanded == True and self.jumpstart == False:
            
            #checks if player is looking right
            if self.direction == "right" and self.swimming == False:

                #sets players animation
                self.playerimg = pygame.image.load("assets/animation/sr.png").convert_alpha()


            #checks if player is looking left
            elif self.direction == "left" and self.swimming == False:

                #sets the player animation
                self.playerimg = pygame.image.load("assets/animation/sl.png").convert_alpha()



            elif self.swimming == True:

                #checks if the player is facing right and that the animation count is in limit
                if self.direction == "right" and self.jcount <= 4:

                    #sets the animation for the player
                    self.playerimg = pygame.image.load(self.jumpR[self.jcount]).convert_alpha()


                    #increments the animation count
                    self.jcount += 1

                #checks if the player is facing left and that the animation is in limit
                elif self.direction == "left" and self.jcount <= 4:

                    #sets the animation
                    self.playerimg = pygame.image.load(self.jumpL[self.jcount]).convert_alpha()

                    #increments the animation count
                    self.jcount += 1

                #checks if you have animation count is outwith limit
                else:

                    #resets the animation count
                    self.jcount = 0

                    


        #clears the playersurface from old frame


        #sets a pygame surface for the player        
        self.image = pygame.Surface([21,53])

        #makes the colour black transparent
        self.image.set_colorkey((255,255,255))

        #blits the set animation to player surface
        self.image.blit(self.playerimg, [0,0])

        #creates a mask of the pygame surface
        self.mask = pygame.mask.from_surface(self.image)
        




    #defining a function for moving
    def movement(self):

        #making a shortcut for pygame input keys
        keys = pygame.key.get_pressed()

        #checks if 'a' key is pressed
        if keys[pygame.K_a] and self.rect.x > 0:

            #sets running to true
            self.isrunning = True

            #sets the direction to left
            self.direction = "left"

            #resets the animation count of opther running side
            self.rcount = 0

            #checks if you are not jumping and you have landed
            if self.isjumping == False and self.haslanded == True:

                #checks if you are in range of the animation count
                if self.lcount < 6:

                    #sets the player animation
                    self.playerimg = pygame.image.load(self.runL[self.lcount]).convert_alpha()


                    #increments 1 to the animation count
                    self.lcount += 1
                    
                #checks if animation count is out of range 
                else:

                    #restes the animation count
                    self.lcount = 0

                    
                #checks if velocity is lower than max speed
                if self.vel < self.maxspeed:

                    #increments velocity
                    self.vel += 1

                #checks if velocity matches max speed
                elif self.vel == self.maxspeed:

                    #makes sure the veolicty stays at max speed
                    self.vel = self.maxspeed

            #changes players x pos by using velocity
            self.rect.x -= self.vel

            
                
        #checks if the 'd' key is pressed
        elif keys[pygame.K_d] and self.rect.x < 1400 - self.width:

            #sets it true that you are running
            self.isrunning = True

            #sets the direction to right
            self.direction = "right"

            #resets the other running animation count
            self.lcount = 0

            #checks if you arnt jumping and have landed
            if self.isjumping == False and self.haslanded == True:

                #checks if you havent exceed the animation count
                if self.rcount < 6:

                    #sets the player animation
                    self.playerimg = pygame.image.load(self.runR[self.rcount]).convert_alpha()

                    #increments the animation count
                    self.rcount += 1

                #checks if you are over the animation count limit
                else:

                    #resets the animation count 
                    self.rcount = 0

            
                #checks if the velocity is lower than the max speed
                if self.vel < self.maxspeed:        

                    #increments the velocity by 1
                    self.vel += 1

                #checks of the velocity is matching the max speed
                elif self.vel == self.maxspeed:

                    #makes sure the velocity stays at the max speed
                    self.vel = self.maxspeed

            
            #changes the players x pos by using the velocity
            self.rect.x += self.vel

        #checks if you arent running
        else:

            #sets running to false
            self.isrunning = False

            #resets the velocity
            self.vel = self.minspeed




            
    #defines the jump function
    def jump(self):

        #creates shortcut for keys
        keys = keys = pygame.key.get_pressed()

        #checks if you have pressed the 'space' key and that the player is touching the floor (to make sure you cant jump in the air) 
        if keys[pygame.K_SPACE] and self.haslanded == True and self.jumptimer + (self.timetilljump)*1000 < pygame.time.get_ticks():
            
            #sets the jump timer
            self.jumptimer = pygame.time.get_ticks()

            #sets the y value to the preset jumpheight
            self.yval = self.jumpheight

            #sets it that you havent landed yet
            self.haslanded = False

            #sets start jump to true
            self.jumpstart = True




        #checks if jumpstart is true
        if self.jumpstart == True:
            
            #checks if player is facing right and jumpcount is less than 4
            if self.direction == "right" and self.jcount < 5:

                #sets the animation
                self.playerimg = pygame.image.load(self.jumpR[self.jcount])

                #increments j count
                self.jcount += 1


            #checks if player is facing left and j count is less than 5
            if self.direction == "left" and self.jcount < 5:

                #sets the animation
                self.playerimg = pygame.image.load(self.jumpL[self.jcount])
                
                #increments j count
                self.jcount += 1

            #checks if j count is over 5
            if self.jcount >= 5:

                #sets is jumoing to true
                self.isjumping = True

                #sets jumpstart to false
                self.jumpstart = False

                #resets the jump count
                self.jcount = 0

                
            

        #checks if you are jumping
        if self.isjumping == True:
            
            
            #checks if the y value is greater than 0 (makes sure you dont jump down)
            if self.yval >= 0:

                #sets the players y pos to the yvalue multiplied by the players jump multiplier
                self.rect.y -= self.yval * self.jumpmult

                #increments the y value by -1
                self.yval -= 1
                
            #checks if the y value has reached below 0
            else:

                #sets it that you arnt jumping anymore
                self.isjumping = False

                #resets the jump animation count
                self.jcount = 0

                #sets it that you havent landed yet
                self.haslanded = False


        #checks if you have not landed and havent jumped (checks if in air)
        if self.haslanded == False and self.isjumping == False:

            #checks if the player is facing right and that the animation count is in limit
            if self.direction == "right":

                #sets the animation for the player
                self.playerimg = pygame.image.load("assets/animation/sr.png")


            #checks if the player is facing left and that the animation is in limit
            elif self.direction == "left":

                #sets the animation
                self.playerimg = pygame.image.load("assets/animation/sl.png")







    #defines the physics function
    def physics(self):

    #gravity
        if self.swimming == False:

            #checks if you have not landed and are not jumping (you are falling)
            if self.haslanded == False and self.isjumping == False:

                #makes sure gravity doesnt exceed limit
                if self.gravity < 20:

                    #incremnts the gravity by 1
                    self.gravity += 1

                #checks if the gravity is at max gravity
                elif self.gravity == 20:

                    #makes sure gravity stays at max gravity
                    self.gravity = 20

                #changes y pos of the player by using the gravity
                self.rect.y += self.gravity

        else:

            #checks if you have not landed and are not jumping (you are falling)
            if self.haslanded == False and self.isjumping == False:

                if self.element == "water":
                    
                    self.gravity = 18

                else:

                    self.gravity = 8

                #changes y pos of the player by using the gravity
                self.rect.y += self.gravity


            





    #defines the collision function
    def collision(self, tiles, bosses, blocks):

        #tile collision


        #checks if the player has collided with the tiles(platforms)
        if pygame.sprite.spritecollide(self, tiles, False):
            
            #sets it that you have landed
            self.haslanded = True

        #chekcs if you havent touched a tile (platform)
        else:

            #sets it that you havent landed
            self.haslanded = False
            
        #gets the tiles that you have hit
        hit = pygame.sprite.spritecollide(self, tiles, False)
        
        #goes through each tile that has been hit by the player
        for tile in hit:

            #checks if you arent jumping
            if self.isjumping == False:

                #sets the y pos of the player so that he can stand on top of the platform
                self.rect.y = tile.rect.y - (self.rect.height-1)

        

        #boss collision

        #checks if the player has collided with the boss
        if pygame.sprite.spritecollide(self, bosses, False):

            #gets the instance of the boss collided with
            for boss in bosses:

                #sets the x pos of the player to the bosses left
                self.rect.x = boss.rect.left - 15



        #block collision

        #checks if the player has collided with the block
        if pygame.sprite.spritecollide(self, blocks, False):

            #gets the instance of block collided with
            for block in blocks:

                #sets the players x pos to the block's left
                self.rect.x = block.rect.left - 20





    #defines a function for checking if player has attacked
    def attack(self):


        #creates shortcut for keys
        keys = pygame.key.get_pressed()



        #checks if player has pressed 'e'
        if keys[pygame.K_e]:

            #sets the bool of is attacking to true
            self.isattacking = True
            

        
        #checks if the player is attacking
        if self.isattacking == True:

            #increments an attack count (usedn to make sure the player only attacks once while hitting 'e')
            self.firstattack += 1



            #checks if the direction is right (facing the boss)
            if self.direction == "right":

                #checks if the animation count is in range
                if self.acount < 4:

                    #sets the player animation for facing right
                    self.playerimg = pygame.image.load(self.attackR[self.acount]).convert_alpha()
                    


                    #incremnts the animation count
                    self.acount += 1



                #checks if the animation count is outwith range (finished attacking)
                else:

                    #restes the animation count
                    self.acount = 0

                    #sets the player to not attacking
                    self.isattacking = False

                    #restes the attack count (so you can hit again after pressing e again)
                    self.firstattack = 0



            #checks the player is facing left
            if self.direction == "left":

                #checks if animation count is in range
                if self.acount < 4:

                    #sets the player animation for facing left
                    self.playerimg = pygame.image.load(self.attackL[self.acount]).convert_alpha()


                    #increments the animation count
                    self.acount += 1



                #checks if the animation count is outwith the range (finsihed attacking)
                else:

                    #restes the animation count
                    self.acount = 0

                    #sets the player to not attacking
                    self.isattacking = False

                    #resets the attack count
                    self.firstattack = 0






    #defines a function to check if player is hit
    def checkhit(self, fireballs, lava):

        #initialises died bool
        died = False
    
        #checks if player collides with any of the fireballs in group
        if pygame.sprite.spritecollide(self, fireballs, False, pygame.sprite.collide_circle) or self.rect.y > 1400:
       
        
                #takes you back to the main menu
                died = True

        if lava != None:
        
            #checks if touching lava (the plus 5 is lee way, makes it a little easier)
            if self.rect.bottom > lava.rect.top+(5):

                #takes you back to the start
                died = True

        if died == True:
            
            pygame.mixer.stop()
            death = pygame.mixer.Sound("assets/general/death.wav")
            death.play()


        return died


    #definesa  fucntion for the player hud
    def hud(self, screen, smallfont):
        
        #sets the symbol images to make the colour black transparent
        self.smallfireimg.set_colorkey((0,0,0))
        self.smallearthimg.set_colorkey((0,0,0))
        self.smallwaterimg.set_colorkey((0,0,0))

        #sets a var for holding the numbers
        one = smallfont.render("1", 1, (255, 255, 255))
        two = smallfont.render("2", 1, (255, 255, 255))
        three = smallfont.render("3", 1, (255, 255, 255))

        #blits all the symbols to the screen
        screen.blit(self.smallwaterimg, [5, 10])
        screen.blit(self.smallearthimg, [25, 10])
        screen.blit(self.smallfireimg, [50, 10])
        screen.blit(one, [5, 35])
        screen.blit(two, [25, 35])
        screen.blit(three, [50, 35])


        #checks if element is unlocked
        if self.fireunlock == True:

            #sets transparency to full
            self.smallfireimg.set_alpha(255)

        else:

            #sets transparency to 0
            self.smallfireimg.set_alpha(0)


        #checks if element is unlocked
        if self.waterunlock == True:

            #sets transparency to full
            self.smallwaterimg.set_alpha(255)

        else:

            #sets transparency to 0
            self.smallwaterimg.set_alpha(0)


        #checks if element is unlocked
        if self.earthunlock == True:

            #sets transparency to full
            self.smallearthimg.set_alpha(255)

        else:

            #sets transparency to 0
            self.smallearthimg.set_alpha(0)

        

        




    #defines a function for showing element symbol on screen
    def showelement(self, screen):

        #sets the symbol images to make the colour black transparent
        self.fireimg.set_colorkey((0,0,0))
        self.earthimg.set_colorkey((0,0,0))
        self.waterimg.set_colorkey((0,0,0))

        #blits all the symbols to the screen
        screen.blit(self.waterimg, [350, 10])
        screen.blit(self.earthimg, [350, 10])
        screen.blit(self.fireimg, [350, 10])
        
        #checks if the water element is set
        if self.element == "water" and self.waterunlock == True:

            #sets other symbols to be transparent
            self.earthimg.set_alpha(0)
            self.fireimg.set_alpha(0)

            #checks if it needs to be shown and if the alpha is in between required values
            if self.show == True and 255 > self.alpha >= 0:

                #changes the alpha of the image by a variable
                self.waterimg.set_alpha(self.alpha)

                #the variable increments by the animation speed variable
                self.alpha += self.animatespeed

                #checks if the alpha is greater than the max alpha
                if self.alpha > 255:

                    #sets the alpha to the max alpha
                    self.alpha = 255
    
            #checks if the alpha is smaller than or equal to 255 and is greater than zero
            elif 0 < self.alpha <= 255:

                #says that we should not be showing the symbol anymore
                self.show = False

                #sets the alpha of the image by a variable
                self.waterimg.set_alpha(self.alpha)

                #increments the variable by a set animation speed variable
                self.alpha -= self.animatespeed

                #checks if the alpha is below zero
                if self.alpha < 0:

                    #sets the alpha to zero
                    self.alpha = 0

        
        #checls if the lement chosen is earth
        if self.element == "earth" and self.earthunlock == True:

            #sets other symbols to be transparent
            self.waterimg.set_alpha(0)
            self.fireimg.set_alpha(0)

            #checks if it needs to be shown and if the alpha is in between required values
            if self.show == True and 255 > self.alpha >= 0:

                #changes the alpha of the image by a variable
                self.earthimg.set_alpha(self.alpha)

                #the variable increments by the animation speed variable
                self.alpha += self.animatespeed

                #checks if the alpha is greater than the max alpha
                if self.alpha > 255:

                    #sets the alpha to the max alpha
                    self.alpha = 255
    
            #checks if the alpha is smaller than or equal to 255 and is greater than zero
            elif 0 < self.alpha <= 255:

                #says that we should not be showing the symbol anymore
                self.show = False

                #sets the alpha of the image by a variable
                self.earthimg.set_alpha(self.alpha)

                #increments the variable by a set animation speed variable
                self.alpha -= self.animatespeed

                #checks if the alpha is below zero
                if self.alpha < 0:

                    #sets the alpha to zero
                    self.alpha = 0



        if self.element == "fire" and self.fireunlock == True:

            #sets other symbols to be transparent
            self.earthimg.set_alpha(0)
            self.waterimg.set_alpha(0)

            #checks if it needs to be shown and if the alpha is in between required values
            if self.show == True and 255 > self.alpha >= 0:

                #changes the alpha of the image by a variable
                self.fireimg.set_alpha(self.alpha)

                #the variable increments by the animation speed variable
                self.alpha += self.animatespeed

                #checks if the alpha is greater than the max alpha
                if self.alpha > 255:

                    #sets the alpha to the max alpha
                    self.alpha = 255
    
            #checks if the alpha is smaller than or equal to 255 and is greater than zero
            elif 0 < self.alpha <= 255:

                #says that we should not be showing the symbol anymore
                self.show = False

                #sets the alpha of the image by a variable
                self.fireimg.set_alpha(self.alpha)

                #increments the variable by a set animation speed variable
                self.alpha -= self.animatespeed

                #checks if the alpha is below zero
                if self.alpha < 0:

                    #sets the alpha to zero
                    self.alpha = 0


    #definesa  function for setting elemental powers
    def elementpowers(self):


        #creates shortcut for getting keys
        keys = pygame.key.get_pressed()

        #checks if '1' is pressed on the keyboard
        if keys[pygame.K_1] and self.waterunlock == True:

            #sets the state to 'water'
            self.element = "water"
            self.show = True
            self.alpha = 0
            self.elementsound.play()

        #checks if '2' is pressed
        elif keys[pygame.K_2] and self.earthunlock == True:

            #sets the state to 'earth'
            self.element = "earth"
            self.show = True
            self.alpha = 0
            self.elementsound.play()

        #checks if '3' is pressed
        elif keys[pygame.K_3] and self.fireunlock == True:

            #sets the state to 'fire'
            self.element = "fire"
            self.show = True
            self.alpha = 0
            self.elementsound.play()

        #checks if '4' is pressed
        elif keys[pygame.K_4]:

            #sets the state to 'none'
            self.element = "none"
            self.elementsound.play()


    #sets powers

            
        #checks if the water power is used
        if self.element == "water":


            #sets positive attrubutes

            #increased speed (maxspeed and minspeed increased)
            self.maxspeed = 35
            self.minspeed = 18
            self.swimspeed = 18

            #sets negatives attributes

            #decreased damage and jump height
            self.jumpmult = 5
            self.damage = 10
            



        #checks if using earh power
        elif self.element == "earth":

            #sets the positive attrivutes

            #increases jump height and slight increase to damage
            self.jumpmult = 10
            self.damage = 25

            #sets the negative attributes

            #decreases speed (max and mins speed decreased)
            self.maxspeed = 20
            self.minspeed = 8
            self.swimspeed = 5



        #checks if the fire power is used
        elif self.element == "fire":

            #sets the positive attributes

            #doubles the players damage
            self.damage = 40

            #sets the negative attributes

            #rest of attributes are set to 'normal'
            self.maxspeed = 25
            self.minspeed = 8
            self.jumpmult = 6
            self.swimspeed = 8


            
        #checks if you are not using power
        elif self.element == "none":

            #sets all attributes to 'normal'
            self.maxspeed = 25
            self.minspeed = 8
            self.jumpmult = 6
            self.damage = 20
            self.swimspeed = 8


    
    def swim(self):

        #sets swimming to true
        self.swimming = True

        #gest shortcut for keys pressed
        keys = pygame.key.get_pressed()

        #checks if the player is facing right and that the animation count is in limit
        if self.direction == "right" and self.jcount < 6:

            #sets the animation for the player
            self.playerimg = pygame.image.load(self.runR[self.jcount]).convert_alpha()


            #increments the animation count
            self.jcount += 1

        #checks if the player is facing left and that the animation is in limit
        elif self.direction == "left" and self.jcount < 6:

            #sets the animation
            self.playerimg = pygame.image.load(self.runL[self.jcount]).convert_alpha()

            #increments the animation count
            self.jcount += 1

        #checks if you have animation count is outwith limit
        else:

            #resets the animation count
            self.jcount = 0

        #checks if space is pressed and rect is above 0
        if keys[pygame.K_SPACE] and self.rect.y >=0:

            #sets has landed to false
            self.haslanded = False

            #sets is jumping to false
            self.isjumping = True

            #increments y pos by swim speed
            self.rect.y -= self.swimspeed
    
        else:

            #sets is jumping to false
            self.isjumping = False



            

        







    #defines a function for travelling through portals
    def portal(self, fireportals, waterportals, earthportals, corruptportals):

        #sets done to intially false
        done = False

        #sets the level back to nothing
        level = ""

        #checks if you have collided with the fire portal
        if pygame.sprite.spritecollide(self, fireportals, False):

            #gets that instance of fire portal
            for portal in fireportals:

                #checks if you are hitting the middle of the portal
                if self.rect.x < portal.rect.center[0]:

                    #exits game loop/ sets done to true
                    done = True

                    #defines which level to put you in
                    level = "fire"
                    
            
            
        #checks if you have collided with the earth portal
        if pygame.sprite.spritecollide(self, earthportals, False):

            #gets that instance of earth portal
            for portal in earthportals:
                
                #checks if you are hitting the middle of the portal
                if self.rect.x < portal.rect.center[0]:

                    #exits game loop/ sets done to true
                    done = True

                    #defines which level to put you in
                    level = "earth"


        #checks if you have collided with the fire portal
        if pygame.sprite.spritecollide(self, waterportals, False):

            #gets instance of that water portal
            for portal in waterportals:
                
                #checks if you are hitting the middle of the portal
                if self.rect.x < portal.rect.center[0]:

                    #exits game loop/ sets done to true
                    done = True

                    #defines which level to put you in
                    level = "water"


        #checks if you have collided with the fire portal
        if pygame.sprite.spritecollide(self, corruptportals, False):

            #gets instance of that water portal
            for portal in corruptportals:
                
                #checks if you are hitting the middle of the portal
                if self.rect.x < portal.rect.center[0]:

                    #exits game loop/ sets done to true
                    done = True

                    #defines which level to put you in
                    level = "corrupt"

        #returns values
        return done, level
                    
            






    
