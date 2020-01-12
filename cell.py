#ESCAPE THE ABYSS
#CELL
#LEVEL 1
import random
import time
import os
import sys
import pickle
import termcolor
from termcolor import colored
from gameconfig import *
from descriptions import * 

cellCommands = [
                'gonorth',
                'gosouth',
                'goeast',
                'gowest',
                'readnote',
                'jumpwindow',
                'checkbrick',
                'takekey',
                'usekey',
                'takepotion'
                ]  

class cellVars:
    potion = True
    cellDoor = "locked"
    cellBrick = False

#1st time playing the game, introduction to the CELL.
def cellIntroduction(playerName):
    textPrinting()

    print(colored('"Just going to lay there?"', 'green').center(93, " "))
    print()
    time.sleep(1)
    print(colored('"pity, such a pathetic, lazy, disappointment."', 'green').center(93, " "))
    time.sleep(2)
    textPrinting()

    print(colored('"Open your eyes."', 'green').center(93, " "))
    print()
    time.sleep(1)
    print(colored('"Show me you are worthy"', 'green').center(93, " "))
    time.sleep(2)
    textPrinting()

    print(colored('"Good... good, thats right."', 'green').center(93, " "))
    print()
    time.sleep(1)
    print(colored('"RISE!"', 'green').center(93, " "))
    time.sleep(3)

    gameVars.playerProfile['playernew'] = False
    saveProfileGame(playerName)
    cellInit(playerName)

def userInputcell():
    userInputcellting = 1
    while userInputcellting == 1:

        #Getting user input
        print()
        Print(divider)
        userInputcell = input(colored("                            > ", 'green'))

        #Splitting input into words
        userInSplit = userInputcell.split()

        #Getting string length
        stringLength = len(userInSplit)
        #Checking if the string is empty
        if stringLength < 1:
            Error("You have to give me a command")

        #For single word commands
        if stringLength == 1:
            command = userInSplit[0].lower()

            if command in playerCommands:
                if command == "inventory":
                    #Printing the inventory
                    printInventory()
                if command == "stats":
                    #Print player stats
                    printStats()
                if command == "clear":
                    clearScreen()
            else:
                print()
                errorResponse()

        #For commands > single words
        if stringLength == 2 or stringLength > 2:
            #Conditions for is the string is more than 1 word
            verb = userInSplit[0].lower()
            obj = userInSplit[-1].lower()
            #Command is first and last word of input
            command = (verb + obj)

            #Checking if verb is a player command
            if verb in playerCommands:

                if verb == "drop":
                    if obj not in oneToTen:
                        print()
                        Error("*Use the number of the inventory item not the name*")
                        continue
                    else:
                        itemName = gameVars.playerProfile['inventory']["{0}. ".format(obj)]
                        if itemName != "Empty":
                            Alert("Dropped {0}".format(itemName))
                            gameVars.playerProfile['inventory']["{0}. ".format(obj)] = "Empty"
                            saveProfileGame(gameVars.playerProfile['playername'])
                            continue
                        else:
                            print()
                            Error("*You have nothing to drop*")
                            continue

                if verb == "move":
                    move = userInSplit[-2]
                    if move in oneToTen:
                        if obj in oneToTen:
                            store = gameVars.playerProfile['inventory']["{0}. ".format(move)]
                            if store == "Empty":
                                print()
                                Error("*There is nothing to move*")
                                continue
                            else:
                                gameVars.playerProfile['inventory']["{0}. ".format(move)] = "Empty"
                                gameVars.playerProfile['inventory']["{0}. ".format(obj)] = store
                                Alert("{0} Moved from {1} to {2}".format(store, move, obj))
                                continue
                        else:
                            print()
                            Error("*Choose a valid number, fool*")
                            continue
                    else:
                        print()
                        Error("*Choose a valid number, fool*")
                        continue

                if verb == "drink" and obj == "potion" and gameVars.playerProfile["healingitems"]["potion"] != 0:
                    if gameVars.playerProfile["playerhealth"] != 100:
                        drinkingPotion()
                        continue
                    else:
                        Alert("Your Health is already full")
                        continue
                else:
                    if verb == "drink" and obj == "potion" and gameVars.playerProfile["healingitems"]["potion"] == 0:
                        print()
                        Error("You do not have any potions")
                        continue

            if command in cellCommands:

                if command == "gonorth" and cellVars.cellDoor == "locked":
                    print(colored(cellNorth, 'green'))
                    gameVars.text = cellNorth
                    
                if command == "goeast":
                    print(colored(cellEast, 'green'))
                    gameVars.text = cellEast
                    
                if command == "gosouth":
                    print(colored(cellSouth, 'green'))
                    gameVars.text = cellSouth
                    
                if command == "gowest":
                    print(colored(cellWest, 'green'))
                    gameVars.text = cellWest
                                  
                if command == "jumpwindow":
                    print(colored(cellWindow, 'green'))
                    gameVars.text = cellWindow
                                    
                if command == "checkbrick":
                    print(colored(cellBrick, 'green'))
                    gameVars.text = cellBrick
                    cellVars.cellBrick = "true"
                
                if command == "takepotion":
                    if cellVars.potion == True:
                        addingPotion()
                        cellVars.potion = False
                    else:
                        print()
                        Error("You have already retrieved the potion")

                if command == "takekey":
                    invItem = "Cell Key"
                    addItem(invItem)
                    
                if command == "usekey":
                    keyItem = "Cell Key"
                    for i in gameVars.playerProfile['inventory']:
                        if keyItem in gameVars.playerProfile['inventory'][i]:
                            Print(unlockingCellDoor)
                            cellVars.cellDoor = "unlocked"
                            removeItem(keyItem)
                            print()
                            Print("      You have escaped the cell.")
                            Print("      Let us see what lies ahead...")
                            Print("      *Press enter to continue*")
                            #Continue function
                            ctn = input()
                            if ctn == "":
                                level1Input()
                            else:
                                Error("I said press enter... hmm")
                                level1Input()
                    else:
                        print()
                        Error("You do not have the correct key...")

                continue
            else:
                print()
                errorResponse()
                continue

def cellInit(playerName):
    menuStart()
    loadProfileGame(playerName)
    gameVars.level = "cell"
    gameVars.potionStrength = 25
    Print(cellOpen)
    userInputcell()
