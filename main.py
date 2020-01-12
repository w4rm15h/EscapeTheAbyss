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
from cell import *

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
    userName = input(colored("                            > ", 'green'))
    c.execute("SELECT username FROM users WHERE username=?", (userName,))
    user = c.fetchall()
    if user:
        print()
        Print("Welcome, {0}".format(userName))
        #Password input
        print()
        Print("Please enter your password...")
        print()
        passWord = getpass(colored("                            > ", 'green')).encode()
        #Verifying the password
        #Pulling userpassword from db
        c.execute("SELECT key FROM users WHERE username=?", (userName,))
        hashed = c.fetchone()
        #checking password against input
        if bcrypt.checkpw(passWord, hashed[0]):
            menuStart()
            Print("Welcome {0}".format(userName))
            Print(divider)
            print()
            #Connecting to FTP server and retrieve user save file
            loadProfile(userName)
            with open("{0}.abyss".format(userName), 'rb') as load:
                gameVars.playerProfile = pickle.load(load)
            #Proceed to hub
            if gameVars.playerProfile['playernew'] == True:
                introduction(userName)
            else:
                theHub(userName)
        else:
            print()
            Error("*Incorrect Username or Password*")
            time.sleep(2)
            userLogin()
    else:
        print()
        Error("Can't find you... ahhh!!!")
        time.sleep(1.5)
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
    userName = input(colored("                            > ", 'green'))
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
    pWord1 = getpass(colored("                            > ", 'green'))
    print()
    Print("One more time...")
    print()
    pWord2 = getpass(colored("                            > ", 'green'))
    while pWord1 != pWord2:
        print()
        Error("Passwords do not match...")
        Error("Try again....")
        print()
        Print("Enter your password")
        Print("Your password will not display")
        print()
        pWord1 = getpass(colored("                            > ", 'green'))
        Print("One more time...")
        print()
        pWord2 = getpass(colored("                            > ", 'green'))
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
    print()
    Print("      M E N U")
    Print('      ' + divider)
    print()
    Print("Login: Game login")
    print()
    Print("Create: Create a new account")
    print()
    Print("Help: game help screen")
    print()
    Print(divider)

    loggingIn = 1
    while loggingIn == 1:

        login = input(colored("                            > ", 'green'))

        if login == "login":
            userLogin()
        if login == "create":
            addingUser()
        if login == "help":
            userHelp()

        else:
            print()
            errorResponse()
            print()

#PRINTING THE HUB
def theHub(userName):
    menuStart()
    print()
    printStats()
    printInventory()
    Print("Type *start* or *begin*")
    print()

    whileLoop = 1
    while whileLoop == 1:

        hubChoice = input(colored("                            > ", 'green'))   
        if hubChoice == "start" or "begin":
            if gameVars.playerProfile['playernew'] == True:
                cellIntroduction(userName)
            else:
                cellInit(userName)
        else:
            errorResponse()
            print()

#INTRO FUNCTION_______________________________________________________

def introduction(userName):
    textPrinting()

    print(colored('"Well, well, well."', 'green').center(93, " "))
    print(colored('"look who we have here?"', 'green').center(93, " "))
    print()
    print(colored("---=---", 'green').center(93, ' '))
    time.sleep(2)

    textPrinting()
    print(colored('"Lost... pity."', 'green').center(93, " "))
    print(colored('"Wondering where?"', 'green').center(93, " "))
    print()
    print(colored("---=---", 'green').center(93, ' '))
    time.sleep(2)

    textPrinting()
    print(colored('"I guess i could tell you"', 'green').center(93, " "))
    print(colored('...', 'green').center(93, " "))
    print(colored('"Lets just say..."', 'green').center(93, " "))
    print()
    print(colored("---=---", 'green').center(93, ' '))
    time.sleep(2)

    textPrinting()
    print(colored('"Deep into the abyss!"', 'green').center(93, " "))
    print()
    print(colored("---=---", 'green').center(93, ' '))
    time.sleep(2)

    textPrinting()
    print(colored('"Will you find your way out?"', 'green').center(93, " "))
    print()
    print(colored("---=---", 'green').center(93, ' '))
    time.sleep(2)

    textPrinting()
    print(colored('"OR"', 'green').center(93, " "))
    print()
    print(colored("---=---", 'green').center(93, ' '))
    time.sleep(2)

    textPrinting()
    print(colored('"Will you get lost,', 'green').center(93, " "))
    print(colored('in the dark?"', 'green').center(93, " "))
    print()
    print(colored("---=---", 'green').center(93, ' '))
    time.sleep(2)

    textPrinting()
    print(colored('"Are you ready?"', 'green').center(93, " "))
    print(colored("Press enter to start.", 'green').center(93, " "))
    print()
    print(colored("---=---", 'green').center(93, ' '))

    cont = input()
    if cont == "":
        theHub(userName)
    else:
        Error("*sigh*")
        Error("I said press enter...")
        time.sleep(1)
        theHub(userName)

initfunction()