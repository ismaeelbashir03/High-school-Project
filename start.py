def start(game):

    #ismaeel bashir

    #imports files
    import pygame       
    import playerclassV3 as p  
    import portals as portal         
    import earthlevel as e          
    import waterlevel as w
    import firelevel as f
    import corruptlevel as c
    import finalbattle as fb
    import lifesource as l
    import brian as b
    import typewriter as t
    import mysql.connector
    from tiles import Tile

    # Define Classes (sprites) here

    pygame.init()                               # Pygame is initialised (starts running)

    pygame.mixer.init()                         #initialise the pygame mixer

    screenwidth = 1400        #game width defined

    screenheight = 700        #game height defined

    screen = pygame.display.set_mode([screenwidth,screenheight]) # Set the width and height of the screen [width,height]

    pygame.display.set_caption("main hub")       # Name your window

    done = False                                # Loop until the user clicks the close button.

    clock = pygame.time.Clock()                 # Used to manage how fast the screen updates

    black    = (   0,   0,   0)                 # Define some colors using rgb values.  These can be

    white    = ( 255, 255, 255)                 # used throughout the game instead of using rgb values.

    clock = pygame.time.Clock()                 #creates a var for a clock

    #sets lava to none type
    lava = None

    #sets to dt to 0
    dt = 0

    #sets time elapsed to zero
    time_elapsed = 0

    #creates var for message font
    messagefont = pygame.font.SysFont('couriernew', 20)
    
    #creates variable for each tile size
    tilesize = 20

    #creates a variable for the background image
    bg = pygame.image.load("assets/main/bgimg.jpg").convert()

    #creates group for the platforms(tiles)
    tiles = pygame.sprite.Group()

    #creates group for the player
    players = pygame.sprite.Group()

    #creates boss group
    bosses = pygame.sprite.Group()

    #creates the fireballs group
    fireballs = pygame.sprite.Group()

    #creates a group for the block
    blocks = pygame.sprite.Group()

    #creates a group for the portals
    portals = pygame.sprite.Group()

    #creates a group for the portals
    fireportals = pygame.sprite.Group()

    #creates a group for the portals
    waterportals = pygame.sprite.Group()

    #creates a group for the portals
    earthportals = pygame.sprite.Group()

    #creates group for portal
    corruptportals = pygame.sprite.Group()

    #createsa  group for brian
    brians = pygame.sprite.Group()


    #background music set as a variable
    music = "assets/main/mainbgmusic.mp3"

    #pause bool
    paused = False

    #defines fonts
    bigfont = pygame.font.Font(None, 64)
    font = pygame.font.Font(None, 36)
    smallfont = pygame.font.Font(None, 14)

    #defines player start pos
    x = 700
    y = 500

    #defines a lvl var for later use
    level = ""

    #defines a function to exit the window
    def leave():

        for event in pygame.event.get():        # Check for an event (mouse click, key press)
            if event.type == pygame.QUIT:       # If user clicked close window
                pygame.quit()                   # Flag that we are done so we exit this loop
             



    #defines a function for drawing onto the screen   
    def redrawscreen(screen, bg, player, smallfont, portalfinish):

        #blits the background image to the screen
        screen.blit(bg, [0,0])

        #draws the portals onto the screen
        portals.draw(screen)

        #draws brians image to screen
        brians.draw(screen)
        
        #draws the player onto the screen
        players.draw(screen)

        #draws the tiles to the screen
        tiles.draw(screen)

        portaltotal = portalfinish[0]+portalfinish[1]+portalfinish[2]

        if portaltotal == 0:

            #draws speech for brian
            brian.drawspeech(screen, "cmon player, lets get those orbes", player)

        if portaltotal == 1:

            #draws speech for brian
            brian.drawspeech(screen, "one down, three to go!", player)

        if portaltotal == 2:
            
            #draws speech for brian
            brian.drawspeech(screen, "the dream team, am I right!", player)

        if portaltotal == 3:

            #draws speech for brian
            brian.drawspeech(screen, "lets go beat this last champion!", player)

            

        #draws th symbol unlock image
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
        file = open("assets/main/maintilemap.csv", "r")

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
    def createlevel(level, tilesize, Tile):

        
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

        sql_portals = "SELECT earthfinish, waterfinish, firefinish, corruptfinish FROM player WHERE active = 1"

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

        #executes sql staement to get how many portals are needed
        mycursor.execute(sql_portals)


        #gets each line in cursor
        for i in mycursor:

            #adds to list every line
            portalfinish = i

        print(portalfinish)

        #commits and closes the database
        mydb.commit()
        mycursor.close()
        mydb.close()
        
        #checks if index 0 is false
        if portalfinish[0] == 0:
            
            #creates an instance of the portals
            newportal = portal.Portal(20, 580, "earth")

            #adds portal to group to be drawn
            portals.add(newportal)

            #adds the portals to a group
            earthportals.add(newportal)

        #checks if index 1 is false
        if portalfinish[1] == 0:
            
            #creates an instance of the portals
            newportal = portal.Portal(1320, 580, "water")

            #adds portal to group to be drawn
            portals.add(newportal)

            #adds the portals to a group
            waterportals.add(newportal)

        #checks if index 2 is false
        if portalfinish[2] == 0:
            
            #creates an instance of the portals
            newportal = portal.Portal(20, 420, "fire")

            #adds portal to group to be drawn
            portals.add(newportal)

            #adds the portals to a group
            fireportals.add(newportal)

        #checks if portals are all fninshed
        if portalfinish == (1,1,1,0):

            #createsa n instance of corrupt portal
            newportal = portal.Portal(1320,420, "corrupt")

            #adds portal to group
            portals.add(newportal)
            corruptportals.add(newportal)

        #sets done to false
        done = False

        #checks if index 3 is true
        if portalfinish[3] == 1:

            #sets done to true
            done = True

        #creates an instance of player
        player = p.Player(x,y)

        #adds the instance to a group
        players.add(player)

        #returns values
        return player, portals, portalfinish, done





    #drawing the level function
    def drawinglevel(tilesize, music, x, y, Tile):

        #plays background music (-1 = loop)
        pygame.mixer.music.load(music)
        pygame.mixer.music.play(-1)

        #opens the file with the tile map
        level = opentilemap()

        #draws the tiles onto the screen 
        tiles = createlevel(level,tilesize, Tile)

        #creates an instance of brian
        brian = b.Brian(750,627)

        #adds brian to group
        brians.add(brian)

        #calling the function which creates the boss
        player, portals, portalfinish, done = create(x, y)

        #returns values
        return player, tiles, portals, brian, portalfinish, done





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


            


    #main

    #calls the function to draw the level
    player, tiles, portals, brian, portalfinish, done = drawinglevel(tilesize, music, x, y, Tile)

    #gets total of portals
    portaltotal = portalfinish[0]+portalfinish[1]+portalfinish[2]+portalfinish[3]

    #checks if started new game
    if game == "new_game":
    
        #cutscene 1

        #creates message
        message = ("--you arrive on the planet and see a strange man, he approaches--",
                   "    ",
                   "stranger: ",
                   "          Hi, my name is brian. i saw you arrive on this planet.",
                   "          i opened these helpful portals for you. why? your probably wondering?",
                   "          well becuase you look quite powerful, i wonder if you can beat our planets champions.",
                   "          they each hold an elemental orb, which you can take if you manage to defeat them.",
                   "          so wanna try going against the best this planet has to offer?",
                   "                    ",
                   "                    ",
                   "          ok cool, when you defeat a champion, ill teleport you back here.",
                   "          good luck...",
                   "                    ",
                   "press SPACE to continue...")
        
        #calls function to blit message to screen
        t.typewriter(message, screen, white, clock)




    #checks if dies and if no portals are complete
    if game == "died" and portaltotal == 0:

        #creates message
        message = ("--you somehow come back to life and wake to see brian--",
                   "      ",
                   "Brian: ",
                   "       Hey player, i brought you back becuase i still think you can beat this planet's champions",
                   "       try to put a little bit more 'oomph' into it this time?",
                   "  ",
                   "press SPACE to continue..."
                   )
        
        #calls function to blit message to screeen
        t.typewriter(message, screen, white, clock)

    #checks if died and only finshed 1 portal
    if game == "died" and portaltotal == 1:

        #creates message
        message = ("--you somehow come back to life and wake to see brian--",
                   "      ",
                   "Brian: ",
                   "       Hey player, i brought you back, we already have one orb, just three more left. why not try using",
                   "       your new orb to help you defeat this champion or try going for another one to get his orb instead",
                   "       and use that orb to beat the one that just killed you.",
                   "        ",
                   "press SPACE to continue..."
                   )
        
        #calls function to blit message to screeen
        t.typewriter(message, screen, white, clock)


    #checks if dead and finished 2 portals
    if game == "died" and portaltotal == 2:

        #creates message
        message = ("--you somehow come back to life and wake to see brian--",
                   "      ",
                   "Brian: ",
                   "       Hey player, i brought you back, we are so close, just two more left. lets not get complacent.",
                   "        ",
                   "press SPACE to continue..."
                   )
        
        #calls function to blit message to screen
        t.typewriter(message, screen, white, clock)



    #checks if won and portal finish is 1
    if game == "won" and portaltotal == 1:

        #creates message
        message = ("--you are teleported back to the portal area--",
                   "     ",
                   "Brian: ",
                   "       see, i brought you back. but do make sure you have all your bones, as my teleportation is a bit rusty.",
                   "          ",
                   "--Brian laughs--",
                   "       ",
                   "--You dont laugh--",
                   "           ",
                   "       ooh nice, you have an orb, on the top left of your screen you'll see which orb you have, press the number",
                   "       below your orb to activate it...",
                   "     ",
                   "press SPACE to continue..."
                   )

        #calls functiont o blit message to screen
        t.typewriter(message, screen, white, clock)


    #checks if won and finihsed two portals
    if game == "won" and portaltotal == 2:

        #creates message
        message = ("--you are teleported back to the portal area--",
                   "     ",
                   "Brian: ",
                   "       welcome back player, that was some impressive work! just two more left. remember, 'what doesnt kill you makes",
                   "       you stronger",
                   "              ",
                   "--you ignore brian--",
                   "     ",
                   "press SPACE to continue..."
                   )

        #calls fucntiont o blit message to screen
        t.typewriter(message, screen, white, clock)


    #checks if won and finished 3 portals
    if game == "won" and portaltotal == 3:

        message = ("--you are teleported back to the portal area--",
                   "     ",
                   "Brian: ",
                   "       i opened the last portal for you player. to be honest i didnt think you would make it this far",
                   "        ",
                   "--brian laughs--",
                   "        ",
                   "       i wonder who the last champion is? ill come with you for this battle, becuase i dont think you",
                   "       can do this one on your own",
                   "           ",
                   "--you try and stop brian from coming with you becuase hes annoying but he ignores you--",
                   "              ",
                   "       ok player, lets head out!",
                   "     ",
                   "press SPACE to continue..."
                   )

        #calls function to blit message to screen
        t.typewriter(message, screen, white, clock)

        
    

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

        #calls function to check if player is hit
        player.checkhit(fireballs, lava)

        #calls elemental function
        player.elementpowers()

        #calls the open portal function
        for portal in portals:

            portal.open(player)

        #calls the pause function
        pause(screen)

        #calls function to check collision with portals
        done, level = player.portal(fireportals, waterportals, earthportals, corruptportals)


        # opens the draw screen function
        redrawscreen(screen, bg, player, smallfont, portalfinish)

        #opens the quit function
        leave()
        

    
    #opens level game loop

    #checks if level is earth
    if level == "earth":

        #fills screen to black
        screen.fill(black)

        #creates message
        message = ("Brian: ",
                   "       "
                   "Hey player, before you go, do you want me to give some advice?",
                   "         ",
                   "press SPACE to get advice or press ESCAPE to skip advice",
                   )

        #calls function to blit message to screen
        answer = t.typewriter(message, screen, white, clock)

        #checks if answer is yes
        if answer == "yes":

            #fills screen to black
            screen.fill(black)

            #creates message
            message = ("Brian: ",
                       "       ",
                       "        this champion, when hurt a certain amount, will use his orb to send",
                       "a wall of vines down.",
                       "good luck...",
                       "       ",
                       "press SPACE to continue"
                       )

            #blits messaeg
            t.typewriter(message, screen, white, clock)
                       
        #calls function to start earth level
        e.earth()

    #opens water level
    elif level == "water":

        #fills screen to black
        screen.fill(black)

        #creates message
        message = ("Brian: ",
                   "       "
                   "Hey player, before you go, do you want me to give some advice?",
                   "         ",
                   "press SPACE to get advice or press ESCAPE to skip advice",
                   )

        #blits message to screen
        answer = t.typewriter(message, screen, white, clock)

        #checks if answer is yes
        if answer == "yes":

            #fills screen to black
            screen.fill(black)

            #creates message
            message = ("Brian: ",
                       "       ",
                       "        this champion, when hurt a certain amount, will use his orb to fill",
                       "the room with water. while under water, he will attack more frequently.",
                       "i would advise you make sure don't get hit with his attack when the water leaks",
                       "back down by standing on a platform when the water leaks back down.",
                       "good luck...",
                       "       ",
                       "press SPACE to continue"
                       )

            #blits message to screen
            t.typewriter(message, screen, white, clock)

        #calls water level function
        w.water()

    #checks if fire level is chosen
    elif level == "fire":

        #fills screen to black
        screen.fill(black)

        #creates message
        message = ("Brian: ",
                   "       "
                   "Hey player, before you go, do you want me to give some advice?",
                   "         ",
                   "press SPACE to get advice or press ESCAPE to skip advice",
                   )

        #blits message to screeen
        answer = t.typewriter(message, screen, white, clock)

        #checks if answer is yes
        if answer == "yes":

            #fills screen to black
            screen.fill(black)

            #creates message
            message = ("Brian: ",
                       "       ",
                       "        this champion, immediately, will start rising lava when he sees you",
                       "try to defeat him as quick as possible to win",
                       "good luck...",
                       "       ",
                       "press SPACE to continue"
                       )
            #blits message to screen
            t.typewriter(message, screen, white, clock)

        #calls function to fire level
        f.fire()

    #checks if corruption level is chosen
    elif level == "corrupt":

        #calls corruption function
        c.corrupt()
    
    #checks if index 3 of portal finish is true
    if portalfinish[3] == 1:

        #calls function to add file to desktop
        l.create_life_source()

        #calls function to open finale level
        fb.finale()
