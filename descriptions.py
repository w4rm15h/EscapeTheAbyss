title = """
▄▄▄ ..▄▄ ·  ▄▄·  ▄▄▄·  ▄▄▄·▄▄▄ .    ▄▄▄▄▄ ▄ .▄▄▄▄ .     ▄▄▄· ▄▄▄▄·  ▄· ▄▌.▄▄ · .▄▄ ·
▀▄.▀·▐█ ▀. ▐█ ▌▪▐█ ▀█ ▐█ ▄█▀▄.▀·    •██  ██▪▐█▀▄.▀·    ▐█ ▀█ ▐█ ▀█▪▐█▪██▌▐█ ▀. ▐█ ▀.
▐▀▀▪▄▄▀▀▀█▄██ ▄▄▄█▀▀█  ██▀·▐▀▀▪▄     ▐█.▪██▀▐█▐▀▀▪▄    ▄█▀▀█ ▐█▀▀█▄▐█▌▐█▪▄▀▀▀█▄▄▀▀▀█▄
▐█▄▄▌▐█▄▪▐█▐███▌▐█ ▪▐▌▐█▪·•▐█▄▄▌     ▐█▌·██▌▐▀▐█▄▄▌    ▐█ ▪▐▌██▄▪▐█ ▐█▀·.▐█▄▪▐█▐█▄▪▐█
 ▀▀▀  ▀▀▀▀ ·▀▀▀  ▀  ▀ .▀    ▀▀▀      ▀▀▀ ▀▀▀ · ▀▀▀      ▀  ▀ ·▀▀▀▀   ▀ •  ▀▀▀▀  ▀▀▀▀

"""

topBanner = "---------=---------"
divider = "---=---"

swordImage = """
                                    /\
                                   // \
                                   || |
                                   || |
                                   || |
                                   || |
                                   || |
                                   || |
                                   || |
                                   || |
                                   || |
                                   || |
                                   || |
                                   || |
                                __ || | __
                               /____**____\
                                    XX
                                    XX
                                   _XX_
                                  (0000)
                                   \  /
                                    \/

"""

#Reference for playerProfile
playerProfile = {

    "playername": "Player 1",
    "playermaxhealth": 100,
    "playerhealth": 100,
    "playerprogress": "Empty",
    "playerweapon":{
            "weaponGrade": "Empty",
            "weaponName": "No Weapon",
            "weaponAttack": 0,
            "weaponColour": "green",
                },
    "playerarmor":{
            "armorGrade": "Empty",
            "armorName": "No Armor",
            "armorDefence": 0,
            "armorColour": "green",
                },
    "healingitems":{
            "potion": 0,
                },
    "playerattack": 0,
    "playerdefence": 0,
    "playerdeaths": 0,
    "playernew": True,
    "inventory": {
            "1. ": "Empty",
            "2. ": "Empty",
            "3. ": "Empty",
            "4. ": "Empty",
            "5. ": "Empty",
            "6. ": "Empty",
            "7. ": "Empty",
            "8. ": "Empty",
            "9. ": "Empty",
            "10. ": "Empty",
        }
}   

#Player key commands
playerCommands = [
    'inventory',
    'stats',
    'use',
    'drop',
    'move',
    'drink',
]

greetings = [

    'hello',
    'hellothere',
]
#Enemy Encounters_________________________________________
level1Enemys = {

    "1":{
        "name": "SPIDER",
        "health": 100,
        'attack': 20,
        "defence": 10,
        },
    "2":{
        "name": "IMP",
        "health": 100,
        'attack': 20,
        "defence": 11,
        },
    "3":{
        "name": "DEMON",
        "health": 100,
        'attack': 20,
        "defence": 12,
        }

}

# ACCEPTED INPUTS_________________________________________

yes = [

    "y",
    "Y",
    "yes",
    "yep",
    'fucking oath',
    "bring it on"
]

no = [

    "n",
    "N",
    "nope",
    "nah"
]

back = [

    "back",
    "head back",
    "go back",
    "backspace",
    "backwards",
    "return"
]

swear = [

    "fuck",
    "cunt",
    "ass",
    "butt",
    "tits",
    "motherfucker",
    "asscheese",
    "piss"

]

verbs = [

    "go",
    "kick",
    "check",
    "jump",
    "read",
    "take",
    "use",
    "exit",
    "move",
    "drop"
]

objects = [

    "north",
    "east",
    "south",
    "west",
    "door",
    "window",
    "wall",
    "brick",
    "note",
    "key",
    "playerInvDict"

]

hubChoices = [

    "start",
    "begin",
    "password"

]

startSword = {

    "common": (10,12),
    "rare": (12,14),
    "mystic": (14,16),
    "legendary": (16,20)

}

oneToTen = [

    "1",
    "2",
    "3",
    "4",
    "5",
    "6",
    "7",
    "8",
    "9",
    "10"

]

drinkingPotionText = """
                            You pull the cork off the small vile,
                            The smell is unpleasent,
                            you open your mouth and empty the
                            vile. You almost instantly feel
                            refreshed and healthy.
                            Alright, Let's continue...
"""

errorOutputs = [

    "Pity, such a simple creation",
    "That is not possible right now",
    "Maybe choose an option that will help...",
    "Shame... can't even perform such a simple task",
    "Come on, Focus!"

]

helpText = """
                            Welcome to Escape the Abyss.

                            To Begin either type; login or create at
                            the main menu, to return to the main menu
                            just press enter.

                            Make your way through the Abyss by solving
                            puzzles and defeating the enemys
                            that try to stand in your way.

                            To control your character, simply just
                            type what you want him/her to do. e.g.
                            check the window.
                            unlock the door.
                            pickup potion.
                            For yes and no inputs,
                            you can type most ways to say yes
                            and no... in english. it should understand.
                            There are secret phrases you can enter,
                            the game will respond to bad language so be
                            sure to give that a try.
                            For everything else, just pay attention, 
                            the way to proceed is always hinted in
                            some way, shape or form.

                            If you die during the game, you will
                            be placed back at the beginning.
                            You will keep the weapons, armor and
                            items you collect along the way to make
                            progressing the next time that little
                            bit easier, though this will still be a
                            challenge.

                            You are assigned an attack and defence
                            number decided by a dice roll.
                            To increase these values seek and find
                            weapons through-out the levels.

                            Weapons and Armor:

                            You will find weapons and armor through
                            your travels, each time you aquire one
                            it is given a grade.
                            Common: a common item, standard stats.
                            Uncommon: an uncommon item, slightly increased stats.
                            Rare: A rare item, much better stats.
                            LEGENDARY: LEGENDARY, if you are lucky enough
                            to come across a weapon with these stats, 
                            your battles will be much easier.

                            Items:

                            You will come accross items in your
                            journey also, some items will restore
                            you health, some will unlock and some will
                            complete puzzels.
                            You can hold up to 10 items at any time, 
                            these will be saved upon death.
                            So be sure to manage your inventory bye typing
                            "inventory" at any point during game play.


                            GOOD LUCK."""


#LEVEL1 - CELL _________________________________________

cellOpen = """ 
                            You wake to find yourself in a small,
                            dark jailcell.
                            Terrible things have happened here,
                            faint sounds of screams haunt the long, narrow,
                            stone hallways. The old cell doors
                            lie direcetly NORTH, their bars rusty,
                            weakened with age.
                            Fingernail scratchings, torn deep into the EAST wall,
                            casting warped, disturbing shadows.
                            To the SOUTH, a small WINDOW, providing
                            an ominious blue glow, that helps illuminate
                            the small cell but also provides a chilling breeze.
                            A wooden desk is chained and bolted to
                            the shadowy WEST wall.
                            Despite the rot in the old wood,
                            The dust on top was fresh.
                            Someone was in here... Recently."""

cellNorth = """
                            You walk up to the cell door and wrap your
                            hands around the old bars.
                            You can feel the rust digging into your
                            skin, all you see is darkness.
                            Screams and groans echoing through the
                            hallways."""

cellEast = """
                            You slowly walk up to the wall
                            and run your fingers down the
                            scrathes. They somewhat resemble
                            an arrow pointing to a odd
                            looking brick in the wall.
"""
cellSouth = """
                            You turn around and look at the
                            window.
                            The bars looked cold, frozen.
                            The window is high, though it
                            seems it might be in reach."""

cellWest = """
                            The desk, just sitting there,
                            Rotting and beaten by old age.
                            The dust on top, fresh.
                            Someone was in here, recently."""

cellBrick = """
                            You grip the edge of the
                            odd looking brick.
                            You pull out the brick,
                            revealing a note and a potion."""

cellNote = """
                            A quick TIP to help you
                            along your travels.
                            Keep the text lowercase.
                            Use words like:
                            go north,
                            kick door,
                            Use key,
                            to interact with your
                            surroundings.
                            You fold the note and
                            place it back in the hole.
                            Just incase..."""

cellWindow = """
                            You jump and hold the glaciated
                            bars blocking the window.
                            Your hands can't get a good grip,
                            but you manage to get a look outside.
                            It's a giant lake, frozen over.
                            souls are frozen in the lake,
                            with only thier necks and heads
                            pertruding the surface.
                            The souls here, stuck, without
                            even the small comfort of thier
                            own tears."""


unlockingCellDoor = """
                            You walk up to the door
                            and place the key in the lock.
                            you twist the key slowly trying
                            not to make to much noise,
                            trying to avoid alerting any
                            potential enemys.
                            The cell door unlocks.
                            You put the key back and
                            place the brick back into
                            the exposed hole.
                            It seems like the right
                            thing to do.
                            You step out of the cell,
                            closing the door behind
                            you."""


#LEVEL 1 - PART 2 ________________________________________________________________

level1Hallway1 = """
                            The air whistles past your ears flowing
                            fast to the NORTH, it was a long hallway,
                            leading off the right.
                            the walls leading high up into the darkness.
                            Behind you to the SOUTH is the small, dark
                            cell you just excaped from.
                            You hear a whisper 'Thisssssss wayyyyyy',
                            pulling your head to the WEST.
                            The hallway was narrow, eary and dark,
                            very dark. There is a light at the end
                            though, though is does seem far,
                            it."""

