#ismaeel bashir

#imports fies
import pygame
import random

#boss superclass

#creates the boss class
class Boss(pygame.sprite.Sprite):

    #creates a constructor
    def __init__(self):

        #inherits pygame sprite class
        pygame.sprite.Sprite.__init__(self)

        #sets the pygame surface of the boss
        self.image = pygame.Surface([280, 700])

        #makes the colour white transparent (gets rid of background)
        self.image.set_colorkey((255,255,255))

        #creates a rectangular area for the boss
        self.rect = self.image.get_rect()

        #sets teh x pos of the boss
        self.rect.x = 1130

        #sets the y pos
        self.rect.y = 80

        #creates a mask of the pygame surface
        self.mask = pygame.mask.from_surface(self.image)

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






    #defines a function for dealing damage
    def givedamage(self, player):

        #checks if the player is near the boss and is facing him
        if (self.rect.x-50) < player.rect.x and player.direction == "right":
            
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
                                         




    #defines a function for the boss attack
    def attack(self, Fireball, fireballs, warnings, Warning_sign):

        #gives a chance of 3 precent (per frame) for this happening
        if random.randrange(1,100) <= 3:

            #creates a random y coordinate
            random_y = random.randint(10, 600)

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


    

    #definesa n function which checks if boss is dead
    def checkdead(self):
        

        #sets initial done to false
        done = False



        #checks if the boss' health is below zero
        if self.current_health <= 0:


            #exits game loop
            done = True



        #returns values
        return done

            

