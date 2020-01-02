#ESCAPE THE ABYSS
#LEVEL 1
import random
import time
import os
import sys
import pickle
import termcolor
from termcolor import *
import configFiles.gameconfig
from configFiles.gameconfig import *
import configFiles.descriptions
from configFiles.descriptions import * 

#Cell inputs
def cellFunction():
    CMC.level = 1
    CMC.choiceMaker = False
    UserInputFunction()
    CMC.choiceMaker = True
    if CMC.choiceMaker == True:
        if CMC.word == "gonorth" and CMC.cellDoor == "locked":
            print(colored(cellNorth, 'green'))
            CMC.text = cellNorth
            print(colored("---=---", 'green').center(93, ' '))
            cellFunction()

        if CMC.word == 'gonorth' and CMC.celldoor == "open":
            print(colored(cellNorth, 'green'))
            print(colored("---=---", 'green').center(93, ' '))
            cellFunction()

        if CMC.word == "goeast":
            print(colored(cellEast, 'green'))
            print(colored("---=---", 'green').center(93, ' '))
            cellFunction()

        if CMC.word == "gosouth":
            print(colored(cellSouth, 'green'))
            print(colored("---=---", 'green').center(93, ' '))
            cellFunction()

        if CMC.word == "gowest":
            print(colored(cellWest, 'green'))
            print(colored("---=---", 'green').center(93, ' '))
            cellFunction()
        
        if CMC.word == "readnote" and CMC.cellBrick == "true":
            print(colored(cellNote, 'green'))
            print(colored("---=---", 'green').center(93, ' '))
            cellFunction()
        
        if CMC.word == "jumpwindow":
            print(colored(cellWindow, 'green'))
            print(colored("---=---", 'green').center(93, ' '))
            cellFunction()
        
        if CMC.word == "checkbrick":
            print(colored(cellBrick, 'green'))
            print(colored("---=---", 'green').center(93, ' '))
            CMC.cellBrick = "true"
            cellFunction()
        
        if CMC.word == "takekey":
            invItem = "Cell Key"
            addingplayerInvDict(invItem)
            print(colored("---=---", 'green').center(93, ' '))
            cellFunction()

        if CMC.word == "usekey":
            keyItem = "Cell Key"
            usingItem(keyItem)
            if CMC.hasItem == "false":
                print(colored("You don't have the correct key."))
                cellFunction()

            if CMC.hasItem == "true":
                print(colored(cellDoorOpen, 'green'))
                time.sleep(5)
                level1()

        else:
            print(colored("Now is not the time for that!", 'green').center(93, " "))
            print()
            print(colored("---=---", 'green').center(93, ' '))
            cellFunction()
    
    else:
        print(colored("** ERROR **", 'green'))
        time.sleep(3)
        UserInputFunction()

#Level 1 function
def level1Function():

    CMC.choiceMaker = False
    UserInputFunction()
    CMC.choiceMaker = True
    
    if CMC.choiceMaker == True:
        None

#Cell description
def cell():
    menuStart()
    areaUpdate(cellParagraph)
    CMC.level = 1
    print(colored(cellParagraph, 'green'))
    print()
    print(colored("---=---", 'green').center(93, ' '))
    cellFunction()

#Level 1 description
def level1():
    menuStart()
    print(colored(level1Hallway1, 'green'))
    print()
    print(colored("---=---", 'green').center(93, ' '))
    level1Function()

#Level 1 intro text
def level1intro():
    menuStart()

    print(colored('"Just going to lay there?"', 'green').center(93, " "))
    print()
    time.sleep(2)
    print(colored('"pity, such a pathetic, lazy, disappointment."', 'green').center(93, " "))
    print()
    print(colored("---=---", 'green').center(93, ' '))
    time.sleep(5)
    menuStart()

    print(colored('"Open your eyes."', 'green').center(93, " "))
    print()
    time.sleep(2)
    print(colored('"Show me you are worthy"', 'green').center(93, " "))
    print()
    print(colored("---=---", 'green').center(93, ' '))
    time.sleep(5)
    menuStart()

    print(colored('"Good... good, thats right."', 'green').center(93, " "))
    print()
    time.sleep(2)
    print(colored('"RISE!"', 'green').center(93, " "))
    print()
    print(colored("---=---", 'green').center(93, ' '))
    time.sleep(5)
    cell()


