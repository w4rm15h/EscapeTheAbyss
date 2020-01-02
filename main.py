#Escape the Abyss
#w4rm15h
#2019
#Imports
import os, os.path, signal, sys
import time, pickle, random, shutil
import hashlib, uuid, binascii, bcrypt
import termcolor, sqlite3
from termcolor import colored
import pysftp as sftp
from getpass import getpass
from gameconfig import *
from descriptions import *
#from levels.level1 import *

#GETTING USERS DATABASE
def initfunction():
    try:
        menuStart()
        print()
        cnopts = sftp.CnOpts()
        cnopts.hostkeys = None
        Print("*STARTING*")
        Print("*ESCAPE THE ABYSS*")
        Print("*CONNECTING TO SERVER*")
        with sftp.Connection(host = "104.198.133.105", username="w4rm15h", password="Magmaturtle1", cnopts=cnopts) as s: 
            s.cwd("escapeSaves")
            remotePath='users.db'
            localPath='users.db'
            s.get(remotePath, localPath)
            s.close()
            Print("*CONNECTION ESTABLISHED*")
            Print("*STARTING GAME!*")
            time.sleep(2)
            userHome()
    except Exception as e:
        Print(str(e))

#LOGIN MENU
def userLogin():
    #Clearing the screen
    menuStart()
    #Connecting to db
    connection = sqlite3.connect('users.db')
    c = connection.cursor()
    #Username input
    Print("Enter your username")
    print()
    userName = input(colored("                                     > ", 'green'))
    c.execute("SELECT username FROM users WHERE username=?", (userName,))
    user = c.fetchall()
    if user:
        print()
        Print("Welcome, {0}".format(userName))
        #Password input
        print()
        Print("Please enter your password...")
        print()
        passWord = getpass(colored("                                     > ", 'green')).encode()
        #Verifying the password
        #Pulling userpassword from db
        c.execute("SELECT key FROM users WHERE username=?", (userName,))
        hashed = c.fetchone()
        #checking password against input
        if bcrypt.checkpw(passWord, hashed[0]):
            Print("Welcome {0}".format(userName))
            #Connecting to FTP server and retrieve user save file
            loadProfile(userName)
            with open("{0}.abyss".format(userName), 'rb') as load:
                playerProfile = pickle.load(load)
            #Proceed to hub
            theHub(userName)
        else:
            Error("*Incorrect password*")
            time.sleep(2)
            userLogin()
    else:
        Error("Can't find you... ahhh!!!")
        time.sleep(1)
        userLogin()

def addingUser():
    #Clearing the screen
    menuStart()
    #Connecting to db
    connect = sqlite3.connect('users.db')
    c = connect.cursor()
    #Getting player information
    Print("Enter your character name")
    print()
    userName = input(colored("                                     > ", 'green'))
    #Checking if username exists
    c.execute("SELECT username FROM users WHERE username=?", (userName,))
    user = c.fetchone()
    if user:
        Error("Sorry, username already taken")
        time.sleep(1)
        addingUser()
    else:
        Print("Alright {0}, let us begin.".format(userName))
        time.sleep(2)
    menuStart()
    #Getting account password
    Print("Enter your password")
    Print("Your password will not display")
    print()
    pWord1 = getpass(colored("                                     > ", 'green'))
    print()
    Print("One more time...")
    print()
    pWord2 = getpass(colored("                                     > ", 'green'))
    while pWord1 != pWord2:
        print()
        Error("Passwords do not match...")
        Error("Try again....")
        print()
        Print("Enter your password")
        Print("Your password will not display")
        print()
        pWord1 = getpass(colored("                                     > ", 'green'))
        Print("One more time...")
        print()
        pWord2 = getpass(colored("                                     > ", 'green'))
    else:
        #Making password hash
        password = pWord1.encode()
        hashedPassword = bcrypt.hashpw(password, bcrypt.gensalt())
        Print("Adding user account...")
        #Putting user into DB
        c.execute('INSERT INTO users (username, key) VALUES (?,?)', (userName, hashedPassword))
        connect.commit()
        connect.close()
        print()
        Print("Alright, {0}".format(userName))
        Print("Creating user profile")
        playerProfile["playerattack"] = random.randint(12, 15)
        playerProfile["playerdefence"] = random.randint(12, 15)
        playerProfile["playername"] = userName
        with open("{0}.abyss".format(userName), 'wb') as save1:
            pickle.dump(playerProfile, save1)
        uploadDatabase()
        saveProfile(userName)
        print()
        Print("Let's login and get started...")
        time.sleep(2)
        userLogin()

def userHelp():
    menuStart()
    print(colored(helpText, 'green'))
    goBack = input()
    if goBack == "":
        userHome()
    else:
        userHome()

def userHome():
    #clear
    menuStart()
    #Connecting to db
    connection = sqlite3.connect('users.db')
    c = connection.cursor()
    #Content
    Print(divider)
    Print("M E N U")
    Print(divider)
    print()
    Print("Login: Game login")
    print()
    Print("Create: Create a new account")
    print()
    Print("Help: game help screen")
    print()
    Print(divider)
    login = input(colored("                                     > ", 'green'))
    if login == "login":
        userLogin()
    if login == "create":
        addingUser()
    if login == "help":
        userHelp()
    if login == "showusers":
        c.execute("SELECT username FROM users")
        users = c.fetchall()
        print(users)
    else:
        Error("Not a valid input")
        time.sleep(1)
        userHome()

def printingInventory():
    item1 = playerProfile["1. "]
    item2 = playerProfile["2. "]
    item3 = playerProfile["3. "]
    item4 = playerProfile["4. "]
    item5 = playerProfile["5. "]
    item6 = playerProfile["6. "]
    item7 = playerProfile["7. "]
    item8 = playerProfile["8. "]
    item9 = playerProfile["9. "]
    item10 = playerProfile["10. "]
    print()
    print(colored("Inventory", 'green').center(93, ' '))
    print()
    print(colored("                                      1. " + item1, 'green'))
    print(colored("                                      2. " + item2, 'green'))
    print(colored("                                      3. " + item3, 'green'))
    print(colored("                                      4. " + item4, 'green'))
    print(colored("                                      5. " + item5, 'green'))
    print(colored("                                      6. " + item6, 'green'))
    print(colored("                                      7. " + item7, 'green'))
    print(colored("                                      8. " + item8, 'green'))
    print(colored("                                      9. " + item9, 'green'))
    print(colored("                                     10. " + item10, 'green'))


#PRINTING THE HUB
def theHub(playerName):
    menuStart()
    with open("{0}.abyss".format(playerName), 'rb') as loading:
        playerProfile = pickle.load(loading)
    weaponName = (playerProfile["playerweapon"]["weaponName"])
    armorName = (playerProfile["playerarmor"]["armorName"])
    weaponAttack = (playerProfile["playerweapon"]["weaponAttack"])
    armorDefence = (playerProfile["playerarmor"]["armorDefence"])
    weaponColour = (playerProfile["playerweapon"]["weaponColour"])
    armorColour = (playerProfile["playerarmor"]["armorColour"])
    playerHealth = playerProfile["playerhealth"]
    playerAttack = playerProfile["playerattack"]
    playerDefence = playerProfile["playerdefence"]
    playerProgress = playerProfile["playerprogress"]
    playerDeaths = playerProfile["playerdeaths"]
    playerAttackTotal = (playerAttack + weaponAttack)
    playerDefenceTotal = (playerDefence + armorDefence)
    weaponPrint = (colored(weaponName, '{0}'.format(weaponColour)).center(93, " "))
    armorPrint = (colored(armorName, '{0}'.format(armorColour)).center(93, " "))

    print(colored("{0}".format(playerName), 'green').center(93, " "))
    print()
    print(colored(topBanner, 'green').center(93, " "))
    print()
    print(weaponPrint)
    print(colored("Damage: {0}".format(weaponAttack), "green").center(93, " "))
    print()
    print(armorPrint)
    print(colored("Defence: {0}".format(armorDefence), "green").center(93, " "))
    print()
    print(colored(topBanner, 'green').center(93, " "))
    print()
    print(colored("Health: {0}".format(playerHealth), 'green').center(92, " "))
    print(colored("Attack: {0}".format(playerAttackTotal), 'green').center(92, " "))
    print(colored("Defence: {0}".format(playerDefenceTotal), 'green').center(90, " "))
    print(colored("Progress: {0}".format(playerProgress), 'green').center(92, " "))
    print(colored("Deaths: {0}".format(playerDeaths), 'green').center(90, " "))
    print()
    print(colored(topBanner, 'green').center(93, " "))
    printingInventory()
    print()
    print(colored("---------=---------", 'green').center(93, ' '))
    print(colored("Type 'start' to begin your adventure.", 'green').center(93, ' '))
    hubInput()

def hubInput():
    hubChoice = input(colored("                                        > ", 'green'))

    while hubChoice in hubChoices:
        if hubChoice == "start":
            cell()
    else:
        errorFunction()
        hubInput()

initfunction()

def hubInput():
    hubChoice = input(colored("                                        > ", 'green'))

    while hubChoice in hubChoices:
        if hubChoice == "start":
            cell()
    else:
        errorFunction()
        hubInput()

#INTRO FUNCTION_______________________________________________________

def introduction(playerName):
    menuStart()

    print(colored('"Well, well, well."', 'green').center(93, " "))
    print(colored('"look who we have here?"', 'green').center(93, " "))
    print()
    print(colored("---=---", 'green').center(93, ' '))
    time.sleep(2)

    menuStart()
    print(colored('"Lost... pity."', 'green').center(93, " "))
    print(colored('"Wondering where?"', 'green').center(93, " "))
    print()
    print(colored("---=---", 'green').center(93, ' '))
    time.sleep(2)

    menuStart()
    print(colored('"I guess i could tell you"', 'green').center(93, " "))
    print(colored('...', 'green').center(93, " "))
    print(colored('"Lets just say..."', 'green').center(93, " "))
    print()
    print(colored("---=---", 'green').center(93, ' '))
    time.sleep(2)

    menuStart()
    print(colored('"Deep into the abyss!"', 'green').center(93, " "))
    print()
    print(colored("---=---", 'green').center(93, ' '))
    time.sleep(2)

    menuStart()
    print(colored('"Will you find your way out?"', 'green').center(93, " "))
    print()
    print(colored("---=---", 'green').center(93, ' '))
    time.sleep(2)

    menuStart()
    print(colored('"OR"', 'green').center(93, " "))
    print()
    print(colored("---=---", 'green').center(93, ' '))
    time.sleep(2)

    menuStart()
    print(colored('"Will you get lost,', 'green').center(93, " "))
    print(colored('in the dark?"', 'green').center(93, " "))
    print()
    print(colored("---=---", 'green').center(93, ' '))
    time.sleep(2)

    menuStart()
    print(colored('"Are you ready?"', 'green').center(93, " "))
    print(colored("Press enter to start.", 'green').center(93, " "))
    print()
    print(colored("---=---", 'green').center(93, ' '))
    with open("save/{0}.abyss".format(playerName), 'rb') as update:
        playerInvDict = pickle.load(update)
    playerInvDict["playernew"] = False
    with open("save/{0}.abyss".format(playerName), 'wb') as addUpdate:
        pickle.dump(playerInvDict, addUpdate)
    process = input()
    if process == " ":
        theHub(playerName)
    else:
        theHub(playerName)