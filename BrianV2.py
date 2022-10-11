#ismaeel bashir

#imports files
import pygame

#brian phase 2

#creates a class for brian in his seocnd phase
class BrianV2():

    #creates a constructor
    def __init__(self):

        #sets an intial value for current health
        self.current_health = 8000

        #sets the initial value for the targeted health
        self.target_health = 8000

        #creates a max health var
        self.max_health = 8000

        #creates a var for the legnth of the health bar
        self.healthbar_legnth = 1200

        #creates a var for the speed in which the current hea;th will catch up to the targeted health
        self.health_changespeed = 20

        #creates a var for the healthbar ratio (keeps healthbar legnth correct)
        self.health_ratio = self.max_health / self.healthbar_legnth
    

    #creates a function for checking brians health
    def check_health(self, health):

        #sets the target health to all the mobs health totaled (which has been passed in)
        self.target_health = health
        

    #defines a function for checking if brians health is at 0
    def checkdead(self):

        #initially sets done to false
        done = False

        #che checks if brians health is below or equal to zero
        if self.current_health <= 0:

            #sets done to true
            done = True

        #returns values
        return done


    #finale healthbar

    #defines a function which creates the health bar
    def healthbar(self, screen):
        
        #sets an initial width for the animated health
        transition_width = 0

        #sets an initial colour for the animated health
        transition_colour = (255, 0, 0)

        #chekcs if target health is below zero
        if self.target_health < 0:

            #makes target health zero
            self.target_health = 0

        #checks if the targeted health is smaller than the current health
        if self.current_health > self.target_health:

            #increments the current health to reach the targeted health
            self.current_health -= self.health_changespeed

            #sets the health animation width (how big it is supposed to be)
            transition_width = int((self.target_health - self.current_health)/self.health_ratio)

            #sets the colour of the health animation 
            transition_colour = (255, 255, 0)

        #creates a rectangle for the health bar with the current health
        healthbar_rect = pygame.Rect((100, 10, self.current_health/self.health_ratio, 25))

        #creates a rectangle for the health which is going to be animated
        transitionbar_rect = pygame.Rect((healthbar_rect.right, 10, transition_width, 25))

        #draws the health bar with current health
        pygame.draw.rect(screen,(255, 0, 0), healthbar_rect)

        #draws the health bar with the animated health
        pygame.draw.rect(screen, transition_colour, transitionbar_rect)

        #draws an outline for the health
        pygame.draw.rect(screen, (0,0,0), (100, 10, self.healthbar_legnth, 25), 4)

