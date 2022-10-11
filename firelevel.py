def fire():

    #ismaeel bashir

    import pygame       # Imports pygame and other libraries

    import playerclassV3 as p  #imports the movement class

    import fireboss as b    #imports the boss class

    import fireball   #imports fireball class

    import firelava as l           #imports lava class

    import start            #imports start area

    import mysql.connector      #imports the mysql connector

    from warning import Warning_sign        #imports class for warning sign

    import file_handelling as fh        #imports file handelling file

    import insertion_sort as i          #imports standard algorithm

    from tiles import Tile              #imports tile class



    # Define Classes (sprites) here

    pygame.init()                               # Pygame is initialised (starts running)

    #records start time
    timer = pygame.time.get_ticks()
    
    pygame.mixer.init()                         #initialise the pygame mixer

    screenwidth = 1400        #game width defined

    screenheight = 700        #game height defined

    screen = pygame.display.set_mode([screenwidth,screenheight]) # Set the width and height of the screen [width,height]

    pygame.display.set_caption("fire level")       # Name your window

    done = False                                # Loop until the user clicks the close button.
    died = False
    
    clock = pygame.time.Clock()                 # Used to manage how fast the screen updates

    black    = (   0,   0,   0)                 # Define some colors using rgb values.  These can be

    white    = ( 255, 255, 255)                 # used throughout the game instead of using rgb values.

    clock = pygame.time.Clock()                 #creates a var for a clock

    #creates variable for each tile size
    tilesize = 20

    #creates a variable for the background image
    bg = pygame.image.load("assets/fire/firebg.jpg").convert()

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

    #creates a group for lava
    lavas = pygame.sprite.Group()

    #creates a group for wanrings
    warnings = pygame.sprite.Group()

    #background music set as a variable
    music = "assets/general/levelbgmusic.mp3"

    #pause bool
    paused = False

    #defines fonts
    bigfont = pygame.font.Font(None, 64)
    font = pygame.font.Font(None, 36)
    smallfont = pygame.font.Font(None, 14)

    #defines player start pos
    x = 50
    y = 100

    sql_watersave = "UPDATE player SET fireunlock = 1, firefinish = 1 WHERE active = 1"




    #defines a function to exit the window
    def leave():

        for event in pygame.event.get():        # Check for an event (mouse click, key press)
            if event.type == pygame.QUIT:       # If user clicked close window
                pygame.quit()                     # Flag that we are done so we exit this loop
      



    #defines a function for drawing onto the screen   
    def redrawscreen(screen, bg, player, smallfont):
        
        #blits the background image to the screen
        screen.blit(bg, [0,0])

        #draws the boss onto screen
        bosses.draw(screen)

        #draws the player onto the screen
        players.draw(screen)

        #draws the tiles to the screen
        tiles.draw(screen)

        #draws the fireballs on the screen
        fireballs.draw(screen)

        #draws the warning sign
        warnings.draw(screen)

        #draws the lava to the screen
        lavas.draw(screen)

        #draws the health bar of the boss
        boss.healthbar(screen)

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
        file = open("assets/fire/fireleveltilemap.csv", "r")

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

        #creates instance of boss class
        boss = b.fireBoss()

        #adds boss to group
        bosses.add(boss)

        #creates an instance of player
        player = p.Player(x, y)

        #adds the instance to a group
        players.add(player)

        #returns values
        return boss, player



    #drawing the level function
    def drawinglevel(tilesize, music, x, y):

        #plays background music (-1 = loop)
        pygame.mixer.music.load(music)
        pygame.mixer.music.play(-1)

        #opens the file with the tile map
        level = opentilemap()

        #draws the tiles onto the screen 
        tiles = createlevel(level,tilesize)

        #creates an instance of lava
        lava = l.Lava()

        #adds lava to a group
        lavas.add(lava)

        #calling the function which creates the boss
        boss, player = create(x, y)


        #returns values
        return boss, player, tiles, lava



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
            clock.tick(20)


            


    #defines main function

    #calls the function to draw the level
    boss, player, tiles, lava = drawinglevel(tilesize, music, x, y)



    #main game loop
    while done == False and died == False:
        
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

        #calls function to check if player is hit
        died = player.checkhit(fireballs, lava)

        #calls elemental function
        player.elementpowers()

        #calls the pause function
        pause(screen)
        
        #opens function that checks for giving damage
        boss.givedamage(player)

        #opens boss death check
        done = boss.checkdead()
        
        #calls the boss attack function
        fireballs, warnings = boss.attack(fireball.Fireball, fireballs, player, warnings, Warning_sign)

        #calls the warning kill function
        for warning in warnings:
            warning.kill(warnings)

        for f in fireballs:

            #calls the move function for fireballs
            f.move()

            #calls the kill function for fireballs
            f.kill(fireballs)

        #calls the lava rise function
        lava.rise()
        
        # opens the draw screen function
        redrawscreen(screen, bg, player, smallfont)

        #opens the quit function
        leave()

    #sets the reason for exit to won
    reason = "won"

    #checks if the reason player exited is bevcuase they died
    if died == True:

        #sets the reason for exit to died
        reason = "died"

        #sets dione to false
        done = False

        #loops while done is false
        while done == False:

            #checks event in pygame
            for event in pygame.event.get():

                #gets the key press event
                if event.type == pygame.KEYDOWN:

                    #checks if escape is pressed
                    if event.key == pygame.K_ESCAPE:

                        #exits loop/ makes paused False
                        done = True
           
            
                if event.type == pygame.QUIT:       # If user clicked close window

                    #quits pygame
                    pygame.quit()
                    

            #creates a var for text
            heading = bigfont.render("You Died", 1, (255,255,255))

            #creates a var for text
            message = font.render("press escape to return to the main area", 1, (255,255,255))

            #fills the screen to black
            screen.fill((0,0,0))

            #blits the text to screen
            screen.blit(heading, (10,100))
            screen.blit(message, (10,300))

            #refreshes screen and sets fps
            pygame.display.update()
            clock.tick(5)


    #checks if killed the boss
    if died == False:

        #gets players time of clearance
        player_time = float((pygame.time.get_ticks() - timer)/1000)

        #adds the players score to a list
        firescore = [player_time]

        #appends other scores from file to the list
        firescore = fh.readfilelist(firescore, "!firescore.txt")

        #sorts the list using insertion sort
        firescore = i.insertion_sort(firescore)

        #takes of the first three value from list
        firescore = firescore[:3]

        #writes the new list to the file
        fh.rewritefile("!firescore.txt", firescore)

        #creates an instacne of database connection
        mydb = mysql.connector.connect(
            host = "localhost",
            user = "root",
            passwd = "",
            charset = "utf8",
            database = "Bushi"
            )

        #creates an instance of cursor
        mycursor = mydb.cursor()

        #executes sql save statement
        mycursor.execute(sql_watersave)

        #commits and closes the database
        mydb.commit()
        mycursor.close()
        mydb.close()
        

    #takes you back to the start
    start.start(reason)





