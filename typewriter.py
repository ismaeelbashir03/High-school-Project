#ismaeel bashir

#imports files
import pygame
#typewriter pygame

#defines function to blit text to screen
def typewriter(message, screen, white, clock):

    #sets done to false
    done = False

    #sets dt to zero
    dt = 0

    #sets time elaped to zero
    time_elapsed = 0

    #sets a var for message font style 
    messagefont = pygame.font.SysFont('couriernew', 20)
    
    

    #~~typewriter~~# (prints text letter by letter)

    #loops for each line
    for index, line in enumerate(message):

        #gets each character in line
        for index2, char in enumerate(line):

            #gets time
            time_elapsed = pygame.time.get_ticks()

            #checks if 0.03 seconds has passed
            while dt+30 > time_elapsed:
        
                for event in pygame.event.get():        # Check for an event (mouse click, key press)
                    if event.type == pygame.QUIT:       # If user clicked close window
                        pygame.quit()                     # Flag that we are done so we exit this loop

                #gets time
                time_elapsed = pygame.time.get_ticks()
                
                pygame.display.flip()                   # Go ahead and update the screen with what we've drawn.
                clock.tick(60)

                
            #creates text of character
            temp_message = messagefont.render(char, 1, white)

            #blits char to screen
            screen.blit(temp_message, (index2*12, index*20))

            #records time
            dt = pygame.time.get_ticks()

    #starts loop
    while done == False:

        for event in pygame.event.get():        # Check for an event (mouse click, key press)
            if event.type == pygame.QUIT:       # If user clicked close window
                pygame.quit()                   # Flag that we are done so we exit this loop

        #gets shortcut for key press
        keys = pygame.key.get_pressed()

        #checks if space ios pressed
        if keys[pygame.K_SPACE]:

            #sets answer to yes
            answer = "yes"

            #sets done to true
            done = True

        #checks if escape id pressed
        elif keys[pygame.K_ESCAPE]:

            #sets answer to no
            answer = "no"

            #sets done to truw#e
            done = True

        pygame.display.update()
        clock.tick(20)

    #returns value
    return answer

