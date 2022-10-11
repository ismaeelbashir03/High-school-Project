#ismaeel bashir

def main():

    #imports files
    import start
    import typewriter as t
    import file_handelling as fh

    #trys to creates saves
    try:
        import DATABASESETUP

    #if player has already made database
    except:

        print("setup already complete")

    #import mysql
    import mysql.connector

    #sets up connection with an instance
    mydb = mysql.connector.connect(
        host = "localhost",
        user = "root",
        passwd = "",
        charset = "utf8",
        database = "Bushi"
        )

    #creating a cursor
    mycursor = mydb.cursor()


    # Basic Pygame Structure

    import pygame                               # Imports pygame and other libraries

    # Define Classes (sprites) here

    pygame.init()                               # Pygame is initialised (starts running)

    screen = pygame.display.set_mode([700,500]) # Set the width and height of the screen [width,height]
    pygame.display.set_caption("main menu")       # Name your window
    done = False                                # Loop until the user clicks the close button.
    clock = pygame.time.Clock()                 # Used to manage how fast the screen updates
    black    = (   0,   0,   0)                 # Define some colors using rgb values.  These can be
    white    = ( 255, 255, 255)                 # used throughout the game instead of using rgb values.

    #sets fonts as variables
    largefont = pygame.font.SysFont("calibri", 64)
    font = pygame.font.SysFont("calibri", 42)
    smallfont = pygame.font.SysFont("couriernew", 20)


    #background music set as a variable
    music = "assets/main/mainbgmusic.mp3"

    #plays background music (-1 = loop)
    pygame.mixer.music.load(music)
    pygame.mixer.music.play(-1)


    #creates variables for text to be rendered in
    Title = largefont.render("SAMURAI", 1, (white))
    new_game = font.render("new game", 1, (white))
    load_game = font.render("load game", 1, (white))
    times = font.render("times", 1, white)

    save_3 = font.render("save 3", 1, (white))
    save_2 = font.render("save 2", 1, (white))
    save_1 = font.render("save 1", 1, (white))

    #creates var for button wodth and height
    button_width = 180
    button_height = 40

    #newgame button pos
    newgame_x = 10
    newgame_y = 200

    #load game button pos
    loadgame_x = 10
    loadgame_y = 250

    #times button pos
    times_x = 10
    times_y = 300

    #defines x and y for save 1
    save1_x = 10
    save1_y = 200

    #defines x and y for save 2
    save2_x = 10
    save2_y = 250

    #defines x and y for save 3
    save3_x = 10
    save3_y = 300

    #defines timers
    dt = 0
    time_elapsed = 0


    #creates rectangles for buttons
    newgame_rect = pygame.Rect((newgame_x, newgame_y), (button_width, button_height))
    loadgame_rect = pygame.Rect((loadgame_x, loadgame_y), (button_width, button_height))
    times_rect = pygame.Rect((times_x, times_y), (button_width, button_height))

    #creates rects for save buttons
    save1_rect = pygame.Rect((save1_x, save1_y), (button_width, button_height))
    save2_rect = pygame.Rect((save2_x, save2_y), (button_width, button_height))
    save3_rect = pygame.Rect((save3_x, save3_y), (button_width, button_height))


    # Define additional Functions and Procedures here

    # -------- Main Program Loop -----------
    while done == False:

        for event in pygame.event.get():        # Check for an event (mouse click, key press)
            if event.type == pygame.QUIT:       # If user clicked close window
                pygame.quit()                    # Flag that we are done so we exit this loop

        

        #gets mouse pos to a variable
        mouse = pygame.mouse.get_pos()

        # Update sprites here

        #fills the screen to black
        screen.fill(black)

        #draws buttons to screen
        pygame.draw.rect(screen, black, newgame_rect)
        pygame.draw.rect(screen, black, loadgame_rect)
        pygame.draw.rect(screen, black, times_rect)
        

        #creates variables for mouse clicks
        mouseclick = pygame.mouse.get_pressed()

        #checks if mouse pos os over new game button
        if newgame_x < mouse[0] < (newgame_x+button_width) and newgame_y < mouse[1] < (newgame_y+button_height):

            #draws a grey rect at button pos (gives effect of mouse hover)
            pygame.draw.rect(screen, (128,128,128), newgame_rect)

            #checks if mouse is clicked
            if mouseclick[0]:

                #sets done to True/exits loop
                done = True

                #sets the gaem type selected
                game = "new_game"

                #gets time
                dt = pygame.time.get_ticks()
            




        #checks if mouse pos is over load game button
        if loadgame_x < mouse[0] < (loadgame_x+button_width) and loadgame_y < mouse[1] < (loadgame_y+button_height):

            #draws a grey rect at button pos (gives effect of mouse hover)
            pygame.draw.rect(screen, (128,128,128), loadgame_rect)

            #checks if mouse is clicked
            if mouseclick[0]:

                #sets done to True/exits loop
                done = True

                #sets the gaem type selected
                game = "load_game"

                #gets time
                dt = pygame.time.get_ticks()


        #checks if mouse pos is over times button
        if times_x < mouse[0] < (times_x+button_width) and times_y < mouse[1] < (times_y+button_height):

            #draws a grey rect at button pos (gives effect of mouse hover)
            pygame.draw.rect(screen, (128,128,128), times_rect)

            #checks if mouse is clicked
            if mouseclick[0]:

                #sets done to True/exits loop
                done = True

                #sets the gaem type selected
                game = "times"

                #gets time
                dt = pygame.time.get_ticks()

                

        #blits the title ot the screen
        screen.blit(Title, [10, 10])

        #blits the new game text to screen
        screen.blit(new_game, [10, 200])

        #blits the load game text to screen
        screen.blit(load_game, [10, 250])

        #blits the times text to screen
        screen.blit(times, [10, 300])

        

        
        pygame.display.flip()                   # Go ahead and update the screen with what we've drawn.
        clock.tick(20)                          # Limit to 20 frames per second



    #cretaes sql statements for new saves and loading in
    sql_savechoice = "UPDATE player SET active = %s WHERE save = %s"
    sql_newsave = "UPDATE player SET earthunlock = 0, waterunlock = 0, fireunlock = 0, earthfinish = 0, waterfinish = 0, firefinish = 0, corruptfinish = 0 WHERE active = 1"




    #checks if button chosen was times
    if game == "times":

        #sets typed to initally not done
        typed = "not_done"

        #defines lists for storing scores
        earthscore = []
        firescore = []
        waterscore = []
        corruptscore = []
        finalescore = []

        #reads scores from files
        earthscore = fh.readfilelist(earthscore, "!earthscore.txt")
        firescore = fh.readfilelist(firescore, "!firescore.txt")
        waterscore = fh.readfilelist(waterscore, "!waterscore.txt")
        corruptscore = fh.readfilelist(corruptscore, "!corruptscore.txt")
        finalescore = fh.readfilelist(finalescore, "!finalescore.txt")

        
        #sets done to false
        done = False

        while done == False:

            for event in pygame.event.get():        # Check for an event (mouse click, key press)
                if event.type == pygame.QUIT:       # If user clicked close window
                    main()

            #checks if screen has not yet typed
            if typed == "not_done":

                #fills the screen to black
                screen.fill(black)

                #creates a message for scoreboard
                message = ("--fastest clearance of each level--",
                           "         ",
                           "earth level: ",
                           "             1. "+str(earthscore[0]),
                           "             2. "+str(earthscore[1]),
                           "             3. "+str(earthscore[2]),
                           "water level: ",
                           "             1. "+str(waterscore[0]),
                           "             2. "+str(waterscore[1]),
                           "             3. "+str(waterscore[2]),
                           "fire level: ",
                           "             1. "+str(firescore[0]),
                           "             2. "+str(firescore[1]),
                           "             3. "+str(firescore[2]),
                           "corrupt level: ",
                           "             1. "+str(corruptscore[0]),
                           "             2. "+str(corruptscore[1]),
                           "             3. "+str(corruptscore[2]),
                           "finale level: ",
                           "             1. "+str(finalescore[0]),
                           "             2. "+str(finalescore[1]),
                           "             3. "+str(finalescore[2]),
                           "      ",
                           "press ESCAPE or SPACE to return to main menu...")

                #calls a function to blit text to screen
                answer = t.typewriter(message, screen, white, clock)

                #sets typed to done
                typed = "done"
                
                #checks if answer is no
                if answer == "no":

                    #calls the main function (replays this function)
                    main()

                #checks if answer is yes
                elif answer == "yes":

                    #calls the main function
                    main()
            
            pygame.display.flip()                   # Go ahead and update the screen with what we've drawn.
            clock.tick(20)


            


    #checks if button chosen was not times
    if game != "times":
            
        #sets done
        done = False

        #starts loop
        while done == False:



            for event in pygame.event.get():        # Check for an event (mouse click, key press)
                if event.type == pygame.QUIT:       # If user clicked close window
                    main()


            #gets mouse pos to a variable
            mouse = pygame.mouse.get_pos()

            #creates variables for mouse clicks
            mouseclick = pygame.mouse.get_pressed()

            #fills the screen black
            screen.fill(black)

            #draws buttons to screen
            pygame.draw.rect(screen, black, save1_rect)
            pygame.draw.rect(screen, black, save2_rect)
            pygame.draw.rect(screen, black, save3_rect)


            #gets the time
            time_elapsed = pygame.time.get_ticks()


            #checks if mouse pos os over new game button
            if save1_x < mouse[0] < (save1_x+button_width) and save1_y < mouse[1] < (save1_y+button_height):
                

                #draws a grey rect at button pos (gives effect of mouse hover)
                pygame.draw.rect(screen, (128,128,128), save1_rect)

                #checks if mouse is clicked
                if mouseclick[0] and dt+500 < time_elapsed:
                    
                    #creates a list for save activation
                    savelist = [[1,1], [0,2], [0,3]]

                    #executes sql statements to set active save
                    mycursor.executemany(sql_savechoice, savelist)

                    #checks if selected new game
                    if game == "new_game":
                        
                        #executes sql to create new save
                        mycursor.execute(sql_newsave)

                    #commits and closes database
                    mydb.commit()
                    mycursor.close()
                    mydb.close()

                    #sets done to true
                    done = True


            #checks if mouse pos is over load game button
            if save2_x < mouse[0] < (save2_x+button_width) and save2_y < mouse[1] < (save2_y+button_height):

                #draws a grey rect at button pos (gives effect of mouse hover)
                pygame.draw.rect(screen, (128,128,128), save2_rect)

                #checks if mouse is clicked
                if mouseclick[0] and  dt+500 < time_elapsed:

                    #creates a asave list for activation
                    savelist = [(0,1), (1,2), (0,3),]

                    #executes sql statements to set active save
                    mycursor.executemany(sql_savechoice, savelist)

                    #checks if selected new game
                    if game == "new_game":

                        #execurtes sql statement for new save
                        mycursor.execute(sql_newsave)

                    #commits and closes database
                    mydb.commit()
                    mycursor.close()
                    mydb.close()

                    #sets done to true
                    done = True


            #checks if mouse pos is over load game button
            if save3_x < mouse[0] < (save3_x+button_width) and save3_y < mouse[1] < (save3_y+button_height):

                #draws a grey rect at button pos (gives effect of mouse hover)
                pygame.draw.rect(screen, (128,128,128), save3_rect)

                #checks if mouse is clicked
                if mouseclick[0] and  dt+500 < time_elapsed:

                    #creates a save list for activation
                    savelist = [[0,1], [0,2], [1,3]]

                    #executes sql statements to set active save
                    mycursor.executemany(sql_savechoice, savelist)

                    #checks if selected new game 
                    if game == "new_game":

                        #executes sql statement to make new save
                        mycursor.execute(sql_newsave)

                    #commits and closes database
                    mydb.commit()
                    mycursor.close()
                    mydb.close()

                    #sets done to true
                    done = True


            

            #blits the title ot the screen
            screen.blit(save_1, [10, 200])

            #blits the new game text to screen
            screen.blit(save_2, [10, 250])

            #blits the load game text to screen
            screen.blit(save_3, [10, 300])
            


            pygame.display.flip()                   # Go ahead and update the screen with what we've drawn.
            clock.tick(20)


        #checks if player selected new save
        if game == "new_game":

            #creates message for new game
            message = ("As you arrive to this planet, you sense the presence",
                      "of the elmental orbes. The last thing you need to",
                       "declare yourself as the most powerful samurai...",
                       "                                                ",
                       "on this planet your movement seems strange...",
                       "to run left you have to press 'a' and to run",
                       "right you have to press 'd'...",
                       "                                                ",
                       "the gravity of this planet has also taken a toll",
                       "on you, you can now only jump with the 'spacebar'",
                       "and attack with 'e'..."
                       "                                                ",
                       "                                                ",
                       "press SPACE to continue...."
                       
                       )
            #fills the screen to black
            screen.fill(black)

            #calls the typewriter function to blit text to screen
            t.typewriter(message, screen, white, clock)



        #calls the start area
        start.start(game)

#calls the main function
main()
