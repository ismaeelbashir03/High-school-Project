#createsa  function to be called when imported
def corrupt():

    #ismaeel bashir

    # Imports pygame and other libraries
    import pygame       
    import playerclassV3 as p  
    import start            
    import brian as b
    import random
    import typewriter as t
    import corruptball as c
    import lifesource as l
    import finalbattle as fb
    import finalbattle
    import mysql.connector
    import file_handelling as fh
    import insertion_sort as i
    from tiles import Tile
    


    # Define Classes (sprites) here

    pygame.init()                               # Pygame is initialised (starts running)

    #creates a var of start time
    timer = pygame.time.get_ticks()
    
    pygame.mixer.init()                         #initialise the pygame mixer

    screenwidth = 1400        #game width defined

    screenheight = 700        #game height defined

    screen = pygame.display.set_mode([screenwidth,screenheight]) # Set the width and height of the screen [width,height]

    pygame.display.set_caption("ERROR >@:!$£(){}*^4;[234265")       # Name your window

    done = False                                # Loop until the user clicks the close button.
    
    clock = pygame.time.Clock()                 # Used to manage how fast the screen updates

    black    = (   0,   0,   0)                 # Define some colors using rgb values.  These can be

    white    = ( 255, 255, 255)                 # used throughout the game instead of using rgb values.

    clock = pygame.time.Clock()                 #creates a var for a clock

    #createsa  none type var for lava
    lava = None

    #sets cutscenes to false
    cutscenes = False

    #defines text var
    text = ""

    #creates variable for each tile size
    tilesize = 20

    #creates a variable for the background image
    bg = pygame.image.load("assets/general/background.jpg").convert()

    #creates group for the platforms(tiles)
    tiles = pygame.sprite.Group()

    #creates group for the player
    players = pygame.sprite.Group()

    #creates boss group
    bosses = pygame.sprite.Group()

    #creates the fireballs group
    fireballs = pygame.sprite.Group()

    #createsa  group fro the block
    blocks = pygame.sprite.Group()

    #creates a group for brian
    brians = pygame.sprite.Group()




    #background music set as a variable
    music = "assets/corrupt/corrupt.mp3"

    #pause bool
    paused = False

    #defines fonts
    bigfont = pygame.font.Font(None, 64)
    font = pygame.font.Font(None, 36)
    smallfont = pygame.font.Font(None, 14)

    #defines player start pos
    x = 10
    y = 500

    #creates an sql statement for saving
    sql_corruptsave = "UPDATE player SET corruptfinish = 1 WHERE active = 1"



    #defines a function to exit the window
    def leave():

        for event in pygame.event.get():        # Check for an event (mouse click, key press)
            if event.type == pygame.QUIT:       # If user clicked close window
                pygame.quit()                     # Flag that we are done so we exit this loop
      



    #defines a function for drawing onto the screen   
    def redrawscreen(screen, bg, player, smallfont, brian, text, cutscenes):
        
        #blits the background image to the screen
        screen.blit(bg, [0,0])

        #draws the player onto the screen
        players.draw(screen)

        #draws the tiles to the screen
        tiles.draw(screen)

        #draws brian to screen
        brians.draw(screen)

        #draws the health bar of the boss
        brian.healthbar(screen)

        #checks if brians health has reached below 1200 and that you are not in the cutscene loop
        if brian.target_health == 1200 and cutscenes != True:

            #calls speech function
            brian.drawspeech(screen, "i see a healthbar, i wonder who the boss is?", player)

        #checks if brians health has reached below 1200 and that you are not in the cutscene loop
        elif 1100 < brian.target_health < 1200 and cutscenes != True:

            #calls speech function
            brian.drawspeech(screen, "hey stop that!", player)

        #checks if brians health has reached below 1200 and that you are not in the cutscene loop
        elif 1000 < brian.target_health < 1100 and cutscenes != True:

            #calls speech function
            brian.drawspeech(screen, "im not joking, stop!", player)

        #checks if brians health has reached below 1200 and that you are not in the cutscene loop
        elif 900 < brian.target_health < 1000 and cutscenes != True:

            #calls speech function
            brian.drawspeech(screen, "final warning!", player)

        #checks if brians y state is lowered and that you are in cutscene loop
        if brian.y_state == "lowered" and cutscenes == True:

            #calls speech function
            brian.drawspeech(screen, text, player)

        #draws the fireballs to the screen
        fireballs.draw(screen)
        
        #draws the symbol instructions
        player.hud(screen, smallfont)

        #blits the lement to screen when power chosen
        player.showelement(screen)



        
        pygame.display.flip()                   # Go ahead and update the screen with what we've drawn.
        clock.tick(20)                          # Limit to 20 frames per second




    #defines the tilemap function
    def opentilemap():

        #creates  empty 2d array
        level = []

        #opens the file with the tilemap
        file = open("assets/corrupt/corruptleveltilemap.csv", "r")

        #goes through each line in the file
        for line in file.readlines():

            #creates a temporary array to store each line
            temparray = []

            #takes away the '\n' and commas inbetwwen values as it is a csv file we are reading
            line = line[:-1].split(',')

            #goes through each value in chosen line
            for each in line:

                #adds the value to a temporary array
                temparray.append(each)

            #temporary array is then appended to the tilemap 2d array 
            level.append(temparray)

        #closes the file
        file.close()

        #returns the tilemap 2d array
        return level




    #defines a funtion to create the level
    def createlevel(level, tilesize):

        
        #goes through each tile in the group
        for each in tiles:

            #delets each tile in the group (improves performance)
            tiles.remove(each)
        
        #initially sets the x and y of the 2d array
        y = 0
        x = 0

        #goes through each row of the 2d array
        for row in level:

            #goes through each element in the row
            for element in row:

                #checks if there is a '1' in the element (code for meaning that i want ot place a tile here)
                if element == "1":

                    #creates a tile at the x and y pos of the 2d array (multiplied by the tile size as the 2d arrya is scaled down)
                    tile = Tile((x*tilesize), (y*tilesize), tilesize)

                    #adds the tile to a group
                    tiles.add(tile)

                #increments the x pos of the 2d array
                x += 1

            #resets the x pos of the 2d array
            x = 0

            #increments the y pos of the 2d array
            y += 1

        #returns values
        return tiles
        
        

    #defines a function to create the boss
    def create(x, y):

        #creates instance of brian class
        brian = b.Brian(700,625)

        #adds brian to group
        brians.add(brian)

        #creates an instance of player
        player = p.Player(x, y)

        #adds the instance to a group
        players.add(player)

        #returns values
        return brian, player



    #drawing the level function
    def drawinglevel(tilesize, music, x, y):

        #plays background music (-1 = loop)
        pygame.mixer.music.load(music)
        pygame.mixer.music.play(-1)

        #opens the file with the tile map
        level = opentilemap()

        #draws the tiles onto the screen 
        tiles = createlevel(level,tilesize)

        #calling the function which creates the boss
        brian, player = create(x, y)


        #returns values
        return brian, player, tiles

    #defines a function for the cutscene loop
    def cutscene(screen, player, bg, smallfont, brian, fireballs, Fireball):

        #initialises the paused bool 
        cutscenes = True

        #sets the players attacking state to false
        player.isattacking = False

        #creates a string var for a message
        message = ("brian: ",
                   "       well done player! you figured me out, i really wanted to toy with you for longer but oh well",
                   "       now lets see how you do against me, the champion of corruption",
                   "      ",
                   "press SPACE to continue..."
                   )

        #fills the screen black
        screen.fill(black)

        #calls the typewriter function to blit text to screeen
        t.typewriter(message, screen, white, clock)

        #creates a list of insults to player
        insults = ["you make me laugh!", "at least give me a challenge", "terrible, just terrible", "have i mentioned yet that you suck!", "--brian sleeps--", "i could do this with my eyes closed"]

        #sets lava to nonetype
        lava = None

        #defines the text var
        text = ""

        #records the time the function was called
        dt = pygame.time.get_ticks()

        #defines d2
        dt2 = 0

        #sets brians health to 1200
        brian.current_health = 1200
        brian.target_health = 1200

        #makes a pause loop
        while cutscenes == True:

            #records time for every loop
            time_elapsed = pygame.time.get_ticks()
            
            #open the movemnt function to check for movement
            player.movement()

            #open the jump function to check for jumps
            player.jump()

            #opens the attack check function
            player.attack()
            
            #opens the physics function to add gravity to the level
            player.physics()

            #opens the collision function to check for collisions
            player.collision(tiles, bosses, blocks)

            #calls the idle animation function
            player.animation()

            #calls function to check if player is hit
            died = player.checkhit(fireballs, lava)

            #calls the pause function
            pause(screen)

            #checks if 15 seconds has not passed since recorded time when function was called
            if dt+15000 > time_elapsed:

                #calls the rise function
                dt = brian.rise(dt)

                #calls brians attack function
                fireballs = brian.attack(Fireball, fireballs)

            #checks if 15 seconds has passed
            else:

                #calls the lower function
                dt, dt2, text = brian.lower(dt, dt2, time_elapsed, insults, text)
                    
                
            #calls the move function for fireballs
            c.move(fireballs, screen)

            #calls the kill function for fireballs
            c.kill(fireballs)

            #calls elemental function
            player.elementpowers()

            #opens function that checks for giving damage
            brian.givedamage(player)

            #calls the function to check if brians health is zero
            cutscenes = brian.checkdead()

            # opens the draw screen function
            redrawscreen(screen, bg, player, smallfont, brian, text, cutscenes)

            #checks if player has died
            if died == True:

                #calls the corrupt function (replays this function)
                corrupt()

            #opens the quit function
            leave()

        #creates a var for a message
        message = ("brian: ",
                   "       your stronger than i thought player...",
                   "       i guess its time for me to go all out by puttin my life source out in the open",
                   "       ",
                   "        -- use the 'wasd' keys to move and mouse to shoot and aim --"
                   "      ",
                   "press SPACE to continue..."
                   )

        #fills the screen to black
        screen.fill(black)

        #calls the typewriter function to blit text to screen
        t.typewriter(message, screen, white, clock)

        #sets done to true
        done = True

        #creates an instance of a connection to the database
        mydb = mysql.connector.connect(
            host = "localhost",
            user = "root",
            passwd = "",
            charset = "utf8",
            database = "Bushi"
            )

        #creates an instacne of cursor
        mycursor = mydb.cursor()

        #executes sql save statement
        mycursor.execute(sql_corruptsave)

        #commits the database and closes it
        mydb.commit()
        mycursor.close()
        mydb.close() 

        #returns values
        return done


        


    

    #defines pause function
    def pause(screen):

        #initialises the paused bool 
        paused = False

        #sets the keys for pressing down
        keys = pygame.key.get_pressed()

        #checks if pressing escape
        if keys[pygame.K_ESCAPE]:

            #sets pasued to true
            paused = True

        #makes a pause loop
        while paused == True:

            #checks event in pygame
            for event in pygame.event.get():

                #gets the key press event
                if event.type == pygame.KEYDOWN:

                    #checks if escape is pressed
                    if event.key == pygame.K_ESCAPE:

                        #exits loop/ makes paused False
                        paused = False
           
                    
                if event.type == pygame.QUIT:       # If user clicked close window

                    #quits pygame
                    pygame.quit()
                   
                    
            #sets the screen to black
            screen.fill((0,0,0))

            #creates a var for text
            heading = bigfont.render("Paused", 1, (255,255,255))

            #creates a var for text
            message = font.render("Press esc to resume and exit the window to quit", 1, (255,255,255))

            #blits the text to screen
            screen.blit(heading, (10,100))
            screen.blit(message, (10,300))

            #refreshes screen and sets fps
            pygame.display.update()
            clock.tick(5)


            


    #defines main function

    #calls the function to draw the level
    brian, player, tiles = drawinglevel(tilesize, music, x, y)



    #main game loop
    while done == False:
        
        #open the movemnt function to check for movement
        player.movement()

        #opens the attack check function
        player.attack()

        #open the jump function to check for jumps
        player.jump()
        
        #opens the physics function to add gravity to the level
        player.physics()

        #opens the collision function to check for collisions
        player.collision(tiles, bosses, blocks)

        #calls the idle animation function
        player.animation()

        #calls elemental function
        player.elementpowers()

        #calls the pause function
        pause(screen)

        #checks if brians health reaches below 900
        if  brian.target_health < 900:

            #starts the custscene loop
            done = cutscene(screen, player, bg, smallfont, brian, fireballs, c.Fireball)
        
        #opens function that checks for giving damage
        brian.givedamage(player)
        
        # opens the draw screen function
        redrawscreen(screen, bg, player, smallfont, brian, text, cutscenes)

        #opens the quit function
        leave()

    #gets players time of clearance
    player_time = float((pygame.time.get_ticks() - timer)/1000)

    #adds the players score to a list
    corruptscore = [player_time]

    #appends other scores from file to the list
    corruptscore = fh.readfilelist(corruptscore, "!corruptscore.txt")

    #sorts the list using insertion sort
    corruptscore = i.insertion_sort(corruptscore)

    #takes of the first three value from list
    corruptscore = corruptscore[:3]

    #writes the new list to the file
    fh.rewritefile("!corruptscore.txt", corruptscore)
        
    #calls the function to put file on desktop
    l.create_life_source()

    #calls the function to start the final battle
    fb.finale()

