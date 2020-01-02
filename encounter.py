#imports
import time
import sys
from pynput import keyboard as keyboard
import random
from random import randint as roll
import signal
import termcolor
from termcolor import *
import pickle
from gameconfig import *
from descriptions import *

#Classes
#class to hold player dict
attackphrase = [
"Direct Hit!",
"Precise Strike...",
"Brutal slash!",
"Clean Hit!"
]

class player():
    attack = ""
    critical = 0
    playerInvDict = {}

#class to hold enemy stats
class eStats():
    name = ""
    health = 0
    attack = 0
    defence = 0
    alive = True
    defend = False

#Functions
def loadingProfile():
    userName = 'w4rm15h'
    with open("save/{0}.abyss".format(userName), 'rb') as loadFile:
        player.playerInvDict = pickle.load(loadFile)

def savingProfile():
    userName = 'w4rm15h'
    with open("save/{0}.abyss".format(userName), 'wb') as saveFile:
        pickle.dump(player.playerInvDict, saveFile)

def attacked():
    phrase = random.choice(attackphrase)
    player.attack = phrase

def eRoll():
    diceRoll = roll(1,3)
    eNum = diceRoll
    loadingProfile()
    choosingEnemy(eNum)

def choosingEnemy(roll):
    eNum = (str(roll))
    eStats.name = level1Enemys[eNum]["name"]
    eStats.health = level1Enemys[eNum]["health"]
    eStats.attack = level1Enemys[eNum]["attack"]
    eStats.Defence = level1Enemys[eNum]["defence"]
    enemyEncounter()

def criticalHit():
    critical = 0
    base = 100
    roll = (random.randint(0,100))
    if roll <= 6:
        player.critical = 2
    else:
        critical = 0

def enemyEncounter():
    menuStart()
    print()
    print()
    print()
    print()
    print()
    print(colored("**********", 'red').center(93, " "))
    print()
    print(colored("{0} ATTACKS!".format(eStats.name), 'green').center(93, " "))
    print()
    print(colored("**********", 'red').center(93, " "))
    print()
    print()
    print()
    print()
    print()
    print(colored(topBanner, 'green').center(93, " "))
    time.sleep(2)
    battle()

#Check to see if enemy is alive
def enemyAlive():
    if eStats.health > 0:
        eStats.alive = True
    else:
        eStats.alive = False
        enemyDead()

def enemyTurn():
    #50/50 chance if enemy attacks or defends.
    move = roll(1,2)
    if move == 1:
        enemyAttack()
    if move == 2:
        enemyDefend()

def enemyAttack():
    menuStart()
    print(colored("**********", 'red').center(93, " "))
    print(colored("*{0} attacks*", 'green').center(93, " "))
    print(colored("**********", 'red').center(93, " "))
    time.sleep(2)
    damage = eStats.attack
    player.playerInvDict[playerhealth] -= damage
    print(colored("You loose {0} health".format(damage), 'green').center(93, " "))
    savingProfile()
    battle()

def enemyDefend():
    menuStart()
    print(colored("**********", 'red').center(93, " "))
    print(colored("*{0} braces for an attack*".format(eStats.name), 'green').center(93, " "))
    print(colored("**********", 'red').center(93, " "))
    eStats.defend = True
    time.sleep(2)
    battle()

#battle function
def battle():
    #clearing screen
    menuStart()
    #Checking enemy state
    enemyAlive()
    #loading changes to profile
    loadingProfile()
    #starting while alive
    while eStats.alive == True:
        #setting shortcuts
        pName = player.playerInvDict["playername"]
        pHealth = player.playerInvDict["playerhealth"]
        #battle menu
        print(colored("-----=-----", 'green').center(93, ' '))
        print(colored("{0}'s health: {1}".format(pName, pHealth),'green').center(93, " "))
        print(colored("-----=-----", 'green').center(93, ' '))
        print(colored("{0}'s Health: {1}".format(eStats.name, eStats.health),'green').center(93, " "))
        print(colored("-----=-----", 'green').center(93, ' '))
        print()
        print(colored(topBanner, 'green').center(93, ' '))
        print()
        print(colored("Your Move", 'green').center(93, " "))
        print(colored("-----=-----", 'green').center(93, ' '))
        print(colored(topBanner, 'green').center(93, ' '))
        print(colored("1. Attack    3. Items", 'green').center(93, " "))
        print(colored("2. Defend    4. Run  ", 'green').center(93, " "))
        #player battle choice
        userAttack = input(colored("                                > ", 'green'))
        if userAttack == "1" or userAttack == "attack":
            playerAttack()
        if userAttack == "2" or userAttack == "defend":
            playerDefend()
        if userAttack == "3" or userAttack == "items":
            inventory()
        if userAttack == "4" or userAttack == "run":
            playerRun()

#player attack function
def playerAttack():
    pName = player.playerInvDict['playername']
    pHealth = player.playerInvDict['playerhealth']
    eName = eStats.name
    eHealth = eStats.health
    if eStats.defend == True:
        pDamage = (player.playerInvDict['playerattack'] + player.playerInvDict['playerweapon']['weaponAttack'])
        crit = player.critical

        totalDamage = (pDamage * crit)
        eStats.health -= eDamage
        print(colored("**********", 'red').center(93, " "))
        print(colored("*{0} blocked the attack*".format(eStats.name), 'green').center(93, " "))
        print(colored("*Damaged was signigicantly reduced*", 'red').center(93, " "))
        print(colored("**********", 'red').center(93, " "))
        time.sleep(2)
        battle()
    else:
        pDamage = player.playerInvDict['playerattack']
        criticalHit()
        eStats.health -= pDamage
        attacked()
        print(colored("**********", 'red').center(93, " "))
        print(colored("*{0} attacked {1}*".format(pName, eName), 'green').center(93, " "))
        print(colored("*{0}*".format(player.attack), 'green').center(93, " "))
        print(colored("**********", 'red').center(93, " "))
        time.sleep(2)
        battle()

def printingText(text):
    letters = list(text)
    for l in letters:
        sys.stdout.write(l)
        sys.stdout.flush()
        time.sleep(0.05)

#player defend function
def playerDefend():
    pass
#inventory function
def playerInv():
    pass
#attemping to flee from battle
def playerRun():
    pass

#if enemy health < 0
def enemyDead():
    print(colored("**********", 'red').center(93, " "))
    print()
    print(colored("{0} DEFEATED!".format(eStats.name), 'green').center(93, " "))
    print()
    print(colored("**********", 'red').center(93, " "))
    print()
    print(colored(topBanner, 'green').center(93, " "))
    time.sleep(3)

printingText(cellParagraph)
#eRoll()
