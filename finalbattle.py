#ismaele bashir
#final battle


#creates a function to be called when imported in file
def finale():
    
    #imports files
    import pygame                               
    import math
    import random
    import typewriter as t
    import BrianV2 as b
    import popup as p
    import particles as ptcl
    import mysql.connector
    from os.path import join
    import os
    import file_handelling as fh
    import insertion_sort as i

    # Define Classes (sprites) here

            
        
    #bullet hell player

    #creates a class for the player as a box
    class Box(pygame.sprite.Sprite):

        #creates the constructor
        def __init__(self):

            #inherits pygame sprite attributes
            pygame.sprite.Sprite.__init__(self)

            #creates a pygame surface
            self.image = pygame.Surface([20,20])

            #creates a rect of the surface
            self.rect = self.image.get_rect()

            #defines the start x pos
            self.rect.x = 700

            #defines the start y pos
            self.rect.y = 350

            #blits a colour to the surface
            self.image.blit(pygame.image.load("assets/finale/red.jpg"), [0,0])

            #defines a speed for player
            self.speed = 20


        #defines a function to move
        def move(self):

            #creates a shortcut for keys pressed
            keys = pygame.key.get_pressed()

            #checks if player ios pressing 'a' and is not leaving screen
            if keys[pygame.K_a] and self.rect.x > 10:

                #increments player x by negative speed
                self.rect.x -= self.speed

            #checks if player ios pressing 'a' and is not leaving screen
            if keys[pygame.K_d] and self.rect.x < 1380:

                #increments players x by speed
                self.rect.x += self.speed

            #checks if player ios pressing 'a' and is not leaving screen
            if keys[pygame.K_w] and self.rect.y > 10:

                #increments players y pos by negative speed
                self.rect.y -= self.speed

            #checks if player ios pressing 'a' and is not leaving screen
            if keys[pygame.K_s] and self.rect.y < 670:

                #increments players y pos by speed
                self.rect.y += self.speed


        #defines a function to check if you have been hit
        def checkdead(self, screen, white, clock):

            #checks if player has collided with mobs group
            if pygame.sprite.spritecollide(self, mobs, False):

                #creates a list of death messages
                message = (("Brian: ",
                           "       i can bring you back and keep killing you as much as i want",
                           "       and ill keep doing this until i grow bored of playing with you.",
                            "      and as long as i have my lifesource at the game file path, i can do what",
                            "      i want.",
                            "        ",
                            "press SPACE to continue..."),

                           ("Brian:  ",
                            "        this is fun, killing you again and again, and becuase i have my lifesource file",
                            "        connected to the games file path, i can use your computer power to draw strength",
                            "         ",
                            "press SPACE to continue..."),

                           ("Brian:  ",
                            "        this is too good, you are so weak, and with my lifesource connected to the games file path",
                            "        im even stronger",
                            "         ",
                            "--Brian laughs--",
                            "         ",
                            "press SPACE to continue...")
                           
                           )

                #chooses a message from the list radnomly
                message = random.choice(message)

                #fills the screen to black
                screen.fill((0,0,0))

                #calls the typewriter function to blit text to screen
                t.typewriter(message, screen, white, clock)

                #calls the finale function (replays this function)
                finale()

    #creates a class for the bullets shot by the player
    class Bullet(pygame.sprite.Sprite):

        #creates a constructor
        def __init__(self, player, targetx, targety, check_lifesource):

            #inherits pygame sprite attributes
            pygame.sprite.Sprite.__init__(self)

            #creates a pygame surface
            self.image = pygame.Surface([10,10])

            #creates a rect for the surface
            self.rect = self.image.get_rect()

            #blits a colour to the surface
            self.image.blit(pygame.image.load("assets/finale/green.jpg"), [0,0])

            #defines the x poc to the players x pos
            self.rect.x = player.rect.x

            #defines the y pos to the players pos
            self.rect.y = player.rect.y

            #defines a speed var for bullets
            self.speed = 50

            #gets angle to shoot atusing arc tan and gradient
            angle = math.atan2(targety - self.rect.y, targetx - self.rect.x)

            #creates a difference in x pos using cos
            self.dx = math.cos(angle)*self.speed

            #createsa a difference in y pos using sin
            self.dy = math.sin(angle)*self.speed

            #creates a x pos for floats
            self.x = self.rect.x

            #creates a y pos for floats
            self.y = self.rect.y

            #checks if player hasnt deleted file on desktop
            if check_lifesource == True:

                #sets damage to 1
                self.damage = 1

            #checks if player has deleted file on desktop
            else:

                #sets damage to 100
                self.damage = 100


        #createsa  function for moving the bullet
        def move(self):

            #creates an x pos with the difference in x incremented
            self.x = self.x + self.dx

            #creates an y pos with the difference in y incremented
            self.y = self.y + self.dy

            #round the float to be set to the bullets rect
            self.rect.x = int(self.x)

            #round the float to be set to the bullets rect
            self.rect.y = int(self.y)

            #checks if bullet leaves screen
            if 1400+5 < self.rect.x or self.rect.x < 0-5 or 700+5 < self.rect.y or self.rect.y < 0-5:

                #removes bullet from group
                bullets.remove(self)

        #definesa  function to check if bullet hit mob
        def hit(self, health):

            #gets list of all mobs that got hit by bullets
            hit = pygame.sprite.spritecollide(self, mobs, False)

            #iterates through each mob in list
            for mob in hit:

                #increment the mobs health by damage
                mob.health -= self.damage

                #increments brians health by damage
                health -= self.damage

                #sets the bool sprite flash effect to true
                mob.flash = True

                #sets the flash count to zero
                mob.flashcount = 0

            #checks if bullet has collided with mobs
            if pygame.sprite.spritecollide(self, mobs, False):

                #removes the bullet from group
                bullets.remove(self)

            #returns values
            return health



            
    #creates a class for mobs
    class Mob(pygame.sprite.Sprite):

        #creates a constructor for the class
        def __init__(self):

            #inherits pygame sprite attributes
            pygame.sprite.Sprite.__init__(self)

            #sets a pygame surface for the mobs
            self.image = pygame.Surface([30,30])

            #blits a colour to the surface
            self.image.blit(pygame.image.load("assets/finale/yellow.jpg"), [0,0])

            #creates a rect from the surface
            self.rect = self.image.get_rect()

            #defines a x pos to be random and in screen range
            self.rect.x = random.randrange(0, 1400-20)

            #defines a y pos to be random and appear on top of screen
            self.rect.y = random.randrange(-100, -40)

            #creates a radnom speed for y vel
            self.speedy = random.randrange(5, 10)

            #creates a radnom speed for x vel
            self.speedx = random.randrange(-4, 4)

            #sets the health of mob
            self.health = 50

            #sets the bool for flash effect on sprite
            self.flash = False

            #sets flashcount to 0
            self.flashcount = 0


        #defines a function to move
        def move(self):

            #increments y pos by y vel
            self.rect.y += self.speedy

            #increments x pos by x vel
            self.rect.x += self.speedx

            #checks if mob leaves screen
            if self.rect.top > 700+20 or self.rect.left < 0-20 or self.rect.right > 1400+20:

                #resets the values for mob to respawn inscreen
                self.rect.x = random.randrange(0, 1400-20)
                self.rect.y = random.randrange(-100, -40)
                self.speedy = random.randrange(5, 18)

                
        #definesa  function ofr checking if mob is dead
        def checkdead(self, Particle, particles):

            #checks if mob health is below zero
            if self.health < 0:

                #sets mob health to zero
                self.health = 0

                #loops 20 times
                for x in range(20):

                    #createsa  particle at mobs pos
                    p = Particle(self.rect.x, self.rect.y)

                    #adds particle to list
                    particles.append(p)

                #removes mob from list
                mobs.remove(self)

            #returns values
            return particles


        #defines a function for flash effect when hit
        def flashhit(self):

            #checks if mob flash is true and flash count is below 2 (only happens for 2 seconds)
            if self.flash == True and self.flashcount  < 2:

                #blits a white screen to mob surface
                self.image.blit(pygame.image.load("assets/finale/white.jpg"), [0,0])

                #increments flashcount
                self.flashcount += 1

            #checks if flash is true but flash count is grater than 2 (time passsed)
            elif self.flash == True and self.flashcount == 2:

                #blits origional colour to surface
                self.image.blit(pygame.image.load("assets/finale/yellow.jpg"), [0,0])

                #sets flash to false
                self.flash = False
                



    pygame.init()                               # Pygame is initialised (starts running)

    #records the start time
    timer = pygame.time.get_ticks()
    
    pygame.mixer.init()
    
    screen = pygame.display.set_mode([1400,700]) # Set the width and height of the screen [width,height]
    pygame.display.set_caption("Final battle")       # Name your window
    done = False                                # Loop until the user clicks the close button.
    clock = pygame.time.Clock()                 # Used to manage how fast the screen updates
    black    = (   0,   0,   0)                 # Define some colors using rgb values.  These can be
    white    = ( 255, 255, 255)                 # used throughout the game instead of using rgb values.

    #background music set as a variable
    music = "assets/corrupt/corrupt.mp3"

    #plays background music (-1 = loop)
    pygame.mixer.music.load(music)
    pygame.mixer.music.play(-1)

    #sets shooting to false
    shooting = False

    #creates an empty list for particles
    particles = []

    #initally sets dt to 0
    dt = 0

    #creates groups for classes
    players = pygame.sprite.Group()
    bullets = pygame.sprite.Group()
    mobs = pygame.sprite.Group()


    #sets health to 8000 initally
    health = 8000

    # Define additional Functions and Procedures here

    #defines a function to check if file has been deleted from desktop
    def check_lifesource():


        #checks if file is at desktop
        if os.path.exists("Brians_lifesource.txt"):

            #returns true
            return True

        #returns false
        return False


    #calls the check lifesource funtcion
    life_source = check_lifesource()

    #creates an instance of player
    player = Box()

    #creates an instance of brian phase 2
    brian = b.BrianV2()

    #creates an instance of window for popup
    win = p.Win()

    #calls function to popup
    win.showpopup(life_source)

    #loops 80 times
    for x in range(80):

        #creates an instacne of mob
        m = Mob()

        #addsmob to group
        mobs.add(m)
        





    # -------- Main Program Loop -----------
    while done == False:

        #calls function to see if player has deleted file from desktop
        life_source = check_lifesource()

        for event in pygame.event.get():        # Check for an event (mouse click, key press)

            if event.type == pygame.QUIT:       # If user clicked close window


                os.remove("Brians_lifesource.txt")
                pygame.quit()                     # Flag that we are done so we exit this loop

            #checks if mouse buttin is down
            if event.type == pygame.MOUSEBUTTONDOWN and event.button == 1:

                #sets shooting to true
                shooting = True

            #checks if mouse button is up
            if event.type == pygame.MOUSEBUTTONUP and event.button == 1:

                #sets shooting to false
                shooting = False


        #records time for each loop
        time_elapsed = pygame.time.get_ticks()
        
        #checks if shooting is true and it has been 0.1 seconds since last shot (shooting delay)
        if shooting == True and dt+100 < time_elapsed:

            #gets the mouse pos
            x,y = pygame.mouse.get_pos()

            #creates an instance of bullet
            b = Bullet(player, x, y, life_source)

            #adds bullet to group
            bullets.add(b)

            #records time
            dt = pygame.time.get_ticks()
                
                

        #calls function to move player
        player.move()

        #calls function to see if player is dead
        player.checkdead(screen, white, clock)


        #calls function to check brians health
        brian.check_health(health)

        #calls function to see if brian is dead
        done = brian.checkdead()

        #gets each bullet in group
        for bullet in bullets:

            #calls function to move bullet
            bullet.move()

            #calls function to check if bullet is hit
            health = bullet.hit(health)

        #gest each mob in group
        for mob in mobs:

            #calls function to move mob
            mob.move()

            #calls function to show flash effect
            mob.flashhit()

            #calls function to check if dead
            particles = mob.checkdead(ptcl.Particle, particles)
        
        # Update sprites here
        screen.fill(black)

        #draws bullets to screen
        bullets.draw(screen)

        #draws mobs to screen
        mobs.draw(screen)

        #gest each particle in list
        for particle in particles:

            #draws particle
            particle.draw(screen, particles)

        #blits player to screen
        screen.blit(player.image, (player.rect.x, player.rect.y))

        #draws brians health bar
        brian.healthbar(screen)

        #checks if player has won
        if done == True:

            #gets players time of clearance
            player_time = float((pygame.time.get_ticks() - timer)/1000)

            #adds the players score to a list
            finalescore = [player_time]

            #appends other scores from file to the list
            finalescore = fh.readfilelist(finalescore, "!finalescore.txt")

            #sorts the list using insertion sort
            finalescore = i.insertion_sort(finalescore)

            #takes of the first three value from list
            finalescore = finalescore[:3]

            #writes the new list to the file
            fh.rewritefile("!finalescore.txt", finalescore)

            #creates a string for final message
            message = ("Brian:  ",
               "        you were too strong for me player.",
               "        here take the orb, you deserve it...",
               "         ",
               "--Brian hands you the orb--",
               "         ",
               "--you take off, back home, knowing you have just became",
               "  the most powerful S A M U R A I --",
                "          ",
                "press space to exit...")

            #fills the screen to black
            screen.fill(black)

            #calls typewriter function to blit message to screen
            t.typewriter(message, screen, white, clock)
            break
        
        pygame.display.flip()                   # Go ahead and update the screen with what we've drawn.
        clock.tick(20)                          # Limit to 20 frames per second



    #creates aninstance of database connection
    mydb = mysql.connector.connect(
        host = "localhost",
        user = "root",
        passwd = "",
        charset = "utf8",
        database = "Bushi"
        )

    #creates an instance of cursor
    mycursor = mydb.cursor()

    #executes sql statement ot reset save
    mycursor.execute("UPDATE player SET earthunlock = 0, waterunlock = 0, fireunlock = 0, earthfinish = 0, waterfinish = 0, firefinish = 0, corruptfinish = 0 WHERE active = 1")

    #commits and closes the database
    mydb.commit()
    mycursor.close()
    mydb.close()

    pygame.quit()


