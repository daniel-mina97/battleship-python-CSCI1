#********************************************************* projectBattleShip.py  ************************************************************
#
# Name: Daniel Mina
#
# Course: CSCI 1470
#
# Assignment: Project
#
# Algorithm:
#   Start
#       Define a function translate_coordinates with two parameters 'number' and 'letter'
#           create an empty list translatedCoordinates
#           set two if statement chains, checking the value of 'number' in one and 'letter' in the other
#               in each possible instance of number and letter, set a corresponding x and y coordinate for turtle graphics
#           append x to translatedCoordinates
#           append y to translated Coordinates
#           return translatedCoordinates
#
#       Define a function draw_ship with three parameters 'turtle', 'screen', and 'shipType'
#           set xCoordinateListUser equal to a list with the integers 1-10 as elements
#           set yCoordinateListUser equal to a list with the letters a-j as elements
#           set an if statement chain checking the value of shipType
#           if shipType is equal to "Aircraft Carrer"
#               set blockLength equal to 5 (this will determine how long the ship is)
#               set screenLimit equal to 6 (this will ensure the ship is within bounds for the game)
#           else if shipType is equal to "Battleship"
#               set blockLength equal to 4
#               set screenLimit equal to 7
#           else if shipType is equal to "Submarine"
#               set blocklength equal to 3
#               set screenLimit equal to 8
#           else if shipType is equal to "Destroyer"
#               set blocklength equal to 3
#               set screenLimit equal to 8
#           else if shipType is equal to "Patrol"
#               set blockLength equal to 2
#               set screenLimit equal to 9
#           prompt user to see if they want their ship vertically or horizontally oriented
#           if user wants a vertical orientation
#               set topMostBlockX equal to a value not in xCoordinateListUser
#               set topMostBlockY equal to a value not in yCoordinateListUser
#               while topMostBlockX is not in xCoordinateListUser or topMostBlockY is not in subindex 0 to screenLimit of yCoordinateListUser
#                   prompt user for a new topMostBlockX value
#                   prompt user for a new topMostBlockY value
#                   let user know if conditions of the while loop are still not met
#               set coordinates equal to the returned value of translate_coordinates function with topMostBlockX and topMostBlockY as arguments
#               lift the pen in turtle graphics
#               set the position of the pen to the coordinates where x equals subindex zero of coordinates and y equals subindex one of coordinates
#               set the pen down and begin the color filling function of turtle graphics
#               draw a rectangle that is blocklength units long vertically
#               stop the filling process
#               set shipLocation equal to an empty list
#               set whichWay equal to a list containing the one element that is the orientation chosen by the user (vertical)
#               for every 'letter'-'number' coordinate covered by the ship
#                   append that coordinate as a string to shipLocation
#               return shipLocation plus whichWay
#           elif user wants a horizontal orientation
#               set leftMostBlockX equal to a value not in xCoordinateListUser
#               set leftMostBlockY equal to a value not in yCoordinateListUser
#               while leftMostBlockX is not in subindex 0 to screenLimit of xCoordinateListUser or leftMostBlockY is not in yCoordinateListUser
#                   prompt user for a new leftMostBlockX value
#                   prompt user for a new leftMostBlockY value
#                   let user know if condition of the while loop are still not met
#               set coordiantes equal to the returned value of translate_coordinates function with leftMostBlockX and leftMostBlockY as arguments
#               lift the pen in turtle graphics
#               set the position of the pen to the coordinates where x equals subindex zero of coordinates and y equals subindex one of coordinates
#               set the pen down and begin the color filling function of turtle graphics
#               draw a rectangle that is blocklength units long horizontally
#               stop the filling process
#               set shipLocation equal to an empty List
#               set whichWay equal to a list containing the one element that is the orientation chose by the user (horizontal)
#               for every 'letter'-'number' coordinate convered by the ship
#                   append that coordinate as a string to shipLocation
#               return shipLocation plus whichWay
#           elif user does not enter an appropriate value for orientation
#               return draw_ship function (this repeats the function until an apporopriate value is chosen
#
#       Define a function named enemy_ship with one parameter shipType
#           set xCoordinateListOpponenet equal to a list with the integers 11-20
#           set yCoordinateListOpponent equal to a list with the letters k-t
#           if shipType equals "Aircraft Carrier"
#               set blockLength equal to 5
#               set screenLimit equal to 6
#           elif shipType equals "Battleship"
#               set blockLength equal to 4
#               set screenLimit equal to 7
#           elif shipType equals "Submarine"
#               set blockLength equal to 3
#               set screenLimit equal to 8
#           elif shipType equals "Destroyer"
#               set blockLength equal to 3
#               set screenLimit equal to 8
#           elif shipType equals "Patrol"
#               set blockLength equal to 2
#               set screenLimit equal to 9
#           set orientationList equal to a list with two elements, "vertical" and "horizontal"
#           set orientation equal to a random subindex (using randint funtion) of orientationList
#           if orientation is vertical
#               set topMostBlockX equal to a value not in xCoordinateListOpponent
#               set topMostBlockY equal to a value not in yCoordinateListOpponent
#               while topMostBlockX is not in xCoordinateListOpponent or topMostBlockY is not in subindex 0 to screenLimit of yCoordinateListOpponent
#                   set topMostBlockX to any random element from xCoordinateListOpponent
#                   set topMostBlockY to any random element subindex 0 to screenLimit from yCoordinateListOpponent
#               set shipLocation equal to an empty list
#               for every y coordinate from topMostBlockY to the index of topMostBlockY plus blockLength
#                   set coordinate equal to a formatted string with topMostBlockX as the first string variable and every y coordinate as the second string variable
#                   append coordinate to shipLocation
#               return shipLocation
#           elif orientation is horizontal
#               set leftMostBlockX equal to a value not in xCoordinateListOpponent
#               set leftMostBlockY equal to a value not in yCoordinateListOpponent
#               while leftMostBlockX is not in subindex 0 to screenLimit of xCoordinateListOpponent or leftMostBlockY is not in yCoordinateListOpponent
#                   set leftMostBlockX to any random element subindex 0 to screenLimit from xCoordinateListOpponent
#                   set leftMostBlockY to any random element from yCoordinateListOpponent
#               set shipLocation equal to an empty list
#               for every x coordinate from leftMostBlockX to the index of leftMostBlockX plus blockLength
#                   set coordinate equal to a formatted string with every x coordinate as the first string variable and leftMostBlockY as the second string variable
#                   append coordinate to shipLocation
#               return shipLocation
#   
#       set gameWindow equal to a turtle graphics screen
#       set the gameWindow title equal to "Battleship"
#       set the screensize of gameWindow and the color of the screen
#       set pegPoints equal to a turtle pen
#       hide pegPoints
#       set the shape of pegPoints equal to a circle
#       left pegPoints up
#       set the speed of pegPoints to the fastes setting
#       use the turtle graphics write function to label the gameWindow
#       create the coordinate systems for both the user and the computer
#       set wantPlay equal to True
#       while wantPlay equals True
#           create a new turtle for every user ship that will be drawn (there should be five)
#           set activeCoordinates equal to an empty list
#           set verticalCount and horizontalCount equal to zero
#           set userAirCraftCarrier equal to a list with "filler" as the only element
#           while subindex zero of userAirCraftCarrier is not in activeCoordinates
#               set uACC equal to the draw_ship function with "Aircraft Carrier" as the ship type
#               set userAirCraftCarrier equal to uACC minus the last element which tells us the orientation
#               for every coordinate in userAirCraftCarrier
#                   if the coordinate is in activeCoordinates
#                       clear the turtle that drew the ship
#                       set userAirCraftCarrier equal to a list with "filler" as the only element
#                   elif the coordinate is not in activeCoordinates
#                       append the coordinate to temporaryCoordinates
#                       if temporaryCoordinates is equal to userAirCraftCarrier
#                           set activeCoordinates equal to activeCoordinates plus userAirCraftCarrier
#           if the last element of uACC is equal to "vertical"
#               add one to verticalCount
#           elif the last element of uACC is equal to "horizontal"
#               add one to horizontalCount
#           set userBattleShip equal to a list with "filler" as the only element
#           while subindex zero of userBattleShip is not in activeCoordinates
#               set uBS equal to the draw_ship function with "Battleship" as the ship type
#           for every coordinate in userBattleShip
#                   if the coordinate is in activeCoordinates
#                       clear the turtle that drew the ship
#                       set userBattleShip equal to a list with "filler" as the only element
#                   elif the coordinate is not in activeCoordinates
#                       append the coordinate to temporaryCoordinates
#                       if temporaryCoordinates is equal to userBattleShip
#                           set activeCoordinates equal to activeCoordinates plus userBattleShip
#           if the last element of uBS is equal to "vertical"
#               add one to verticalCount              
#           elif the last element of uBS is equal to "horizontal"
#               add one to horizontalCount
#           set userSubmarine equal to a list with "filler" as the only element
#           while subindex zero of userSubmarine is not in activeCoordinates
#               set uS equal to the draw_ship function with "Submarine" as the ship type
#               set userSubmarine equal to uS minus the last element which tells us the orientation
#               for every coordinate in userSubmarine
#                   if the coordinate is in activeCoordinates
#                       clear the turtle that drew the ship
#                       set userSubmarine equal to a list with "filler" as the only element
#                   elif the coordinate is not in activeCoordinates
#                       append the coordinate to temporaryCoordinates
#                       if temporaryCoordinates is equal to userSubmarine
#                           set activeCoordinates equal to activeCoordinates plus userSubmarine
#               add one to verticalCount
#           elif the last element of uS is equal to "horizontal"
#               add one to horizontalCount
#           set userDestroyer equal to a list with "filler" as the only element
#           while subindex zero of userDestroyer is not in activeCoordinates
#               set uD equal to the draw_ship function with "Destroyer" as the ship type
#               set userDestroyer equal to uD minus the last element which tells us the orientation
#               for every coordinate in userDestroyer
#                   if the coordinate is in activeCoordinates
#                       clear the turtle that drew the ship
#                       set userDestroyer equal to a list with "filler" as the only element
#                   elif the coordinate is not in activeCoordinates
#                       if temporaryCoordinates is equal to userDestroyer
#                           set activeCoordinates equal to activeCoordinates plus userDestroyer
#           if the last element of uD is equal to "vertical"
#               add one to verticalCount
#           elif the last element of uD is equal to "horizontal"
#               add one to horizontalCount
#           while subindex zero of userPatrol is not in activeCoordinates
#               set uP equal to the draw_ship function with "Patrol" as the ship type
#               set userPatrol equal to uP minus the last element which tells us the orientation
#               for every coordinate in userPatrol
#                   if the coordinate is in activeCoordinates
#                       clear the turtle that drew the ship
#                       set userPatrol equal to a list with "filler" as the only element
#                   elif the coordinate is not in activeCoordinates
#                       append the coordinate to temporaryCoordinates
#                       if temporaryCoordinates is equal to userPatrol
#                           set activeCoordinates equal to activeCoordinates plus userPatrol
#           if the last element of uP is equal to "vertical"
#               add one to verticalCount
#               add one to horizontalCount
#           set enemyActiveCoordinates equal to an empty list
#           set opponentAirCraftCarrier equal to a list with "filler" as the only element
#           while subindex zero of opponentAirCraftCarrier is not in enemyActiveCoordinates
#               set opponentAirCraftCarrier equal to the function enemy_ship with "Aircraft Carrier" as the shipType
#               set temporaryCoordinates equal to an empty list
#               for every coordinate in opponentAirCraftCarrier
#                   if the coordinate is in enemyActiveCoordinates
#                       set opponentAirCraftCarrier equal to a list with "filler" as the only element
#                   elif the coordinate is not in enemyActiveCoordinates
#                       append the coordinate to temporaryCoordinates
#                       if temporaryCoordinates is equal to opponentAirCraftCarrier
#                           set enemyActiveCoordinates equal to enemyActiveCoordinates plus opponentAirCraftCarrier
#           set opponentBattleShip equal to a list with "filler" as the only element
#           while subindex zero of opponentBattleShip is not in enemyActiveCoordinates
#               set opponentBattleShip equal to the function enemy_ship with "BattleShip" as the shipType
#               set temporaryCoordinates equal to an empty list
#               for every coordinate in opponentBattleShip
#                   if the coordinate is not in enemyActiveCoordiantes
#                       set opponentBattleShip equal to a list with "filler" as the only element
#                   elif the coordinate is not in enemyActiveCoordinates
#                           set enemyActiveCoordinates equal to enemyActiveCoordinates plus opponentBattleShip
#           set opponentSubmarine equal to a list with "filler" as the only element
#           while subindex zero of opponentSubmarine is not in enemyActiveCoordinates
#               set opponentSubmarine equal to the function enemy_ship with "Submarine" as the shipType
#               set temporaryCoordinates equal to an empty list
#               for every coordinate in opponentSubmarine
#                   if the coordinate is in enemyActiveCoordinates:
#                       set opponentSubmarine equal to a list with "filler" as the only element
#                       append the coordinate to temporaryCoordinates
#                       if temporaryCoordinates is equal to opponentSubmarine
#                           set enemyActiveCoordinates equal to enemyActiveCoordinates plus opponentSubmarine
#           set opponentDestroyoer equal to a list with "filler" as the only element
#           while subindex zero of opponentDestroyer is not in enemyActiveCoordinates
#               set opponentDestroyer equal to the function enemy_ship with "Destroyer" as the shipType
#               set temporaryCoordinates equal to an empty list
#               for every coordinate in opponentDestroyer
#                   if the coordinate is in enemyActiveCoordinates:
#                       set opponentDestroyer equal to a list with "filler" as the only element
#                   elif the coordinate is not in enemyActiveCoordinates
#                       append the coordinate to temporaryCoordinates
#                       if temporaryCoordinates is equal to opponentDestroyer
#                           set enemyActiveCoordinates equal to enemyActiveCoordinates plus opponentDestroyer
#           set opponentAirPatrol equal to a list with "filler" as the only element
#           while subindex zero of opponentPatrol is not in enemyActiveCoordinates
#               set opponentPatrol equal to the function enemy_ship with "Patrol" as the shipType
#               set temporaryCoordinates equal to an empty list
#               for every coordinate in opponentPatrol
#                   if the coordinate is in enemyActiveCoordinates:
#                       set opponentPatrol equal to a list with "filler" as the only element
#                   elif the coordinate is not in enemyActiveCoordinates
#                       append the coordinate to temporaryCoordinates
#                       if temporaryCoordinates is equal to opponentPatrol
#                           set enemyActiveCoordinates equal to enemyActiveCoordinates plus opponentPatrol
#           set userTurn equal to True
#           set computerTurn equal to False
#           set userGuesses equal to an empty list
#           set computerGuesses equal to an empty list
#           while userTurn equals True or computerTurn equals True
#               if userTurn equals True and computerTurn equals False
#                   set compareCoordinates equal to "filler"
#                   set userGuessX equal to "filler"
#                   set userGuessY equal to "filler"
#                   while userGuessX is not in xCoordinateListOpponent or userGuessY is not in yCoordinateListOpponent
#                       prompt user for new userGuessX and new userGuessY
#                       set compareCoordinates equal to a formatted string with userGuessX as the first string variable and userGuessY as the second string variable
#                   append compareCoordinates to userGuesses
#               elif userTurn equals False and computerTurn equals True
#                   set compareCoordinates equal to "filler"
#                   set computerGuessX equal to "filler"
#                   set computerGuessY equal to "filler"
#                   while computerGuessX is not in xCoordinateListUser or computerGuessY is not in yCoordinateListUser
#                       have a new computerGuessX and computerGuessY randomly generated with randint funtion
#                       set compareCoordinates equal to a fromatted string with computerGuessX as the first string varibale and computerGuessY as the second string variable
#                   append compareCoordinates to computerGuesses
#           prompt user if they would like to play again
#           if user wants to play again
#               set wantPlay equal to True
#               clear all lists and turtle drawings
#           elif user does not want to play again
#               set wantPlay equal to False
#   Stop
#
#***************************************************************************************************************************************
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


            
            
            
            
            





    






