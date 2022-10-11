#ismaeel bashir


#imports files
import pygame
import random


#brian

#creates a class for brian
class Brian(pygame.sprite.Sprite):

    #creates a constructor
    def __init__(self, x, y):

        #inherits pygame sprite attributes
        pygame.sprite.Sprite.__init__(self)

        #creates a pygame surface
        self.image = pygame.Surface([21,53])

        #creates a rect for the surface
        self.rect = self.image.get_rect()

        #makes the colour white transparent
        self.image.set_colorkey((255,255,255))

        #sets the x pos of brian
        self.rect.x = x

        #sets the y pos of brian
        self.rect.y = y

        #blits an image to the surface
        self.image.blit(pygame.image.load("assets/brian/brian.png"), [0,0])

        #defines a bool for checking if brian is speaking
        self.speaking = False

        #creates a variable for brians y pos state
        self.y_state = "lowered"

        #sets an intial value for current health
        self.current_health = 1200

        #sets the initial value for the targeted health
        self.target_health = 1200

        #creates a max health var
        self.max_health = 1200

        #creates a var for the legnth of the health bar
        self.healthbar_legnth = self.max_health

        #creates a var for the speed in which the current hea;th will catch up to the targeted health
        self.health_changespeed = 5


    #creates a function for drawing speech to screen
    def drawspeech(self, screen, text, player):

        
        #text

        #creates a font type
        font = pygame.font.SysFont("arial", 24)

        #renders the font with 'text' var which has been passed in
        speech = font.render(text, True, (255,255,255))

        #gets the rect area of the speech
        speech_rect = speech.get_rect(midbottom = self.rect.midtop)


        #gets the modulus of the difference between players x pos and brians x pos
        if abs(player.rect.x - self.rect.x) < 100:

            #draws text to screen at speech rect
            screen.blit(speech, speech_rect)



    #defines a function for dealing damage
    def givedamage(self, player):

        #checks if the player is in the same y range as brian
        if player.rect.y >= self.rect.y and player.rect.y < self.rect.y+21:
            #checks if the player is near the boss and is facing him
            if self.rect.x- 30 < player.rect.x < self.rect.x and player.direction == "right":
                #checks if the player is attacking and makes sure he only hits him once per attack 
                if player.isattacking == True and player.firstattack == 1:

                    #checks if the targeted health is above zero
                    if self.target_health > 0:

                        #lowers the targeted health of the boss
                        self.target_health -= player.damage

                #checks if the health is below or equal to zero
                if self.target_health <= 0:

                    #sets the health to be zero
                    self.target_health = 0


            #checks if the player is near the boss and is facing him
            if self.rect.x + 30 > player.rect.x > self.rect.x and player.direction == "left":
                
                #checks if the player is attacking and makes sure he only hits him once per attack 
                if player.isattacking == True and player.firstattack == 1:

                    #checks if the targeted health is above zero
                    if self.target_health > 0:

                        #lowers the targeted health of the boss
                        self.target_health -= player.damage

                #checks if the health is below or equal to zero
                if self.target_health <= 0:

                    #sets the health to be zero
                    self.target_health = 0




    #defines a function which creates the health bar
    def healthbar(self, screen):
        
        #sets an initial width for the animated health
        transition_width = 0

        #sets an initial colour for the animated health
        transition_colour = (255, 0, 0)

        #checks if the targeted health is smaller than the current health
        if self.current_health > self.target_health:

            #increments the current health to reach the targeted health
            self.current_health -= self.health_changespeed

            #sets the health animation width (how big it is supposed to be)
            transition_width = (self.target_health - self.current_health)

            #sets the colour of the health animation 
            transition_colour = (255, 255, 0)

        #creates a rectangle for the health bar with the current health
        healthbar_rect = pygame.Rect((100, 10, self.current_health, 25))

        #creates a rectangle for the health which is going to be animated
        transitionbar_rect = pygame.Rect((healthbar_rect.right, 10, transition_width, 25))

        #draws the health bar with current health
        pygame.draw.rect(screen,(255, 0, 0), healthbar_rect)

        #draws the health bar with the animated health
        pygame.draw.rect(screen, transition_colour, transitionbar_rect)

        #draws an outline for the health
        pygame.draw.rect(screen, (0,0,0), (100, 10, self.healthbar_legnth, 25), 4)


    #createsa  function to rise brian
    def rise(self, dt):

        #checks if brians y pos is lowered
        if self.rect.y > 10 and self.y_state == "lowered":

            #increments the y pos by -10
            self.rect.y -= 10

            #checks if brian has reached the top of the screen (y = 10)
            if self.rect.y <= 10:

                #sets the bool for brinas state to 'raised'
                self.y_state = "raised"

                #records the time brian was raised
                dt = pygame.time.get_ticks()

        #returns values
        return dt


    #defines the function for lowering brian
    def lower(self, dt, dt2, time_elapsed, insults, text):

        #checks if brians y is raised
        if self.rect.y < 625 and self.y_state == "raised":

            #increments the y pos by 10
            self.rect.y += 10

            #checks if brians y pos is at floor level (y = 625)
            if self.rect.y >= 625:

                #sets the bool for brians y state to 'lowered'
                self.y_state = "lowered"

                #gets a random insult from list that has been passed in
                text = random.choice(insults)

                #removes insult from list, so there are no repeats
                insults.remove(text)

                #records the time brian was lowered
                dt2 = pygame.time.get_ticks()

        #checks if brians y state is lowered
        if self.y_state == "lowered":  

                #checks if it has been 5 seconds sionce brian lowered (5000ms = 5 secs)
                if dt2+5000 < time_elapsed:

                    #records when that time has been reached
                    dt = pygame.time.get_ticks()

        #returns values
        return dt, dt2, text


                
                                         



    #defines a function for the boss attack
    def attack(self, Fireball, fireballs):

        #gives a chance of 3 precent (per frame) for this happening
        if random.randrange(1,100) <= 30:
            
            #creates a random y coordinate
            random_x = random.randint(1, 1400)

            #createa an instance of fireball class with random y
            fireball = Fireball(random_x)

            #adds the instance to a group
            fireballs.add(fireball)


        #returns values
        return fireballs



    #definesa n function which checks if boss is dead
    def checkdead(self):
        
        #sets initial done to false
        cutscene = True

        #checks if the boss' health is below zero
        if self.current_health <= 0:

            #exits game loop
            cutscene = False

        #returns values
        return cutscene  

        
