import turtle
import random

def translate_coordinates(number, letter):
    translatedCoordinates = []
    if letter == "a" or letter == "k":
        y = 185
    elif letter == "b" or letter == "l":
        y = 135
    elif letter == "c" or letter == "m":
        y = 85
    elif letter == "d" or letter == "n":
        y = 35
    elif letter == "e" or letter == "o":
        y = -15
    elif letter == "f" or letter == "p":
        y = -65
    elif letter == "g" or letter == "q":
        y = -115
    elif letter == "h" or letter == "r":
        y = -165
    elif letter == "i" or letter == "s":
        y = -215
    elif letter == "j" or letter == "t":
        y = -265
    if number == "1":
        x = -500
    elif number == "2":
        x = -450
    elif number == "3":
        x = -400
    elif number == "4":
        x = -350
    elif number == "5":
        x = -300
    elif number == "6":
        x = -250
    elif number == "7":
        x = -200
    elif number == "8":
        x = -150
    elif number == "9":
        x = -100
    elif number == "10":
        x = -50
    elif number == "11":
        x = 50
    elif number == "12":
        x = 100
    elif number == "13":
        x = 150
    elif number == "14":
        x = 200
    elif number == "15":
        x = 250
    elif number == "16":
        x = 300
    elif number == "17":
        x = 350
    elif number == "18":
        x = 400
    elif number == "19":
        x = 450
    elif number == "20":
        x = 500
    translatedCoordinates.append(x)
    translatedCoordinates.append(y)
    return translatedCoordinates
    
        
def draw_ship(turtle, screen, shipType):
    """Draws a ship and returns a list with its coordinates"""
    xCoordinateListUser = ["1", "2", "3", "4", "5", "6", "7", "8", "9", "10"]
    yCoordinateListUser = ["a", "b", "c", "d", "e", "f", "g", "h", "i", "j"]
    if shipType == "Aircraft Carrier":
        blockLength = 5
        screenLimit = 6
    elif shipType == "Battleship":
        blockLength = 4
        screenLimit = 7
    elif shipType == "Submarine":
        blockLength = 3
        screenLimit = 8
    elif shipType == "Destroyer":
        blockLength = 3
        screenLimit = 8
    elif shipType == "Patrol":
        blockLength = 2
        screenLimit = 9

    orientation = screen.textinput("{0}".format(shipType), "The {0} is {1} blocks long, would you like it 'vertical' (v) or 'horizontal' (h)?".format(shipType,blockLength)).lower()
    turtle.color("black", "gray")

    if orientation == "vertical" or orientation == "v":
        topMostBlockX = "21"
        topMostBlockY = "u"
        while topMostBlockX not in xCoordinateListUser or topMostBlockY not in yCoordinateListUser[0:screenLimit]:
            topMostBlockX = screen.textinput("{0}".format(shipType), "What NUMERIC coordinate would you like the TOP block of this ship to be on?").lower()
            topMostBlockY = screen.textinput("{0}".format(shipType), "What LETTER coordinate would you like the TOP block of this ship to be on?").lower()
            if topMostBlockX not in xCoordinateListUser or topMostBlockY not in yCoordinateListUser[0:screenLimit]:
                if topMostBlockX not in xCoordinateListUser:
                    message = screen.textinput("{0}".format(shipType), "Your NUMERIC coordinate was invalid. Press 'enter' to try again.")
                if topMostBlockY not in yCoordinateListUser[0:screenLimit]:
                    if topMostBlockY in yCoordinateListUser[screenLimit:10]:
                        message = screen.textinput("{0}".format(shipType), "Your {0} would be out of bounds. Remember it is {1} blocks long. Press 'enter' to try again.".format(shipType, blockLength))
                    elif topMostBlockY not in yCoordinateListUser:
                        message = screen.textinput("{0}".format(shipType), "Your LETTER coordinate was invalid. Press 'enter' to try again.")
        coordinates = translate_coordinates(topMostBlockX, topMostBlockY)
        turtle.penup()
        turtle.setposition(coordinates[0]-25, coordinates[1]+25)
        turtle.pendown()
        turtle.begin_fill()
        for i in range(2):
            turtle.forward(50)
            turtle.right(90)
            turtle.forward(50*blockLength)
            turtle.right(90)
        turtle.end_fill()
        turtle.penup()
        shipLocation = []
        whichWay = [orientation]
        for i in yCoordinateListUser[yCoordinateListUser.index(topMostBlockY):yCoordinateListUser.index(topMostBlockY)+blockLength]:
            coordinate = "{0}{1}".format(topMostBlockX, i)
            shipLocation.append(coordinate)
        return shipLocation + whichWay
        
    elif orientation == "horizontal" or orientation == "h":
        leftMostBlockX = "21"
        leftMostBlockY = "u"
        while leftMostBlockX not in xCoordinateListUser[0:screenLimit] or leftMostBlockY not in yCoordinateListUser:
            leftMostBlockX = screen.textinput("{0}".format(shipType), "What NUMERIC coordinate would you like the LEFT-MOST block of this ship to be on?").lower()
            leftMostBlockY = screen.textinput("{0}".format(shipType), "What LETTER coordinate would you like the LEFT-MOST block of this ship to be on?").lower()
            if leftMostBlockX not in xCoordinateListUser[0:screenLimit] or leftMostBlockY not in yCoordinateListUser:
                if leftMostBlockX not in xCoordinateListUser[0:screenLimit]:
                    if leftMostBlockX in xCoordinateListUser[screenLimit:10]:
                        message = screen.textinput("{0}".format(shipType), "Your {0} would be out of bounds. Remember it is {1} blocks long. Press 'enter' to try again.".format(shipType, blockLength))
                    elif leftMostBlockX not in xCoordinateListUser:
                        message = screen.textinput("{0}".format(shipType), "Your NUMERIC coordinate was invalid. Press 'enter' to try again.")
                if leftMostBlockY not in xCoordinateListUser:
                    message = screen.textinput("{0}".format(shipType), "Your LETTER coordinate was invalid. Press 'enter' to try again.")
        coordinates = translate_coordinates(leftMostBlockX, leftMostBlockY)
        turtle.penup()
        turtle.setposition(coordinates[0]-25, coordinates[1]+25)
        turtle.pendown()
        turtle.begin_fill()
        for i in range(2):
            turtle.forward(50*blockLength)
            turtle.right(90)
            turtle.forward(50)
            turtle.right(90)
        turtle.end_fill()
        turtle.penup()
        shipLocation = []
        whichWay = [orientation]
        for i in xCoordinateListUser[xCoordinateListUser.index(leftMostBlockX):xCoordinateListUser.index(leftMostBlockX)+blockLength]:
            coordinate = "{0}{1}".format(i, leftMostBlockY)
            shipLocation.append(coordinate)
        return shipLocation + whichWay

    elif orientation != "vertical" and orientation != "horizontal":
        message = screen.textinput("Orientation", "Your input was INVALID for the ORIENTATION of the ship, press 'enter' to try again.")
        return draw_ship(turtle, screen, shipType)

def enemy_ship(shipType):
    """"Creates enemy's ships to be guessed."""
    xCoordinateListOpponent = ["11", "12", "13", "14", "15", "16", "17", "18", "19", "20"]
    yCoordinateListOpponent = ["k", "l", "m", "n", "o", "p", "q", "r", "s", "t"]
    if shipType == "Aircraft Carrier":
        blockLength = 5
        screenLimit = 6
    elif shipType == "Battleship":
        blockLength = 4
        screenLimit = 7
    elif shipType == "Submarine":
        blockLength = 3
        screenLimit = 8
    elif shipType == "Destroyer":
        blockLength = 3
        screenLimit = 8
    elif shipType == "Patrol":
        blockLength = 2
        screenLimit = 9
        
    orientationList = ["vertical", "horizontal"]
    orientation = orientationList[random.randint(0,1)]

    if orientation == "vertical":
        topMostBlockX = "21"
        topMostBlockY = "u"
        while topMostBlockX not in xCoordinateListOpponent or topMostBlockY not in yCoordinateListOpponent[0:screenLimit]:
            topMostBlockX = xCoordinateListOpponent[random.randint(0,9)]
            topMostBlockY = yCoordinateListOpponent[random.randint(0,screenLimit-1)]
        shipLocation = []
        for i in yCoordinateListOpponent[yCoordinateListOpponent.index(topMostBlockY):yCoordinateListOpponent.index(topMostBlockY)+blockLength]:
            coordinate = "{0}{1}".format(topMostBlockX, i)
            shipLocation.append(coordinate)
        return shipLocation

    elif orientation  == "horizontal":
        leftMostBlockX = "21"
        leftMostBlockY = "u"
        while leftMostBlockX not in xCoordinateListOpponent[0:screenLimit] or leftMostBlockY not in yCoordinateListOpponent:
            leftMostBlockX = xCoordinateListOpponent[random.randint(0, screenLimit-1)]
            leftMostBlockY = yCoordinateListOpponent[random.randint(0,9)]
        shipLocation = []
        for i in xCoordinateListOpponent[xCoordinateListOpponent.index(leftMostBlockX):xCoordinateListOpponent.index(leftMostBlockX)+blockLength]:
            coordinate = "{}{}".format(i, leftMostBlockY)
            shipLocation.append(coordinate)
        return shipLocation

#**********************************************************************************************************************
#This section of code sets up the graphics screen of the game.
        
gameWindow = turtle.Screen()
gameWindow.title("BattleShip")
gameWindow.setup(width=1.0, height=1.0, startx=None, starty=None)
gameWindow.screensize(1000, 500, 'light blue')


pegPoints = turtle.Turtle()
pegPoints.hideturtle()
pegPoints.shape("circle")
pegPoints.penup()
pegPoints.speed(0)

pegPoints.setposition(-275, 300)
pegPoints.write("Your Ships", align = 'center', font = ('Arial', 24, 'bold'))

pegPoints.setposition(-500, 225)
for i in range(1,11):
    pegPoints.write(i, align = 'center', font = ('Arial', 24, 'normal'))
    pegPoints.forward(50)
    
pegPoints.setposition(-550, 170)
index = 0
for i in ["A", "B", "C", "D", "E", "F", "G", "H", "I", "J"]:
    pegPoints.write(i, align = 'center', font = ('Arial', 24, 'normal'))
    index = index + 1
    pegPoints.setposition(-550, 170-(50*index))
    
pegPoints.setposition(-500, 185)
for i in range(10):
    for j in range(10):
        pegPoints.dot(5, 'black')
        pegPoints.forward(50)
    pegPoints.setposition(-500, 185-(50*(i+1)))

pegPoints.setposition(275, 300)
pegPoints.write("Opponent's Ships", align = 'center', font = ('Arial', 24, 'bold'))
    
pegPoints.setposition(50, 225)
for i in range(11,21):
    pegPoints.write(i, align = 'center', font = ('Arial', 24, 'normal'))
    pegPoints.forward(50)

pegPoints.setposition(550, 170)
index = 0
for i in ["K", "L", "M", "N", "O", "P", "Q", "R", "S", "T"]:
    pegPoints.write(i, align = "center", font = ('Arial', 24, 'normal'))
    index = index + 1
    pegPoints.setposition(550, 170-(50*index))

pegPoints.setposition(50, 185)
for i in range(10):
    for j in range(10):
        pegPoints.dot(5, 'black')
        pegPoints.forward(50)
    pegPoints.setposition(50, 185-(50*(i+1)))

pegPoints.setposition(0, 250)
pegPoints.pendown()
pegPoints.right(90)
pegPoints.forward(550)
pegPoints.penup()
pegPoints.left(90)

print("WELCOME TO BATTLESHIP")
print("IF YOU ALREADY KNOW HOW TO PLAY...")
print("     Go ahead and click on the game window to continue.")
print("OBJECT OF THE GAME")
print("     The goal of this game is to sink all of the computer's ships.")
print("     You won't be able to see where their ships are, so you will on a turn-by-turn basis")
print("     with the computer fire at each other's ships by guessing at the alpha-numeric coordinates.")
print("     Once either you or the opponents ships are sunk, the game ends.")
print("HOW TO PLAY")
print("     1. All inputs in this game will be through the keyboard.")
print("     2. Both you and the computer will have 5 different ships of varying sizes.")
print("          1. Aircraft Carrier - 5 blocks long")
print("          2. Battleship - 4 blocks long")
print("          3. Submarine - 3 blocks long")
print("          4. Destroyer - 3 blocks long")
print("          5. Patrol - 2 blocks long")
print("     3. You will begin by placing your ships across your coordinate grid (1-10, A-J).")
print("        Be careful to enter valid inputs and not to overlap your ships.")
print("     4. When firing at the computer's ships, make sure to use their coordinate grid (11-20, K-T).")
print("     5. A succesful hit is colored RED and a miss is colored BLUE.")
print("     6. If a hit is succesful on either side, whoever made a correct guess immedietly gets another turn.")
print("WARNING")
print("     Avoid exiting out of message screens in the gamewindow, doing so may cause game to freeze.")
wantPlay = True
while wantPlay == True:

#**********************************************************************************************************
#This section of code creates indiviual turtles for each of the users ships, and the missle.

    airCraftCarrier = turtle.Turtle()
    airCraftCarrier.hideturtle()
    airCraftCarrier
    airCraftCarrier.speed(0)
    battleShip = turtle.Turtle()
    battleShip.hideturtle()
    battleShip.speed(0)
    submarine = turtle.Turtle()
    submarine.hideturtle()
    submarine.speed(0)
    destroyer = turtle.Turtle()
    destroyer.hideturtle()
    destroyer.speed(0)
    patrol = turtle.Turtle()
    patrol.hideturtle()
    patrol.speed(0)
    missle = turtle.Turtle()
    missle.hideturtle()
    missle.shape("circle")
    missle.speed(0)
    missle.penup()

#**********************************************************************************************************
#This section of code creates the actual ships of the user and makes sure they don't overlap.

    activeCoordinates = []
    verticalCount = 0
    horizontalCount = 0

    userAirCraftCarrier = [""]
    while userAirCraftCarrier[0] not in activeCoordinates:
        uACC = draw_ship(airCraftCarrier, gameWindow, "Aircraft Carrier")
        userAirCraftCarrier = uACC[0:len(uACC)-1]
        temporaryCoordinates = []
        sendMessage = False
        for coordinate in userAirCraftCarrier:
            if coordinate in activeCoordinates:
                airCraftCarrier.clear()
                userAirCraftCarrier = [""]
                if sendMessage == False:
                    message = gameWindow.textinput("Aircraft Carrier", "The ship would OVERLAP with another ship. Press any key to try again.")
                    sendMessage = True
            elif coordinate not in activeCoordinates:
                temporaryCoordinates.append(coordinate)
                if temporaryCoordinates == userAirCraftCarrier:
                    activeCoordinates = activeCoordinates + userAirCraftCarrier
    if uACC[len(uACC)-1] == "vertical":
        verticalCount = verticalCount + 1
    elif uACC[len(uACC)-1] == "horizontal":
        horizontalCount = horizontalCount + 1

    userBattleShip = [""]
    while userBattleShip[0] not in activeCoordinates:
        uBS = draw_ship(battleShip, gameWindow, "Battleship")
        userBattleShip = uBS[0:len(uBS)-1]
        temporaryCoordinates = []
        sendMessage = False
        for coordinate in userBattleShip:
            if coordinate in activeCoordinates:
                battleShip.clear()
                userBattleShip = [""]
                if sendMessage == False:
                    message = gameWindow.textinput("BattleShip", "The ship would OVERLAP with another ship. Press any key to try again.")
                    sendMessage = True
            elif coordinate not in activeCoordinates:
                temporaryCoordinates.append(coordinate)
                if temporaryCoordinates == userBattleShip:
                    activeCoordinates = activeCoordinates + userBattleShip
    if uBS[len(uBS)-1] == "vertical":
        verticalCount = verticalCount + 1
    elif uBS[len(uBS)-1] == "horizontal":
        horizontalCount = horizontalCount + 1

    userSubmarine = [""]
    while userSubmarine[0] not in activeCoordinates:
        uS = draw_ship(submarine, gameWindow, "Submarine")
        userSubmarine = uS[0:len(uS)-1]
        temporaryCoordinates = []
        sendMessage = False
        for coordinate in userSubmarine:
            if coordinate in activeCoordinates:
                submarine.clear()
                userSubmarine = [""]
                if sendMessage == False:
                    message = gameWindow.textinput("Submarine", "The ship would OVERLAP with another ship. Press any key to try again.")
                    sendMessage = True
            elif coordinate not in activeCoordinates:
                temporaryCoordinates.append(coordinate)
                if temporaryCoordinates == userSubmarine:
                    activeCoordinates = activeCoordinates + userSubmarine
    if uS[len(uS)-1] == "vertical":
        verticalCount = verticalCount + 1
    elif uS[len(uS)-1] == "horizontal":
        horizontalCount = horizontalCount + 1
    

    userDestroyer = [""]
    while userDestroyer[0] not in activeCoordinates:
        uD = draw_ship(destroyer, gameWindow, "Destroyer")
        userDestroyer = uD[0:len(uD)-1]
        temporaryCoordinates = []
        sendMessage = False
        for coordinate in userDestroyer:
            if coordinate in activeCoordinates:
                destroyer.clear()
                userDestroyer = [""]
                if sendMessage == False:
                    message = gameWindow.textinput("Destroyer", "The ship would OVERLAP with another ship. Press any key to try again.")
                    sendMessage = True
            elif coordinate not in activeCoordinates:
                temporaryCoordinates.append(coordinate)
                if temporaryCoordinates == userDestroyer:
                    activeCoordinates = activeCoordinates + userDestroyer
    if uD[len(uD)-1] == "vertical":
        verticalCount = verticalCount + 1
    elif uD[len(uD)-1] == "horizontal":
        horizontalCount = horizontalCount + 1
                    
    userPatrol = [""]
    while userPatrol[0] not in activeCoordinates:
        uP = draw_ship(patrol, gameWindow, "Patrol")
        userPatrol = uP[0:len(uP)-1]
        temporaryCoordinates = []
        sendMessage = False
        for coordinate in userPatrol:
            if coordinate in activeCoordinates:
                patrol.clear()
                userPatrol = [""]
                if sendMessage == False:
                    message = gameWindow.textinput("Patrol", "The ship would OVERLAP with another ship. Press any key to try again.")
                    sendMessage = True
            elif coordinate not in activeCoordinates:
                temporaryCoordinates.append(coordinate)
                if temporaryCoordinates == userPatrol:
                    activeCoordinates = activeCoordinates + userPatrol
    if uP[len(uP)-1] == "vertical":
        verticalCount = verticalCount + 1
    elif uP[len(uP)-1] == "horizontal":
        horizontalCount = horizontalCount + 1

#***********************************************************************************************************
#This section of code creates the computer's "boats" and makes sure they don't overlap.

    enemyActiveCoordinates = []

    opponentAirCraftCarrier = ["filler"]
    while opponentAirCraftCarrier[0] not in enemyActiveCoordinates:
        opponentAirCraftCarrier = enemy_ship("Aircraft Carrier")
        temporaryCoordinates = []
        for coordinate in opponentAirCraftCarrier:
            if coordinate in enemyActiveCoordinates:
                opponentAirCraftCarrier = ["filler"]
            elif coordinate not in enemyActiveCoordinates:
                temporaryCoordinates.append(coordinate)
                if temporaryCoordinates == opponentAirCraftCarrier:
                    enemyActiveCoordinates = enemyActiveCoordinates + opponentAirCraftCarrier

    opponentBattleShip = ["filler"]
    while opponentBattleShip[0] not in enemyActiveCoordinates:
        opponentBattleShip = enemy_ship("Battleship")
        temporaryCoordinates = []
        for coordinate in opponentBattleShip:
            if coordinate in enemyActiveCoordinates:
                opponentBattleShip = ["filler"]
            elif coordinate not in enemyActiveCoordinates:
                temporaryCoordinates.append(coordinate)
                if temporaryCoordinates == opponentBattleShip:
                    enemyActiveCoordinates = enemyActiveCoordinates + opponentBattleShip

    opponentSubmarine = ["filler"]
    while opponentSubmarine[0] not in enemyActiveCoordinates:
        opponentSubmarine = enemy_ship("Submarine")
        temporaryCoordinates = []
        for coordinate in opponentSubmarine:
            if coordinate in enemyActiveCoordinates:
                opponentSubmarine = ["filler"]
            elif coordinate not in enemyActiveCoordinates:
                temporaryCoordinates.append(coordinate)
                if temporaryCoordinates == opponentSubmarine:
                    enemyActiveCoordinates = enemyActiveCoordinates + opponentSubmarine

    opponentDestroyer = ["filler"]
    while opponentDestroyer[0] not in enemyActiveCoordinates:
        opponentDestroyer = enemy_ship("Destroyer")
        temporaryCoordinates = []
        for coordinate in opponentDestroyer:
            if coordinate in enemyActiveCoordinates:
                opponentDestroyer = ["filler"]
            elif coordinate not in enemyActiveCoordinates:
                temporaryCoordinates.append(coordinate)
                if temporaryCoordinates == opponentDestroyer:
                    enemyActiveCoordinates = enemyActiveCoordinates + opponentDestroyer

    opponentPatrol = ["filler"]
    while opponentPatrol[0] not in enemyActiveCoordinates:
        opponentPatrol = enemy_ship("Patrol")
        temporaryCoordinates = []
        for coordinate in opponentPatrol:
            if coordinate in enemyActiveCoordinates:
                opponentPatrol = ["filler"]
            elif coordinate not in enemyActiveCoordinates:
                temporaryCoordinates.append(coordinate)
                if temporaryCoordinates == opponentPatrol:
                    enemyActiveCoordinates = enemyActiveCoordinates + opponentPatrol

##    print(activeCoordinates)
##    print(enemyActiveCoordinates)

#*************************************************************************************************************
#This section of code facilitates the actual gameplay.

    userTurn = True
    computerTurn = False
    userGuesses = []
    computerGuesses = []

    xCoordinateListUser = ["1", "2", "3", "4", "5", "6", "7", "8", "9", "10"] 
    yCoordinateListUser = ["a", "b", "c", "d", "e", "f", "g", "h", "i", "j"]
    xCoordinateListOpponent = ["11", "12", "13", "14", "15", "16", "17", "18", "19", "20"]
    yCoordinateListOpponent = ["k", "l", "m", "n", "o", "p", "q", "r", "s", "t"]

    while userTurn == True or computerTurn == True:
        if userTurn == True and computerTurn == False:
            compareCoordinates = "filler"
            userGuessX = "filler"
            userGuessY = "filler"
            while userGuessX not in xCoordinateListOpponent or userGuessY not in yCoordinateListOpponent or compareCoordinates in userGuesses:
                userGuessX = gameWindow.textinput("User attack!", "What NUMERIC coordinate would you like to shoot?")
                userGuessY = gameWindow.textinput("User attack!", "What LETTER coordinate would you like to shoot?")
                compareCoordinates = "{0}{1}".format(userGuessX,userGuessY)
                if userGuessX not in xCoordinateListOpponent or userGuessY not in yCoordinateListOpponent:
                    if userGuessX not in xCoordinateListOpponent and userGuessY in yCoordinateListOpponent:
                        message = gameWindow.textinput("Error","Your NUMERIC input was invalid, press 'enter' to try again.")
                    elif userGuessX in xCoordinateListOpponent and userGuessY not in yCoordinateListOpponent:
                        message = gameWindow.textinput("Error","Your LETTER input was invalid, press 'enter' to try again.")
                    else:
                        message = gameWindow.textinput("Error","Both of your inputs were invalid, press 'enter' to try again.")
                        
                if compareCoordinates in userGuesses:
                    message = gameWindow.textinput("Error", "You've already shot there!")
            userGuesses.append(compareCoordinates)
            coordinates = translate_coordinates(userGuessX, userGuessY)
            missle.setposition(coordinates[0],coordinates[1])
            if compareCoordinates in enemyActiveCoordinates:
                missle.color("red")
                missle.stamp()
                enemyActiveCoordinates.remove(compareCoordinates)
                if enemyActiveCoordinates != []:
                    userTurn = True
                    computerTurn = False
                elif enemyActiveCoordinates == []:
                    userTurn = False
                    computerTurn = False
                    missle.setposition(0,0)
                    missle.color("black")
                    missle.write("YOU WON!!!", align = "center", font = ("Arial", 50, "bold"))
            elif compareCoordinates not in enemyActiveCoordinates:
                missle.color("blue")
                missle.stamp()
                userTurn = False
                computerTurn = True
        elif userTurn == False and computerTurn == True:
            compareCoordinates = "filler"
            computerGuessX = "filler"
            computerGuessY = "filler"
            while computerGuessX not in xCoordinateListUser or computerGuessY not in yCoordinateListUser or compareCoordinates in computerGuesses:
                computerGuessX = xCoordinateListUser[random.randint(0,9)]
                computerGuessY = yCoordinateListUser[random.randint(0,9)]
                compareCoordinates = "{0}{1}".format(computerGuessX,computerGuessY)
##            print(compareCoordinates)
            computerGuesses.append(compareCoordinates)
            coordinates = translate_coordinates(computerGuessX, computerGuessY)
            missle.setposition(coordinates[0], coordinates[1])
            if compareCoordinates in activeCoordinates:
                missle.color("red")
                missle.stamp()
                activeCoordinates.remove(compareCoordinates)
                if activeCoordinates != []:
                    userTurn = False
                    computerTurn = True
                elif activeCoordinates == []:
                    userTurn = False
                    computerTurn = False
                    missle.setposition(0,0)
                    missle.color("black")
                    missle.write("You lost...", align = "center", font = ("Arial", 50, "bold"))
            elif compareCoordinates not in activeCoordinates:
                missle.color("blue")
                missle.stamp()
                userTurn = True
                computerTurn = False
            
            
        


#*************************************************************************************************************
#This section of code lets you play again.
                
    playAgain = "filler"
    while playAgain != "yes" and playAgain != "no":
        playAgain = gameWindow.textinput("Play Again?","Enter 'yes' to play again, or 'no' to quit.").lower()
        if playAgain == "yes":
            wantPlay = True
            activeCoordinates = []
            enemyActiveCoordinates = []
            airCraftCarrier.clear()
            battleShip.clear()
            submarine.clear()
            destroyer.clear()
            patrol.clear()
            missle.clear()
            
        elif playAgain == "no":
            wantPlay = False

        else:
            message = gameWindow.textinput("ERROR", "That was not a valid inpt. Enter either 'yes' or 'no'.")

gameWindow.bye()


            
            
            
            
            





    






