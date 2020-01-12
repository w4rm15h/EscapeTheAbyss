import os, os.path, signal, sys
import time, pickle, random, shutil
import hashlib, uuid, binascii, bcrypt
import termcolor, sqlite3
from termcolor import colored
import pysftp as sftp
from getpass import getpass
from descriptions import *

#Class to store variables for player
class gameVars:
    playerProfile = {}
    currentText = ""
    currentLevel = ""
    potionStrength = 25

def textPrinting():
    os.system('clear')
    print(colored("---------=---------", 'green').center(93, ' '))

def menuStart():
    os.system("clear")
    Print(topBanner)

#Printing standart text
def Print(text):
    print(colored('                            {0}'.format(text), 'green'))

#Printing Alerts and information
def Alert(text):
    print()
    print(colored('                            *{0}*'.format(text), 'yellow'))

#Print for error comments
def Error(text):
    print(colored('                            {0}'.format(text), 'red'))

#Function for the error responses
def errorResponse():
    response = random.choice(errorOutputs)
    Error(response)

#Pressing CTRL + C
import signal
def signal_handler(sig, frame):
    pass
signal.signal(signal.SIGINT, signal_handler)

#UPLOADING USERS DATABASE
def uploadDatabase():
    #Putting users.db in FTP server
    try:
        cnopts = sftp.CnOpts()
        cnopts.hostkeys = None
        Print("*CONNECTING TO SERVER*")
        with sftp.Connection(host = "104.198.133.105", username="w4rm15h", password="Magmaturtle1", cnopts=cnopts) as s:
            Print('*SAVING DATA*')
            s.cwd("escapeSaves")
            remotePath='users.db'
            localPath='users.db'
            s.put(localPath, remotePath)
            s.close()   
            Print("*FILES SAVED!*")
    except Exception as e:
        Print(str(e))

#DOWNLOADING USER PROFILE
def loadProfile(userName):
    #getting user profile from server
    try:
        cnopts = sftp.CnOpts()
        cnopts.hostkeys = None
        Print("*ESTABLISHING A CONNECTION*")
        with sftp.Connection(host = "104.198.133.105", username="w4rm15h", password="Magmaturtle1", cnopts=cnopts) as s:
            Print("*CONNECTED*")
            s.cwd("escapeSaves")
            remotePath='{0}.abyss'.format(userName)
            localPath='{0}.abyss'.format(userName)
            Print("*RETRIEVING FILES*")
            s.get(remotePath, localPath)
            Print("*LOADING COMPLETE*")
            s.close()
    except Exception as e:
        Print(str(e))

#UPLOADING USER PROFILE
def uploadingSaveFile():
    try:
        cnopts = sftp.CnOpts()
        cnopts.hostkeys = None
        Print("*ESTABLISHING A CONNECTION*")
        with sftp.Connection(host = "104.198.133.105", username="w4rm15h", password="Magmaturtle1", cnopts=cnopts) as s:
            Print("*CONNECTED*")
            s.cwd("escapeSaves")
            remotePath='{0}.abyss'.format(userName)
            localPath='{0}.abyss'.format(userName)
            Print("*UPLOADING FILES*")
            s.put(remotePath, localPath)
            Print("*SAVE COMPLETE!*")
            s.close()
    except Exception as e:
        Print(str(e))

#Uploading the save file quietly
def saveProfile(userName):
    #uploading user profile to server
    try:
        cnopts = sftp.CnOpts()
        cnopts.hostkeys = None
        with sftp.Connection(host = "104.198.133.105", username="w4rm15h", password="Magmaturtle1", cnopts=cnopts) as s:
            s.cwd("escapeSaves")
            remotePath='{0}.abyss'.format(userName)
            localPath='{0}.abyss'.format(userName)
            s.put(remotePath, localPath)
            Alert("*Game Saved*")
            s.close()
    except Exception as e:
        Print(str(e))

#LOADINGS AND SAVING PLAYER PROFILE --------START--------
#Loading the player profile
def loadProfileGame(playerName):
    with open("{0}.abyss".format(playerName), 'rb') as loadingProfile:
        gameVars.playerProfile = pickle.load(loadingProfile)

#Saving the player profile
def saveProfileGame(playerName):
    with open("{0}.abyss".format(playerName), 'wb') as savingProfile:
        pickle.dump(gameVars.playerProfile, savingProfile)
    saveProfile(playerName)
#LOADINGS AND SAVING PLAYER PROFILE ---------END---------

def drinkingPotion():
    Alert("You drink a potion, recovering {0} health.".format(gameVars.potionStrength))
    gameVars.playerProfile['healingitems']['potion'] -= 1
    playerHealth = gameVars.playerProfile["playerhealth"]
    playerMaxHealth = gameVars.playerProfile["playermaxhealth"]
    gameVars.playerProfile['playerhealth'] += gameVars.potionStrength
    if gameVars.playerProfile['playerhealth'] > playerMaxHealth:
        playerHealth = playerHealth
    saveProfileGame(gameVars.playerProfile['playername'])

def addingPotion():
    playerHealth = gameVars.playerProfile['playerhealth']
    playerMaxHealth = gameVars.playerProfile['playermaxhealth']
    if gameVars.playerProfile['healingitems']['potion'] < 3:
        gameVars.playerProfile['healingitems']['potion'] += 1
        Alert("1 x Potion added")
    else:
        if gameVars.playerProfile['healingitems']['potion'] == 3:
            print()
            Error("Potion's bag full!")
            Print("Do you want to use the potion now?")
            usePotion = input(colored("                            > ", 'green'))
            if usePotion in yes:
                if playerHealth < playerMaxHealth:
                    playerHealth += gameVars.potionStrength
                    if playerHealth > playerMaxHealth:
                        playerHealth = playerMaxHealth
                        Alert("Player health: {0}".format(playerHealth))
                else:
                    print()
                    Alert("Player health is already full")

            else:
                print()
                Print("you put back the potion")

def printStats():
    playerName = gameVars.playerProfile['playername']
    weaponName = (gameVars.playerProfile["playerweapon"]["weaponName"])
    armorName = (gameVars.playerProfile["playerarmor"]["armorName"])
    weaponAttack = (gameVars.playerProfile["playerweapon"]["weaponAttack"])
    armorDefence = (gameVars.playerProfile["playerarmor"]["armorDefence"])
    weaponColour = (gameVars.playerProfile["playerweapon"]["weaponColour"])
    armorColour = (gameVars.playerProfile["playerarmor"]["armorColour"])
    playerHealth = gameVars.playerProfile["playerhealth"]
    playerAttack = gameVars.playerProfile["playerattack"]
    playerDefence = gameVars.playerProfile["playerdefence"]
    playerAttackTotal = (playerAttack + weaponAttack)
    playerDefenceTotal = (playerDefence + armorDefence)
    weaponPrint = (colored("                            Weapon: " + weaponName, '{0}'.format(weaponColour)))
    armorPrint = (colored("                            Armor: " + armorName, '{0}'.format(armorColour)))

    Print(divider)
    Print(playerName)
    Print(divider)
    print(weaponPrint)
    Print("Weapon Attack: {0}".format(weaponAttack))
    print(armorPrint)
    Print("Player Health: {0}".format(playerHealth))
    Print("Armor Defence: {0}".format(armorDefence))
    Print("Player Attack: {0}".format(playerAttackTotal))
    Print("Player Defence: {0}".format(playerDefenceTotal))
    Print(divider)

#Inventory functions
def printInventory():
    item1 = gameVars.playerProfile['inventory']["1. "]
    item2 = gameVars.playerProfile['inventory']["2. "]
    item3 = gameVars.playerProfile['inventory']["3. "]
    item4 = gameVars.playerProfile['inventory']["4. "]
    item5 = gameVars.playerProfile['inventory']["5. "]
    item6 = gameVars.playerProfile['inventory']["6. "]
    item7 = gameVars.playerProfile['inventory']["7. "]
    item8 = gameVars.playerProfile['inventory']["8. "]
    item9 = gameVars.playerProfile['inventory']["9. "]
    item10 = gameVars.playerProfile['inventory']["10. "]
    playerPotions = gameVars.playerProfile["healingitems"]['potion']

    Print(divider)
    Print('Inventory')
    Print(divider)
    Print(" 1. " + item1)
    Print(" 2. " + item2)
    Print(" 3. " + item3)
    Print(" 4. " + item4)
    Print(" 5. " + item5)
    Print(" 6. " + item6)
    Print(" 7. " + item7)
    Print(" 8. " + item8)
    Print(" 9. " + item9)
    Print("10. " + item10)
    Print(divider)
    Print("Potion(s): {0}".format(playerPotions))
    Print(divider)

#Adding item to inventory
def addItem(item):
    adding = 1
    while adding == 1:

        printInventory()
        Print("Do you want to pick up the {0}?".format(item))
        Print("Where would you like to place the item?")
        placement = input(colored("                            >", 'green'))

        if placement in oneToTen:
            if gameVars.playerProfile['inventory']["{0}. ".format(placement)] != "Empty":
                Alert("Are you sure you want to overwrite {0}?".format(gameVars.playerProfile['inventory']["{0}. ".format(placement)]))
                confirm = input(colored("                            >", 'green'))

                if confirm in yes:
                    gameVars.playerProfile['inventory']["{0}. ".format(placement)] = item
                    Alert("{0} added to inventory!".format(item))
                    saveProfileGame(gameVars.playerProfile['playername'])
                    break

                else:
                    if confirm in no:
                        Error("Alright...")
                    else:
                        Error("Not really a valid input was it?")
            else:
                gameVars.playerProfile['inventory']["{0}. ".format(placement)] = item
                Alert("{0} added to inventory!".format(item))
                saveProfileGame(gameVars.playerProfile['playername'])
                break
        else:
            Error("Shame, such a simple creation...")

def removeItem(item):
    name = gameVars.playerProfile['playername']
    for i in gameVars.playerProfile['inventory']:
        if gameVars.playerProfile['inventory'][i] == item:
            gameVars.playerProfile['inventory'][i] = 'Empty'
    Alert("{0} removed from inventory".format(item))
    saveProfileGame(name)

    #Picking up WEAPON function
def pickUpWeapon(weaponName):
#Rolling the dice
    number1 = random.randint(1,20)
    number2 = random.randint(1,20)
    total = (number1 + number2)
#Legendary grade
    if total < 4:
        grade = "legendary"
        name = (weaponName)
        score = 30
        colour = "magenta"
        weaponScore(grade, name, score, colour)
#Mystic grade
    if total > 4 and total < 10:
        grade = "mystic"
        name = (weaponName)
        score = 25
        colour = "cyan"
        weaponScore(grade, name, score, colour)
#Uncommon grade
    if total > 10 and total < 20:
        grade = "uncommon"
        name = (weaponName)
        score = 23
        colour = "blue"
        weaponScore(grade, name, score, colour)
#Common Grade
    if total > 20 and total < 40:
        grade = "common"
        name = (weaponName)
        score = 21
        colour = "green"
        weaponScore(grade, name, score, colour)

#Equipping or passing on WEAPON
def weaponScore(grade, name, score, colour):
    menuStart()
#Displaying Weapon and givinge choice to equip
    menuStart()
    print()
    print(colored("**********", 'green').center(93, " "))
    print(colored("Chest contains", 'green').center(93, " "))
    print(colored("**********", 'green').center(93, " "))
    print()
    print(colored("{0}".format(name), '{0}'.format(colour)).center(93, " "))
    print(colored("Damage: {0}".format(score), '{0}'.format(colour)).center(93, " "))
    print()
    print(colored("-----=-----", 'green').center(93, ' '))
    print(colored("Would you like to equip", 'green').center(93, " "))
    print(colored("'{0}'?".format(name), 'green').center(93, " "))
    yesNo = input("                                          > ")
#Picking Up Weapon
    if yesNo in yes:
        gameVars.playerProfile["playerweapon"]["weaponGrade"] = grade
        gameVars.playerProfile["playerweapon"]["weaponName"] = name
        gameVars.playerProfile["playerweapon"]["weaponAttack"] = score
        gameVars.playerProfile["playerweapon"]["weaponColour"] = colour
        saveProfileGame(gameVars.playerProfile['playername'])
        print(colored("-----=-----", 'green').center(93, ' '))
        print()
        print(colored("You have equipped the weapon", 'green').center(93, " "))
        print()
        print(colored("-----=-----", 'green').center(93, ' '))
        time.sleep(3)
        menuStart()
#Leaving weapon behind
    if yesNo in no:
        print(colored("-----=-----", 'green').center(93, ' '))
        print()
        print(colored("You left the weapon behind", 'green').center(93, " "))
        print()
        print(colored("-----=-----", 'green').center(93, ' '))
        time.sleep(3)
        menuStart()

#Picking up ARMOR function
def pickUpArmor(armorName):
#Rolling the dice
    number1 = random.randint(1,20)
    number2 = random.randint(1,20)
    total = (number1 + number2)
#Legendary grade
    if total < 4:
        grade = "legendary"
        name = (armorName)
        score = 50
        colour = "magenta"
        armorScore(grade, name, score, colour)
#Mystic grade
    if total > 4 and total < 10:
        grade = "mystic"
        name = (armorName)
        score = 40
        colour = "cyan"
        armorScore(grade, name, score, colour)
#Uncommon grade
    if total > 10 and total < 20:
        grade = "uncommon"
        name = (armorName)
        score = 35
        colour = "blue"
        armorScore(grade, name, score, colour)
#Common Grade
    if total > 20 and total < 40:
        grade = "common"
        name = (armorName)
        score = 30
        colour = "green"
        armorScore(grade, name, score, colour)

#Equipping or passing on ARMOR
def armorScore(grade, name, score, colour):
    menuStart()
#Displaying ARMOR and giving choice to equip
    menuStart()
    print()
    print(colored("**********", 'green').center(93, " "))
    print(colored("Chest contains", 'green').center(93, " "))
    print(colored("**********", 'green').center(93, " "))
    print()
    print(colored("{0}".format(name), '{0}'.format(colour)).center(93, " "))
    print(colored("Defence: {0}".format(score), '{0}'.format(colour)).center(93, " "))
    print()
    print(colored("-----=-----", 'green').center(93, ' '))
    print(colored("Would you like to equip", 'green').center(93, " "))
    print(colored("'{0}'?".format(name), 'green').center(93, " "))
    yesNo = input("                                          > ")
#Picking Up armor
    if yesNo in yes:
        gameVars.playerProfile["playerarmor"]["armorGrade"] = grade
        gameVars.playerProfile["playerarmor"]["armorName"] = name
        gameVars.playerProfile["playerarmor"]["armorDefence"] = score
        gameVars.playerProfile["playerarmor"]["armorColour"] = colour
        saveProfileGame(gameVars.playerProfile['playername'])
        print(colored("-----=-----", 'green').center(93, ' '))
        print()
        print(colored("You put on the Armor", 'green').center(93, " "))
        print()
        print(colored("-----=-----", 'green').center(93, ' '))
        time.sleep(3)
        menuStart()
#Leaving armor behind
    if yesNo in no:
        print(colored("-----=-----", 'green').center(93, ' '))
        print()
        print(colored("You left the armor behind", 'green').center(93, " "))
        print()
        print(colored("-----=-----", 'green').center(93, ' '))
        time.sleep(3)
        menuStart()
