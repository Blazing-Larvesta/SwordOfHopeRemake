#NPCs
define theo = Character("Theo")
define oldman = Character("Old Man")
define shaman = Character("Shaman")
define martel = Character("Martel")
define shabow = Character("Shabow")
define camu = Character("Camu")
define shopkeeper = Character("Shopkeeper")
define queen = Character("Queen Remy")
define unknown = Character("???")

# Monsters
define moth = Character("Moth", image="moth", monsterhp = 3, monstermp = 0, monsterdex = 1, monsterstam = 1, monsteragil = 1, monstergolddrop = 1, monsterexpdrop = 1, escapable = True)
define skeleton = Character("Floating Skull", image="skeleton", monsterhp = 4, monstermp = 3, monsterdex = 1, monsterstam = 1, monsteragil = 1, monstergolddrop = 2, monsterexpdrop = 3, escapable = True)
define treant = Character("Treant", image="treant")
define king = Character("King Hennessy", image="theking")

label bestiary:
    if monsternumber == 1:
        $ monstersprite = "moth"
        $ monstername = "Moth"
        $ monsterhp = 3
        $ monstermp = 0
        $ monsterdex = 1
        $ monsterstam = 1
        $ monsteragil = 1
        $ monstergolddrop = 1
        $ monsterexpdrop = 1
        $ escapable = True
    elif monsternumber == 2:
        $ monstersprite = "skeleton"
        $ monstername = "Floating Skull"
        $ monsterhp = 4
        $ monstermp = 3
        $ monsterdex = 1
        $ monsterstam = 1
        $ monsteragil = 1
        $ monstergolddrop = 2
        $ monsterexpdrop = 3
        $ escapable = True
    elif monsternumber == 3:
        $ monstersprite = "treant"
        $ monstername = "The Treant"
        $ monsterhp = 40
        $ monstermp = 10
        $ monsterdex = 15
        $ monsterstam = 15
        $ monsteragil = 15
        $ monstergolddrop = 6
        $ monsterexpdrop = 12
        $ escapable = False
    elif monsternumber == 4:
        $ monstersprite = "elemental.png"
        $ monstername = "Explosive Fiend"
        $ monsterhp = 1
        $ monstermp = 0
        $ monsterdex = 1
        $ monsterstam = 1
        $ monsteragil = 1
        $ monstergolddrop = 2
        $ monsterexpdrop = 4
        $ escapable = True
    elif monsternumber == 5:
        $ monstersprite = "bigbat.png"
        $ monstername = "Big Bat"
        $ monsterhp = 8
        $ monstermp = 0
        $ monsterdex = 1
        $ monsterstam = 1
        $ monsteragil = 1
        $ monstergolddrop = 3
        $ monsterexpdrop = 7
        $ escapable = True
    elif monsternumber == 6:
        $ monstersprite = "goblin.png"
        $ monstername = "Goblin"
        $ monsterhp = 25
        $ monstermp = 0
        $ monsterdex = 1
        $ monsterstam = 1
        $ monsteragil = 1
        $ monstergolddrop = 5
        $ monsterexpdrop = 10
        $ escapable = True
    elif monsternumber == 7:
        $ monstersprite = "mimic.png"
        $ monstername = "Mimic"
        $ monsterhp = 46
        $ monstermp = 0
        $ monsterdex = 1
        $ monsterstam = 1
        $ monsteragil = 1
        $ monstergolddrop = 2
        $ monsterexpdrop = 3
        $ escapable = False
    elif monsternumber == 8:
        $ monstersprite = "slug.png"
        $ monstername = "Slug"
        $ monsterhp = 48
        $ monstermp = 0
        $ monsterdex = 1
        $ monsterstam = 1
        $ monsteragil = 1
        $ monstergolddrop = 7
        $ monsterexpdrop = 18
        $ escapable = True
    elif monsternumber == 9:
        $ monstersprite = "ape.png"
        $ monstername = "Mage Gorilla"
        $ monsterhp = 19
        $ monstermp = 15
        $ monsterdex = 20
        $ monsterstam = 30
        $ monsteragil = 20
        $ monstergolddrop = 6
        $ monsterexpdrop = 13
        $ escapable = True
    elif monsternumber == 10:
        $ monstersprite = "cyclops.png"
        $ monstername = "Cyclops"
        $ monsterhp = 24
        $ monstermp = 0
        $ monsterdex = 30
        $ monsterstam = 30
        $ monsteragil = 18
        $ monstergolddrop = 7
        $ monsterexpdrop = 16
        $ escapable = True
    elif monsternumber == 11:
        $ monstersprite = "frog.png"
        $ monstername = "Frog"
        $ monsterhp = 25
        $ monstermp = 0
        $ monsterdex = 1
        $ monsterstam = 1
        $ monsteragil = 1
        $ monstergolddrop = 5
        $ monsterexpdrop = 10
        $ escapable = True
    elif monsternumber == 12:
        $ monstersprite = "eel.png"
        $ monstername = "Eel"
        $ monsterhp = 45
        $ monstermp = 0
        $ monsterdex = 1
        $ monsterstam = 1
        $ monsteragil = 1
        $ monstergolddrop = 10
        $ monsterexpdrop = 15
    elif monsternumber == 13:
        $ monstersprite = "larva.png"
        $ monstername = "Fiendish Grub"
        $ monsterhp = 45
        $ monstermp = 0
        $ monsterdex = 1
        $ monsterstam = 1
        $ monsteragil = 1
        $ monstergolddrop = 8
        $ monsterexpdrop = 19
        $ escapable = True
    elif monsternumber == 14:
        $ monstersprite = "myconid.png"
        $ monstername = "Fungal Beast"
        $ monsterhp = 49
        $ monstermp = 0
        $ monsterdex = 1
        $ monsterstam = 1
        $ monsteragil = 1
        $ monstergolddrop = 9
        $ monsterexpdrop = 18
        $ escapable = True
    elif monsternumber == 15:
        $ monstersprite = "shadow.png"
        $ monstername = "Shadow Creature"
        $ monsterhp = 56
        $ monstermp = 0
        $ monsterdex = 1
        $ monsterstam = 1
        $ monsteragil = 1
        $ monstergolddrop = 12
        $ monsterexpdrop = 27
        $ escapable = True
    elif monsternumber == 16:
        $ monstersprite = "lizard.png"
        $ monstername = "Lizard"
        $ monsterhp = 60
        $ monstermp = 0
        $ monsterdex = 1
        $ monsterstam = 1
        $ monsteragil = 1
        $ monstergolddrop = 13
        $ monsterexpdrop = 30
        $ escapable = True
    elif monsternumber == 17:
        $ monstersprite = "orc.png"
        $ monstername = "Orc"
        $ monsterhp = 46
        $ monstermp = 0
        $ monsterdex = 1
        $ monsterstam = 1
        $ monsteragil = 1
        $ monstergolddrop = 10
        $ monsterexpdrop = 19
        $ escapable = True
    elif monsternumber == 18:
        $ monstersprite = "lamia.png"
        $ monstername = "Lamia"
        $ monsterhp = 100
        $ monstermp = 0
        $ monsterdex = 1
        $ monsterstam = 1
        $ monsteragil = 1
        $ monstergolddrop = 42
        $ monsterexpdrop = 42
        $ escapable = False
    elif monsternumber == 19:
        $ monstersprite = "yeti.png"
        $ monstername = "Abominable Snowman"
        $ monsterhp = 100
        $ monstermp = 0
        $ monsterdex = 1
        $ monsterstam = 1
        $ monsteragil = 1
        $ monstergolddrop = 100
        $ monsterexpdrop = 45
        $ escapable = False
    elif monsternumber == 20:
        $ monstersprite = "imp.png"
        $ monstername = "Greedy Imp"
        $ monsterhp = 100
        $ monstermp = 0
        $ monsterdex = 1
        $ monsterstam = 1
        $ monsteragil = 1
        $ monstergolddrop = 1
        $ monsterexpdrop = 38
        $ escapable = False
    elif monsternumber == 21:
        $ monstersprite = "mudman.png"
        $ monstername = "The Mudman"
        $ monsterhp = 100
        $ monstermp = 0
        $ monsterdex = 1
        $ monsterstam = 1
        $ monsteragil = 1
        $ monstergolddrop = 150
        $ monsterexpdrop = 36
        $ escapable = False
    elif monsternumber == 22:
        $ monstersprite = "vampire.png"
        $ monstername = "Vampire"
        $ monsterhp = 163
        $ monstermp = 0
        $ monsterdex = 1
        $ monsterstam = 1
        $ monsteragil = 1
        $ monstergolddrop = 150
        $ monsterexpdrop = 36
        $ escapable = False
    elif monsternumber == 23:
        $ monstersprite = "bogle.png"
        $ monstername = "Bogle"
        $ monsterhp = 38
        $ monstermp = 0
        $ monsterdex = 1
        $ monsterstam = 1
        $ monsteragil = 1
        $ monstergolddrop = 30
        $ monsterexpdrop = 21
        $ escapable = True
    elif monsternumber == 24:
        $ monstersprite = "mimic2.png"
        $ monstername = "Magic Mimic"
        $ monsterhp = 60
        $ monstermp = 50
        $ monsterdex = 40
        $ monsterstam = 40
        $ monsteragil = 50
        $ monstergolddrop = 50
        $ monsterexpdrop = 40
        $ escapable = False
    elif monsternumber == 25:
        $ monstersprite = "hag.png"
        $ monstername = "Wretched Hag"
        $ monsterhp = 80
        $ monstermp = 0
        $ monsterdex = 40
        $ monsterstam = 40
        $ monsteragil = 40
        $ monstergolddrop = 11
        $ monsterexpdrop = 37
        $ escapable = True
    elif monsternumber == 26:
        $ monstersprite = "centipede.png"
        $ monstername = "Centipede"
        $ monsterhp = 65
        $ monstermp = 30
        $ monsterdex = 30
        $ monsterstam = 30
        $ monsteragil = 30
        $ monstergolddrop = 20
        $ monsterexpdrop = 40
        $ escapable = True
    elif monsternumber == 27:
        $ monstersprite = "druid.png"
        $ monstername = "Heretic"
        $ monsterhp = 100
        $ monstermp = 0
        $ monsterdex = 50
        $ monsterstam = 60
        $ monsteragil = 65
        $ monstergolddrop = 70
        $ monsterexpdrop = 40
        $ escapable = True
    elif monsternumber == 28:
        $ monstersprite = "grimlock.png"
        $ monstername = "Grimlock"
        $ monsterhp = 80
        $ monstermp = 0
        $ monsterdex = 1
        $ monsterstam = 1
        $ monsteragil = 1
        $ monstergolddrop = 17
        $ monsterexpdrop = 44
        $ escapable = True
    elif monsternumber == 29:
        $ monstersprite = "mimic3.png"
        $ monstername = "Dark Mimic"
        $ monsterhp = 100
        $ monstermp = 0
        $ monsterdex = 1
        $ monsterstam = 1
        $ monsteragil = 1
        $ monstergolddrop = 50
        $ monsterexpdrop = 50
        $ escapable = False
    elif monsternumber == 30:
        $ monstersprite = "theking.png"
        $ monstername = "King Hennessy"
        $ monsterhp = 110
        $ monstermp = 100
        $ monsterdex = 100
        $ monsterstam = 100
        $ monsteragil = 100
        $ monstergolddrop = 0
        $ monsterexpdrop = 0
        $ escapable = False
    elif monsternumber == 31:
        $ monstersprite = "dragon.png"
        $ monstername = "The Dark Dragon"
        $ monsterhp = 250
        $ monstermp = 250
        $ monsterdex = 100
        $ monsterstam = 100
        $ monsteragil = 100
        $ monstergolddrop = 0
        $ monsterexpdrop = 0
        $ escapable = False
    elif monsternumber == 32:
        $ monstername = "The Weapon Master"
        $ monsterhp = 150
        $ monstermp = 0
        $ monsterdex = 1
        $ monsterstam = 1
        $ monsteragil = 1
        $ monstergolddrop = 100
        $ monsterexpdrop = 100
        $ escapable = False
    elif monsternumber == 33:
        $ monstername = "The Marksman Chief"
        $ monsterhp = 150
        $ monstermp = 0
        $ monsterdex = 1
        $ monsterstam = 1
        $ monsteragil = 1
        $ monstergolddrop = 100
        $ monsterexpdrop = 100
        $ escapable = False
    elif monsternumber == 34:
        $ monstername = "The Swift Slasher"
        $ monsterhp = 150
        $ monstermp = 0
        $ monsterdex = 1
        $ monsterstam = 1
        $ monsteragil = 1
        $ monstergolddrop = 100
        $ monsterexpdrop = 100
        $ escapable = False
    elif monsternumber == 35:
        $ monstername = "The Irontight Knight"
        $ monsterhp = 150
        $ monstermp = 0
        $ monsterdex = 1
        $ monsterstam = 1
        $ monsteragil = 1
        $ monstergolddrop = 100
        $ monsterexpdrop = 100
        $ escapable = False
    elif monsternumber == 36:
        $ monstername = "Mute"
        $ monsterhp = 150
        $ monstermp = 0
        $ monsterdex = 1
        $ monsterstam = 1
        $ monsteragil = 1
        $ monstergolddrop = 100
        $ monsterexpdrop = 100
        $ escapable = False
    elif monsternumber == 37:
        $ monstername = "Layl"
        $ monsterhp = 150
        $ monstermp = 0
        $ monsterdex = 1
        $ monsterstam = 1
        $ monsteragil = 1
        $ monstergolddrop = 100
        $ monsterexpdrop = 100
        $ escapable = False
    elif monsternumber == 38:
        $ monstername = "Nina"
        $ monsterhp = 150
        $ monstermp = 0
        $ monsterdex = 1
        $ monsterstam = 1
        $ monsteragil = 1
        $ monstergolddrop = 100
        $ monsterexpdrop = 100
        $ escapable = False
    elif monsternumber == 39:
        $ monstername = "Bogi"
        $ monsterhp = 150
        $ monstermp = 0
        $ monsterdex = 1
        $ monsterstam = 1
        $ monsteragil = 1
        $ monstergolddrop = 100
        $ monsterexpdrop = 100
        $ escapable = False
    elif monsternumber == 40:
        $ monstername = "Buglivia"
        $ monsterhp = 300
        $ monstermp = 150
        $ monsterdex = 200
        $ monsterstam = 200
        $ monsteragil = 200
        $ monstergolddrop = 255
        $ monsterexpdrop = 500
        $ escapable = False
    elif monsternumber == 41:
        $ monstername = "Zakdos"
        $ monsterhp = 300
        $ monstermp = 300
        $ monsterdex = 300
        $ monsterstam = 300
        $ monsteragil = 300
        $ monstergolddrop = 0
        $ monsterexpdrop = 0
        $ escapable = False
    else:
        $ monstername = "Null"
        $ monsterhp = 0
        $ monstermp = 0
        $ monsterdex = 0
        $ monsterstam = 0
        $ monsteragil = 0
        $ monstergolddrop = 0
        $ monsterexpdrop = 0
        $ escapable = True
    jump battleSetup

label start:
# Variable Initialization
# RNG
    $ d2 = renpy.random.randint(1, 2)
    $ d4 = renpy.random.randint(1, 4)
    $ d6 = renpy.random.randint(1, 6)
    $ d10 = renpy.random.randint(1, 10)
    $ d20 = renpy.random.randint(1, 20)
    $ d24 = renpy.random.randint(1, 24) #Calculate Turn Order
    $ monsterEncounter = 0

# Stats
    $ roomNumber = 0
    $ level = 1
    $ hp = 20
    $ maxhp = 20
    $ mp = 20
    $ maxmp = 20
    $ baseDexterity = 0
    $ baseStamina = 0
    $ baseAgility = 0
    $ swordDexBoost = 0
    $ armorStamBoost = 0
    $ dexAlter = 0
    $ stamAlter = 0
    $ agilAlter = 0
    $ gold = 0
    $ exp = 0
    $ toNext = 9999
    $ totalTurns = 0
    $ turnCounter = 0
    $ gameOver = False
    $ statCheck = False
    $ enemy1value = 0
    $ enemy2value = 0
    $ enemy3value = 0
    $ enemy1hp = 0
    $ enemy2hp = 0
    $ enemy3hp = 0
    $ enemy1dex = 0
    $ enemy2dex = 0
    $ enemy3dex = 0
    $ enemy1stam = 0
    $ enemy2stam = 0
    $ enemy3stam = 0
    $ enemy1agil = 0
    $ enemy2agil = 0
    $ enemy3agil = 0
    $ enemy1expdrop = 0
    $ enemy2expdrop = 0
    $ enemy3expdrop = 0
    $ enemy1golddrop = 0
    $ enemy2golddrop = 0
    $ enemy3golddrop = 0
    $ enemy1number = 0
    $ enemy2number = 0
    $ enemy3number = 0
    $ target = 0
    $ playermoved = False
    $ enemy1moved = False
    $ enemy2moved = False
    $ enemy3moved = False
    $ enemy1name = "Null"
    $ enemy2name = "Null"
    $ enemy3name = "Null"
    $ monstersprite = "Null"
    $ enemy1sprite = "Null"
    $ enemy2sprite = "Null"
    $ enemy3sprite = "Null"
    $ monstername = "Null"
    $ monsternumber = 0
    $ monsterhp = 0
    $ monstermp = 0
    $ monsterdex = 0
    $ monsterstam = 0
    $ monsteragil = 0
    $ monstergolddrop = 0
    $ monsterexpdrop = 0
    $ enemypool = 0
    $ monsterssetup = 0
    $ escapable = True

# Spell Unlocks
    $ teleportUnlocked = True # Available from start; should never be False
    $ graceUnlocked = False # Obtain from forest merchant
    $ secretUnlocked = False # Obtain in underground castle
    $ fireball1Unlocked = False
    $ fireball2Unlocked = False
    $ fireball3Unlocked = False
    $ fireball4Unlocked = False
    $ tornado1Unlocked = False
    $ tornado2Unlocked = False
    $ tornado3Unlocked = False
    $ tornado4Unlocked = False
    $ explosion1Unlocked = False
    $ explosion2Unlocked = False
    $ lightning1Unlocked = False
    $ lightning2Unlocked = False
    $ lightning3Unlocked = False
    $ lightning4Unlocked = False
    $ arctic1Unlocked = False
    $ arctic2Unlocked = False
    $ drainHealthUnlocked = False
    $ sapMPUnlocked = False
    $ sapAllUnlocked = False
    $ drainMagicUnlocked = False
    $ blindUnlocked = False
    $ drainDexUnlocked = False
    $ drainAgilStamUnlocked = False
    $ raiseAgilUnlocked = False
    $ raiseDexUnlocked = False
    $ raiseStamUnlocked = False
    $ recoverMinUnlocked = False
    $ recoverMedUnlocked = False
    $ recoverMaxUnlocked = False

# Inventory
    $ swordLevel = 1
    $ armorLevel = 1
    $ barleysOwned = 0
    $ wheatsOwned = 1
    $ herbsOwned = 1
    $ charmObtained = False
    $ rubyObtained = False
    $ sporeObtained = False
    $ dollObtained = False
    $ moonFragmentObtained = False
    $ sapphireObtained = False
    $ ringObtained = False
    $ unicornHornObtained = False
    $ fairyLampObtained = False
    $ ivySeedObtained = False
    $ keyMObtained = False
    $ keySObtained = False
    $ keyCObtained = False
    $ whiteEggObtained = False
    $ blueEggObtained = False
    $ redEggObtained = False
    $ treantFruitObtained = False
    $ yellowFruitObtained = False

# Teleports
    $ martelFound = False
    $ shabowFound = False
    $ camuFound = False
    $ castleFound = False
    $ finalBossFound = False

# Other Story Checks
    $ doorMOpened = False
    $ doorSOpened = False
    $ doorCOpened = False
    $ treesSpoken = False
    $ room9Herb = False
    $ shopkeepVisits = 0
    $ graceRoomUnlocked = False
    $ moonCompleted = False
    $ millstonePushed = False
    $ secretWorldUnlocked = False

    stop music
    scene bg black
    scene bg prologue with dissolve
    play music "prologue.mp3"

    "This is a legend of one who was chosen by destiny; a hero who must claim a Sword of Hope, destroy a looming darkness, and return the light of his kingdom."
    "Once, there was a brave king, ruler of the peaceful country of Riccar."
    "Though beloved by his subjects, the king was one day overwhelmed by the power of an evil dragon."
    "This dragon had once been bound by the hex of a sword thrust into the heart of his likeness."
    "However, the beast was able to instill strong visions of wisdom and power in the king, bringing forth the hidden evil in his heart, and taking complete control over him."
    "The possessed king was urged to remove the damning sword from the ancient painting, spilling darkness throughout Riccar."
    "As people feared the corrupted king more and more, the country declined drastically."
    "The dragon summoned the evil power Mammon, who cursed the people to become trees."
    "Throughout the dark times, the people held onto a ray of light: the birth of Prince Theo!"
    "The king grew angry at his child, for on Theo's left arm was a birthmark shaped like a dagger!"
    "Filled with rage, the king attempted to bring his sword down upon the prince. It is only thanks to the intervention of the brave knight Pascal that Theo was spared."
    "Pascal had fled to the forest with Prince Theo, hoping to seek the aid of the three powerful magicians who banished the king and his castle underground."
    "One of them had retrieved the banished Sword of Hope, and the three magicians had secured themselves behind locked gates."
    "Time has passed... The tide is turning."
    "A truly important mission awaits Prince Theo."

    scene bg black with dissolve

    scene bg oldmanroom
    show oldman
    with dissolve
    $ roomNumber = 1
    play music "oldmanroom.mp3"

    oldman "Theo! You are finally big enough to live on your own."
    theo "Many thanks! I wouldn't have made it this far without you."
    oldman "I've waited until this day to tell you an important truth. Listen well."
    oldman "The darkness rules this country, and changed its people into trees."
    oldman "Only one of royal blood can save the forsaken king from the darkness..."
    oldman "And that hero is you!"
    theo "Me...?"
    oldman "Indeed, you, Prince Theo. You are the Chosen One, selected to wield the Sword of Hope!"
    theo "I... had a hunch, to be honest."
    oldman "One of the three magicians has the Sword of Hope needed to destroy the darkness."
    oldman "All of them have locked the gates of their lands strongly, and meant to send the keys to you through their pigeons."
    theo "Then where are these keys?"
    oldman "Unfortunately, they were all intercepted by helpers of the darkness to trap you in this forest."
    theo "Then I'll just have to find and retrieve them."
    oldman "Theo... This will be a hard journey, but you must locate the Sword of Hope!"
    oldman "If you find yourself wearing thin, then my neighbor, the Shaman, can soothe your wounds. Your teleport spell can bring you back to the two of us."
    oldman "Now, get ready for your travel. Good luck!"
    theo "Thanks, old man! I'll be careful out there!"
    play sound "itemacquired.mp3"
    "Theo equips the copper armor and probite sword, and begins his journey!"
    play sound "itemacquired.mp3"
    "He brings white wheat, an herb, and his trusty magic book with him!"

    jump levelCheck

label levelCheck:
    if toNext <= 0 and level < 32: #Exp. check is updating, but level is not going up
        $ level += 1
        $ maxhp += 4
        $ maxmp += 2
        $ baseDexterity += 2
        $ baseStamina += 3
        $ baseAgility += 2
        play sound "levelupmagic.mp3"
        "You have been promoted to the next level! You are now Level [level]!"
        if level <= 21 or level == 23:
            "You have learned a new spell! Check it out in the magic book!"

    if exp < 10:
        $ level = 1
        $ toNext = 10 - exp
        $ maxhp = 20
        $ maxmp = 20
        $ baseDexterity = 7
        $ baseStamina = 8
        $ baseAgility = 12
    elif exp < 35:
        $ toNext = 35 - exp
        $ fireball1Unlocked = True
    elif exp < 85:
        $ toNext = 85 - exp
        $ sapAllUnlocked = True
    elif exp < 165:
        $ toNext = 165 - exp
        $ fireball2Unlocked = True
    elif exp < 265: # Level 5
        $ toNext = 265 - exp
        $ raiseAgilUnlocked = True
    elif exp < 405:
        $ toNext = 35 - exp
        $ recoverMinUnlocked = True
        $ fireball3Unlocked = True
    elif exp < 585:
        $ toNext = 585 - exp
        $ lightning1Unlocked = True
        $ drainDexUnlocked = True
    elif exp < 785:
        $ toNext = 785 - exp
        $ fireball4Unlocked = True
        $ tornado1Unlocked = True
    elif exp < 1035:
        $ toNext = 1035 - exp
        $ drainAgilStamUnlocked = True
        $ lightning2Unlocked = True
    elif exp < 1335: # Level 10
        $ toNext = 1335 - exp
        $ tornado2Unlocked = True
        $ raiseDexUnlocked = True
    elif exp < 1680:
        $ toNext = 1680 - exp
        $ blindUnlocked = True
        $ sapMPUnlocked = True
    elif exp < 2085:
        $ toNext = 2085 - exp
        $ tornado3Unlocked = True
        $ raiseStamUnlocked = True
    elif exp < 2535:
        $ toNext = 2535 - exp
        $ lightning3Unlocked = True
        $ recoverMedUnlocked = True
    elif exp < 3035:
        $ toNext = 3035 - exp
        $ drainHealthUnlocked = True
    elif exp < 3585: # Level 15
        $ toNext = 3585 - exp
        $ tornado4Unlocked = True
    elif exp < 4185:
        $ toNext = 4135 - exp
        $ lightning4Unlocked = True
    elif exp < 4835:
        $ toNext = 4835 - exp
        $ arctic1Unlocked = True
    elif exp < 5535:
        $ toNext = 5535 - exp
        $ explosion1Unlocked = True
    elif exp < 6335:
        $ toNext = 6335 - exp
        $ arctic2Unlocked = True
    elif exp < 7335: # Level 20
        $ toNext = 7335 - exp
        $ recoverMaxUnlocked = True
    elif exp < 8535:
        $ toNext = 8535 - exp
        $ pillageMagicUnlocked = True
    elif exp < 9935:
        $ toNext = 9935 - exp
    elif exp < 11535: # Level 23 - Final spell unlocked
        $ toNext = 11535 - exp
        $ explosion2Unlocked = True
    elif exp < 13535:
        $ toNext = 13535 - exp
    elif exp < 15935: # Level 25
        $ toNext = 15935 - exp
    elif exp < 18735:
        $ toNext = 18735 - exp
    elif exp < 21735:
        $ toNext = 21735 - exp
    elif exp < 25325:
        $ toNext = 25325 - exp
    elif exp < 29035:
        $ toNext = 29035 - exp
    elif exp < 33035: # Level 30
        $ toNext = 33035 - exp
    else: # Level 31 - Max level
        $ exp = 33035
        $ toNext = 1

    if swordLevel == 1:
        $ sword = "Probite Sword"
        $ swordDexBoost = 0
    elif swordLevel == 2:
        $ sword = "Three-Star Sword"
        $ swordDexBoost = 10
    elif swordLevel == 3:
        $ sword = "Extra Sword"
        $ swordDexBoost = 20
    elif swordLevel == 4:
        $ sword = "Agate Sword"
        $ swordDexBoost = 40
    elif swordLevel == 5:
        $ sword = "Wish, the Sword of Hope"
        $ swordDexBoost = 55
    else:
        $ weapon = "Dirty Hacker Sword"
        $ swordDexBoost = -999

    if armorLevel == 1:
        $ armor = "Copper Armor"
        $ armorStamBoost = 0
    elif armorLevel == 2:
        $ armor = "Silver Armor"
        $ armorStamBoost = 20
    elif armorLevel == 3:
        $ armor = "Gold Armor"
        $ armorStamBoost = 40
    elif armorLevel == 4:
        $ armor = "Platinum Armor"
        $ armorStamBoost = 60
    else:
        $ armor = "Dirty Hacker Armor"
        $ armorStamBoost = -999

    $ dexterity = baseDexterity + swordDexBoost + dexAlter
    $ stamina = baseStamina + armorStamBoost + stamAlter
    $ agility = baseAgility + agilAlter

    if statCheck == True:
        "Sword: [sword], Armor: [armor]"
        "Dexterity: [dexterity], Stamina: [stamina], Agility: [agility]"
        "HP: [hp], Max HP: [maxhp], MP: [mp], Max MP: [maxmp]"
        if level < 31:
            "You are Level [level]. You need [toNext] experience points to get to the next level."
        else:
            "You are Level 31, the maximum level in the game! Congratulations!"
        $ statCheck = False

    if enemy2number == 3 and roomNumber == 19:
        jump treantDefeat

    jump gameMenu

label gameMenu:
    menu:
        "Move":
        #Old Man's Forest
            if roomNumber == 1: #Old Man Room
                menu:
                    "House Entrance":
                        scene bg black with dissolve
                        scene bg gateentrance with dissolve
                        $ roomNumber = 3
                        $ monsterEncounter = renpy.random.randint(1, 20)
                        play music "riccarfield.mp3"
                    "Mill Room":
                        scene bg black with dissolve
                        scene bg millroom with dissolve
                        $ roomNumber = 2
                        $ monsterEncounter = renpy.random.randint(1, 20)
                    "Back":
                        pass
            elif roomNumber == 2: #Mill Room
                menu:
                    "Old Man's House":
                        scene bg black with dissolve
                        scene bg oldmanroom
                        show oldman
                        with dissolve
                        $ roomNumber = 1
                        $ monsterEncounter = renpy.random.randint(1, 20)
                    "The underground castle" if millstonePushed == True:
                        scene bg black with dissolve
                        stop music
                        "You fall down the staircase into the underground castle!"
                        scene bg finaldungeonstart with dissolve
                        play music "evilcastle.mp3"
                        $ roomNumber = 123
                        $ monsterEncounter = renpy.random.randint(1, 20)
                    "Back":
                        pass
            elif roomNumber == 3: #Old Man's Entrance
                menu:
                    "Old Man's House":
                        scene bg black with dissolve
                        scene bg oldmanroom
                        show oldman
                        with dissolve
                        play music "oldmanroom.mp3"
                        "Home sweet home. You've returned to the old man's room."
                        $ roomNumber = 1
                        $ monsterEncounter = renpy.random.randint(1, 20)
                    "Crossroads":
                        scene bg black with dissolve
                        scene bg forest with dissolve
                        if treesSpoken == False:
                            "Oh? Just now, someone called Theo's name!"
                            unknown "Prince Theo! Please listen to our story..."
                            theo "What? Who- Who said that?"
                            theo "Did the trees try speaking to me...?"
                            $ treesSpoken = True
                        $ roomNumber = 4
                        $ monsterEncounter = renpy.random.randint(1, 20)
                        if monsterEncounter <= 5:
                            play sound "enemyappear.mp3"
                            stop music
                            "Suddenly, an enemy attacks you!"
                            if monsterEncounter == 1:
                                $ enemy2number = 1
                            elif monsterEncounter == 2:
                                $ enemy2number = 2
                            elif monsterEncounter == 3:
                                $ enemy1number = 1
                                $ enemy2number = 1
                            elif monsterEncounter == 4:
                                $ enemy1number = 1
                                $ enemy2number = 2
                            elif monsterEncounter == 5:
                                $ enemy1number = 2
                                $ enemy2number = 1
                                $ enemy3number = 1
                            jump battleSetup
                    "Back":
                        pass
            elif roomNumber == 4: #Crossroads between Old Man and Shaman
                menu:
                    "Old Man's Entrance":
                        scene bg black with dissolve
                        scene bg gateentrance with dissolve
                        $ roomNumber = 3
                        $ monsterEncounter = renpy.random.randint(1, 20)
                    "Shaman's Entrance":
                        scene bg black with dissolve
                        scene bg gateentrance with dissolve
                        $ roomNumber = 5
                        $ monsterEncounter = renpy.random.randint(1, 20)
                    "Set off":
                        scene bg black with dissolve
                        scene bg forest with dissolve
                        $ roomNumber = 7
                        $ monsterEncounter = renpy.random.randint(1, 20)
                        if monsterEncounter <= 5:
                            play sound "enemyappear.mp3"
                            stop music
                            "Suddenly, an enemy attacks you!"
                            if monsterEncounter == 1:
                                $ enemy2number = 1
                            elif monsterEncounter == 2:
                                $ enemy2number = 2
                            elif monsterEncounter == 3:
                                $ enemy1number = 2
                                $ enemy2number = 1
                            elif monsterEncounter == 4:
                                $ enemy1number = 2
                                $ enemy2number = 2
                            elif monsterEncounter == 5:
                                $ enemy1number = 2
                                $ enemy2number = 1
                                $ enemy3number = 1
                            jump battleSetup
                    "Back":
                        pass
            elif roomNumber == 5: #Shaman's Entrance
                menu:
                    "Shaman's House":
                        scene bg black with dissolve
                        scene bg shamanRoom
                        show shaman
                        with dissolve
                        play music "shamanroom.mp3"
                        "There's a shaman wrapped up in a black mantle."
                        "Despite the eerie atmosphere, Theo feels that he can trust him."
                        $ roomNumber = 6
                        $ monsterEncounter = renpy.random.randint(1, 20)
                    "Crossroads":
                        scene bg black with dissolve
                        scene bg forest with dissolve
                        if treesSpoken == False:
                            "Oh? Just now, someone called Theo's name!"
                            unknown "Prince Theo! Please listen to our story..."
                            theo "What? Who- Who said that?"
                            theo "Did the trees try speaking to me...?"
                            $ treesSpoken = True
                        $ roomNumber = 4
                        $ monsterEncounter = renpy.random.randint(1, 20)
                    "Back":
                        pass
            elif roomNumber == 6: #Shaman's House
                menu:
                    "Leave the Shaman's House":
                        scene bg black with dissolve
                        scene bg gateentrance with dissolve
                        $ roomNumber = 5
                        play music "riccarfield.mp3"
                        $ monsterEncounter = renpy.random.randint(1, 20)
                    "Back":
                        pass
            elif roomNumber == 7: #Forest Area
                menu:
                    "The old man and shaman's houses":
                        scene bg black with dissolve
                        scene bg forest with dissolve
                        $ roomNumber = 4
                        $ monsterEncounter = renpy.random.randint(1, 20)
                        if monsterEncounter <= 5:
                            play sound "enemyappear.mp3"
                            stop music
                            "Suddenly, an enemy attacks you!"
                            if monsterEncounter == 1:
                                $ enemy2number = 1
                            elif monsterEncounter == 2:
                                $ enemy2number = 2
                            elif monsterEncounter == 3:
                                $ enemy1number = 1
                                $ enemy2number = 1
                            elif monsterEncounter == 4:
                                $ enemy1number = 1
                                $ enemy2number = 2
                            elif monsterEncounter == 5:
                                $ enemy1number = 2
                                $ enemy2number = 1
                                $ enemy3number = 1
                            jump battleSetup
                    "Go left":
                        scene bg black with dissolve
                        scene bg forest with dissolve
                        $ roomNumber = 8
                        "Beyond this gate is the magician Martel's domain."
                        $ monsterEncounter = renpy.random.randint(1, 20)
                        if monsterEncounter <= 5:
                            play sound "enemyappear.mp3"
                            stop music
                            "Suddenly, an enemy attacks you!"
                            if monsterEncounter == 1:
                                $ enemy2number = 2
                            elif monsterEncounter == 2:
                                $ enemy2number = 2
                            elif monsterEncounter == 3:
                                $ enemy1number = 1
                                $ enemy2number = 2
                            elif monsterEncounter == 4:
                                $ enemy1number = 2
                                $ enemy2number = 2
                            elif monsterEncounter == 5:
                                $ enemy1number = 1
                                $ enemy2number = 1
                                $ enemy3number = 1
                            jump battleSetup
                    "Go right":
                        scene bg black with dissolve
                        scene bg forest with dissolve
                        $ roomNumber = 9
                        $ monsterEncounter = renpy.random.randint(1, 20)
                        if monsterEncounter <= 5:
                            play sound "enemyappear.mp3"
                            stop music
                            "Suddenly, an enemy attacks you!"
                            if monsterEncounter == 1:
                                $ enemy2number = 2
                            elif monsterEncounter == 2:
                                $ enemy2number = 2
                            elif monsterEncounter == 3:
                                $ enemy1number = 2
                                $ enemy2number = 2
                            elif monsterEncounter == 4:
                                $ enemy1number = 2
                                $ enemy2number = 2
                            elif monsterEncounter == 5:
                                $ enemy1number = 1
                                $ enemy2number = 1
                                $ enemy3number = 1
                            jump battleSetup
                    "Back":
                        pass
            elif roomNumber == 8: #Martel's Gate
                menu:
                    "Return to the forest":
                        scene bg black with dissolve
                        scene bg forest with dissolve
                        $ doorMOpened = False
                        $ roomNumber = 7
                        $ monsterEncounter = renpy.random.randint(1, 20)
                        if monsterEncounter <= 5:
                            play sound "enemyappear.mp3"
                            stop music
                            "Suddenly, an enemy attacks you!"
                            if monsterEncounter == 1:
                                $ enemy2number = 1
                            elif monsterEncounter == 2:
                                $ enemy2number = 1
                            elif monsterEncounter == 3:
                                $ enemy1number = 2
                                $ enemy2number = 2
                            elif monsterEncounter == 4:
                                $ enemy1number = 1
                                $ enemy2number = 2
                            elif monsterEncounter == 5:
                                $ enemy1number = 2
                                $ enemy2number = 2
                                $ enemy3number = 1
                            jump battleSetup
                    "Enter Martel's domain" if keyMObtained == True:
                        scene bg black with dissolve
                        scene bg gateentrance with dissolve
                        $ doorMOpened = False
                        $ roomNumber = 20
                        $ monsterEncounter = renpy.random.randint(1, 20)
                    "Back":
                        pass
            elif roomNumber == 9: #Another forest area
                menu:
                    "Go left":
                        scene bg black with dissolve
                        scene bg gateentrance with dissolve
                        $ roomNumber = 7
                        $ monsterEncounter = renpy.random.randint(1, 20)
                        if monsterEncounter <= 5:
                            play sound "enemyappear.mp3"
                            stop music
                            "Suddenly, an enemy attacks you!"
                            if monsterEncounter == 1:
                                $ enemy2number = 1
                            elif monsterEncounter == 2:
                                $ enemy2number = 1
                            elif monsterEncounter == 3:
                                $ enemy1number = 2
                                $ enemy2number = 2
                            elif monsterEncounter == 4:
                                $ enemy1number = 1
                                $ enemy2number = 1
                            elif monsterEncounter == 5:
                                $ enemy1number = 1
                                $ enemy2number = 1
                                $ enemy3number = 1
                            jump battleSetup
                    "Go right":
                        scene bg black with dissolve
                        scene bg forest with dissolve
                        $ roomNumber = 10
                        $ monsterEncounter = renpy.random.randint(1, 20)
                        if monsterEncounter <= 5:
                            play sound "enemyappear.mp3"
                            stop music
                            "Suddenly, an enemy attacks you!"
                            if monsterEncounter == 1:
                                $ enemy2number = 1
                            elif monsterEncounter == 2:
                                $ enemy2number = 1
                            elif monsterEncounter == 3:
                                $ enemy2number = 2
                            elif monsterEncounter == 4:
                                $ enemy1number = 1
                                $ enemy2number = 2
                            elif monsterEncounter == 5:
                                $ enemy1number = 2
                                $ enemy2number = 2
                                $ enemy3number = 1
                            jump battleSetup
                    "Back":
                        pass
            elif roomNumber == 10: #Yet another forest area
                menu:
                    "Go forward":
                        scene bg black with dissolve
                        scene bg forest with dissolve
                        $ roomNumber = 12
                        $ monsterEncounter = renpy.random.randint(1, 20)
                        if monsterEncounter <= 5:
                            play sound "enemyappear.mp3"
                            stop music
                            "Suddenly, an enemy attacks you!"
                            if monsterEncounter == 1:
                                $ enemy2number = 1
                            elif monsterEncounter == 2:
                                $ enemy1number = 1
                                $ enemy2number = 2
                            elif monsterEncounter == 3:
                                $ enemy1number = 1
                                $ enemy2number = 1
                            elif monsterEncounter == 4:
                                $ enemy1number = 2
                                $ enemy2number = 2
                            elif monsterEncounter == 5:
                                $ enemy1number = 2
                                $ enemy2number = 2
                                $ enemy3number = 1
                            jump battleSetup
                    "Go left":
                        scene bg black with dissolve
                        scene bg forest with dissolve
                        $ roomNumber = 9
                        $ monsterEncounter = renpy.random.randint(1, 20)
                        if monsterEncounter <= 5:
                            play sound "enemyappear.mp3"
                            stop music
                            "Suddenly, an enemy attacks you!"
                            if monsterEncounter == 1:
                                $ enemy2number = 1
                            elif monsterEncounter == 2:
                                $ enemy2number = 2
                            elif monsterEncounter == 3:
                                $ enemy1number = 1
                                $ enemy2number = 1
                            elif monsterEncounter == 4:
                                $ enemy1number = 1
                                $ enemy2number = 2
                            elif monsterEncounter == 5:
                                $ enemy1number = 2
                                $ enemy2number = 1
                                $ enemy3number = 1
                            jump battleSetup
                    "Go right":
                        scene bg black with dissolve
                        scene bg gateentrance with dissolve
                        "Beyond this gate is the magician Shabow's domain."
                        $ roomNumber = 11
                        $ monsterEncounter = renpy.random.randint(1, 20)
                        if monsterEncounter <= 5:
                            play sound "enemyappear.mp3"
                            stop music
                            "Suddenly, an enemy attacks you!"
                            if monsterEncounter == 1:
                                $ enemy2number = 1
                            elif monsterEncounter == 2:
                                $ enemy2number = 1
                            elif monsterEncounter == 3:
                                $ enemy1number = 2
                                $ enemy2number = 1
                            elif monsterEncounter == 4:
                                $ enemy1number = 1
                                $ enemy2number = 2
                            elif monsterEncounter == 5:
                                $ enemy1number = 2
                                $ enemy2number = 1
                                $ enemy3number = 1
                            jump battleSetup
                    "Back":
                        pass
            elif roomNumber == 11: #Shabow's Gate
                menu:
                    "Return to the forest":
                        scene bg black with dissolve
                        scene bg forest with dissolve
                        $ doorSOpened = False
                        $ roomNumber = 10
                        $ monsterEncounter = renpy.random.randint(1, 20)
                        if monsterEncounter <= 5:
                            play sound "enemyappear.mp3"
                            stop music
                            "Suddenly, an enemy attacks you!"
                            if monsterEncounter == 1:
                                $ enemy2number = 1
                            elif monsterEncounter == 2:
                                $ enemy2number = 2
                            elif monsterEncounter == 3:
                                $ enemy1number = 2
                                $ enemy2number = 1
                            elif monsterEncounter == 4:
                                $ enemy1number = 1
                                $ enemy2number = 2
                            elif monsterEncounter == 5:
                                $ enemy1number = 1
                                $ enemy2number = 2
                                $ enemy3number = 1
                            jump battleSetup
                    "Enter Shabow's domain" if keySObtained == True:
                        scene bg black with dissolve
                        scene bg gateentrance with dissolve
                        $ doorSOpened = False
                        $ roomNumber = 50
                        $ monsterEncounter = renpy.random.randint(1, 20)
                    "Back":
                        pass
            elif roomNumber == 12: #Yep, more forest
                menu:
                    "Go backwards":
                        scene bg black with dissolve
                        scene bg forest with dissolve
                        $ roomNumber = 10
                        $ monsterEncounter = renpy.random.randint(1, 20)
                        if monsterEncounter <= 5:
                            play sound "enemyappear.mp3"
                            stop music
                            "Suddenly, an enemy attacks you!"
                            if monsterEncounter == 1:
                                $ enemy2number = 1
                            elif monsterEncounter == 2:
                                $ enemy2number = 1
                            elif monsterEncounter == 3:
                                $ enemy1number = 1
                                $ enemy2number = 2
                            elif monsterEncounter == 4:
                                $ enemy1number = 1
                                $ enemy2number = 2
                            elif monsterEncounter == 5:
                                $ enemy1number = 2
                                $ enemy2number = 2
                                $ enemy3number = 1
                            jump battleSetup
                    "Go left":
                        scene bg black with dissolve
                        scene bg forest with dissolve
                        $ roomNumber = 13
                        $ monsterEncounter = renpy.random.randint(1, 20)
                    "Go right":
                        scene bg black with dissolve
                        scene bg gateentrance with dissolve
                        $ roomNumber = 16
                        $ monsterEncounter = renpy.random.randint(1, 20)
                        if monsterEncounter <= 5:
                            play sound "enemyappear.mp3"
                            stop music
                            "Suddenly, an enemy attacks you!"
                            if monsterEncounter == 1:
                                $ enemy2number = 1
                            elif monsterEncounter == 2:
                                $ enemy2number = 2
                            elif monsterEncounter == 3:
                                $ enemy1number = 1
                                $ enemy2number = 2
                            elif monsterEncounter == 4:
                                $ enemy1number = 2
                                $ enemy2number = 2
                            elif monsterEncounter == 5:
                                $ enemy1number = 2
                                $ enemy2number = 1
                                $ enemy3number = 2
                            jump battleSetup
                    "Back":
                        pass
            elif roomNumber == 13: #Shop Entrance
                menu:
                    "Enter the shop":
                        scene bg black with dissolve
                        scene bg shop 
                        show shopkeeper
                        with dissolve
                        $ roomNumber = 14
                        $ shopkeepVisits += 1
                        play music "oldmanroom.mp3"
                        "You are inside the forest shop."
                        $ monsterEncounter = renpy.random.randint(1, 20)
                    "Return to the forest":
                        scene bg black with dissolve
                        scene bg forest
                        $ roomNumber = 12
                        $ monsterEncounter = renpy.random.randint(1, 20)
                        if monsterEncounter <= 5:
                            play sound "enemyappear.mp3"
                            stop music
                            "Suddenly, an enemy attacks you!"
                            if monsterEncounter == 1:
                                $ enemy2number = 1
                            elif monsterEncounter == 2:
                                $ enemy2number = 2
                            elif monsterEncounter == 3:
                                $ enemy1number = 1
                                $ enemy2number = 1
                            elif monsterEncounter == 4:
                                $ enemy1number = 1
                                $ enemy2number = 2
                            elif monsterEncounter == 5:
                                $ enemy1number = 2
                                $ enemy2number = 2
                                $ enemy3number = 2
                            jump battleSetup
                    "Back":
                        pass
            elif roomNumber == 14: #Inside the shop
                menu:
                    "Exit the shop":
                        scene bg black with dissolve
                        scene bg gateentrance with dissolve
                        $ roomNumber = 13
                        play music "riccarfield.mp3"
                        $ monsterEncounter = renpy.random.randint(1, 20)
                    "Enter the secret room" if graceRoomUnlocked == True:
                        scene bg black with dissolve
                        scene bg shop with dissolve
                        $ roomNumber = 15
                        $ monsterEncounter = renpy.random.randint(1, 20)
                    "Back":
                        pass
            elif roomNumber == 15: #Grace Scroll
                menu:
                    "Return to the shop":
                        scene bg black with dissolve
                        scene bg shop 
                        show shopkeeper
                        with dissolve
                        $ roomNumber = 14
                        $ monsterEncounter = renpy.random.randint(1, 20)
                    "Back":
                        pass
            elif roomNumber == 16: #Even more forest. Again.
                menu:
                    "Go forward":
                        scene bg black with dissolve
                        scene bg forest with dissolve
                        "Beyond this gate is the magician Camu's domain."
                        $ roomNumber = 17
                        $ monsterEncounter = renpy.random.randint(1, 20)
                        if monsterEncounter <= 5:
                            play sound "enemyappear.mp3"
                            stop music
                            "Suddenly, an enemy attacks you!"
                            if monsterEncounter == 1:
                                $ enemy2number = 1
                            elif monsterEncounter == 2:
                                $ enemy2number = 1
                            elif monsterEncounter == 3:
                                $ enemy1number = 2
                                $ enemy2number = 1
                            elif monsterEncounter == 4:
                                $ enemy1number = 1
                                $ enemy2number = 2
                            elif monsterEncounter == 5:
                                $ enemy1number = 1
                                $ enemy2number = 1
                                $ enemy3number = 1
                            jump battleSetup
                    "Go left":
                        scene bg black with dissolve
                        scene bg forest with dissolve
                        $ roomNumber = 12
                        $ monsterEncounter = renpy.random.randint(1, 20)
                        if monsterEncounter <= 5:
                            play sound "enemyappear.mp3"
                            stop music
                            "Suddenly, an enemy attacks you!"
                            if monsterEncounter == 1:
                                $ enemy2number = 1
                            elif monsterEncounter == 2:
                                $ enemy2number = 2
                            elif monsterEncounter == 3:
                                $ enemy1number = 2
                                $ enemy2number = 1
                            elif monsterEncounter == 4:
                                $ enemy1number = 1
                                $ enemy2number = 1
                            elif monsterEncounter == 5:
                                $ enemy1number = 1
                                $ enemy2number = 2
                                $ enemy3number = 2
                            jump battleSetup
                    "Go right":
                        scene bg black with dissolve
                        scene bg forest with dissolve
                        $ roomNumber = 18
                        $ monsterEncounter = renpy.random.randint(1, 20)
                        if monsterEncounter <= 5:
                            play sound "enemyappear.mp3"
                            stop music
                            "Suddenly, an enemy attacks you!"
                            if monsterEncounter == 1:
                                $ enemy2number = 1
                            elif monsterEncounter == 2:
                                $ enemy2number = 1
                            elif monsterEncounter == 3:
                                $ enemy2number = 2
                            elif monsterEncounter == 4:
                                $ enemy1number = 1
                                $ enemy2number = 1
                            elif monsterEncounter == 5:
                                $ enemy1number = 1
                                $ enemy2number = 1
                                $ enemy3number = 1
                            jump battleSetup
                    "Back":
                        pass
            elif roomNumber == 17: #Camu's Gate
                menu:
                    "Return to the forest":
                        scene bg black with dissolve
                        scene bg forest with dissolve
                        $ doorCOpened = False
                        $ roomNumber = 16
                        $ monsterEncounter = renpy.random.randint(1, 20)
                        if monsterEncounter <= 5:
                            play sound "enemyappear.mp3"
                            stop music
                            "Suddenly, an enemy attacks you!"
                            if monsterEncounter == 1:
                                $ enemy2number = 1
                            elif monsterEncounter == 2:
                                $ enemy2number = 2
                            elif monsterEncounter == 3:
                                $ enemy1number = 1
                                $ enemy2number = 2
                            elif monsterEncounter == 4:
                                $ enemy1number = 2
                                $ enemy2number = 2
                            elif monsterEncounter == 5:
                                $ enemy1number = 2
                                $ enemy2number = 1
                                $ enemy3number = 1
                            jump battleSetup
                    "Enter Camu's domain" if keyCObtained == True:
                        scene bg black with dissolve
                        scene bg gateentrance with dissolve
                        $ doorCOpened = False
                        $ roomNumber = 86
                        $ monsterEncounter = renpy.random.randint(1, 20)
                    "Back":
                        pass
            elif roomNumber == 18: #Forest square
                menu:
                    "Go forward":
                        scene bg black with dissolve
                        scene bg forest with dissolve
                        $ roomNumber = 19
                        $ monsterEncounter = renpy.random.randint(1, 20)
                    "Go left":
                        scene bg black with dissolve
                        scene bg forest with dissolve
                        $ roomNumber = 16
                        $ monsterEncounter = renpy.random.randint(1, 20)
                        if monsterEncounter <= 5:
                            play sound "enemyappear.mp3"
                            stop music
                            "Suddenly, an enemy attacks you!"
                            if monsterEncounter == 1:
                                $ enemy2number = 1
                            elif monsterEncounter == 2:
                                $ enemy2number = 2
                            elif monsterEncounter == 3:
                                $ enemy1number = 2
                                $ enemy2number = 2
                            elif monsterEncounter == 4:
                                $ enemy1number = 1
                                $ enemy2number = 1
                            elif monsterEncounter == 5:
                                $ enemy1number = 1
                                $ enemy2number = 2
                                $ enemy3number = 2
                            jump battleSetup
                    "Back":
                        pass
            elif roomNumber == 19: #Treant's Room
                menu:
                    "Go back":
                        scene bg black with dissolve
                        scene bg forest with dissolve
                        $ roomNumber = 18
                        $ monsterEncounter = renpy.random.randint(1, 20)
                        if monsterEncounter <= 5:
                            play sound "enemyappear.mp3"
                            stop music
                            "Suddenly, an enemy attacks you!"
                            if monsterEncounter == 1:
                                $ enemy2number = 1
                            elif monsterEncounter == 2:
                                $ enemy2number = 2
                            elif monsterEncounter == 3:
                                $ enemy1number = 1
                                $ enemy2number = 1
                            elif monsterEncounter == 4:
                                $ enemy1number = 1
                                $ enemy2number = 2
                            elif monsterEncounter == 5:
                                $ enemy1number = 2
                                $ enemy2number = 1
                                $ enemy3number = 1
                            jump battleSetup
                    "Back":
                        pass
        #Martel's Domain
            elif roomNumber == 20: #Entrance to Martel's Domain
                menu:
                    "Return to the Old Man's forest":
                        scene bg black with dissolve
                        scene bg gateentrance with dissolve
                        $ roomNumber = 8
                        "The door to Martel's domain re-locked."
                        $ monsterEncounter = renpy.random.randint(1, 20)
                    "Back":
                        pass
        #The Well
        #Shabow's Domain
        #Camu's Domain
        #The Pagoda
        #Underground Ruins
        #The Castle
        #The Mirror World
        #Postgame Dungeon
            jump gameMenu

        "Look":
            if roomNumber == 1: #Old Man Room
                menu:
                    "In room":
                        "This room fills you with memories of your 15 years with the old man."
                    "The Old Man":
                        if keyMObtained == False:
                            oldman "Oh, Prince Theo! You are the chosen one who will save this world from the darkness!"
                            oldman "Though difficult, find the Sword of Hope with all your power!"
                            oldman "I look forward to the day you obtain the fabled blade."
                            theo "I swear, for the sake of all Riccar, I will obtain that sword!"
                        else:
                            "Defeat the evil king now!"
                    "Back":
                        pass
            elif roomNumber == 2: #Mill Room
                menu:
                    "In room":
                        "A room with a millstone."
                    "Millstone":
                        if millstonePushed == False:
                            "A millstone sits in the room, all in its lonesome."
                        else:
                            "The millstone has been moved aside, opening the way to the underground castle."
                            "Go forth, Prince Theo! Your final journey awaits you!"
                    "Back":
                        pass
            elif roomNumber == 3: #Old Man Gate
                menu:
                    "Wall":
                        "A vertical wall is in front of you."
                    "Front Door":
                        "The door to the old man's house. You are welcome inside at any time."
                    "Back":
                        pass
            elif roomNumber == 4: #Crossroads
                menu:
                    "Trees":
                        "Prince Theo!"
                        "The force of darkness suddenly turned us into trees."
                        "We've been here so long, we don't know how much time has passed."
                        "Please! Return us to normal as soon as possible!"
                        "We will do all we can to help you."
                        "If you want to know something, listen and we will tell you."
                    "Grass":
                        "Grass is growing in the forest."
                        "There's something in the grass, but it's better off not described..."
                    "Back":
                        pass
            elif roomNumber == 5: #Shaman Gate
                menu:
                    "Front Door":
                        "The door to the shaman's house."
                        "Though it looks like any other door, you still feel uneasy looking at it."
                    "Back":
                        pass
            elif roomNumber == 6: # Shaman Room
                menu:
                    "In room":
                        "You are inside an eerie, dimly lit room."
                        "The whole room has a terrible stench."
                    "Shaman":
                        shaman "I am almighty! I will pray to return your power."
                        shaman "Will you pay me [level + 4] gold?"
                        menu:
                            "Yes":
                                if hp == maxhp and mp == maxmp:
                                    shaman "But you are as fit as a fiddle! Do not waste your hard-earned coins on me now!"
                                elif gold >= level + 4:
                                    $ gold -= level + 4
                                    hide shaman
                                    show bg black
                                    with dissolve
                                    shaman "Tnailavmaet!"
                                    $ hp = maxhp
                                    $ mp = maxmp
                                    shaman "Your health and magic points have been returned to maximum value!"
                                    show bg shamanRoom
                                    show shaman
                                    with dissolve
                                    shaman "I hope to see you again."
                                    shaman "Now go, and be careful."
                                else:
                                    shaman "Hmmmm... Sorry, Theo. I know times are rough, but I can't give credit. You'll have to come back when you're a little richer."
                            "No":
                                shaman "Very well. Be careful."
                    "Crystal Ball":
                        shaman "I will give you a message from my crystal ball!"
                        if keyMObtained == False:
                            shaman "It is said that the key of Martel is held by the wicked Treant!"
                            shaman "Heroes under Level 4 should avoid the Treant for the time being; raise your level to stand a chance against the wooden fiend!"
                        shaman "The crystal ball says you have a good future, but don't let your guard down. Go carefully."
                    "Back":
                        pass
            elif roomNumber == 7: #Forest
                menu:
                    "Surroundings":
                        "Some monsters are battling each other in the distance."
                        "Theo decides to leave them be for the time being."
                    "Trees":
                        "Listen, Theo! You can read the magic text after some experience."
                    "Sign":
                        "<- Martel's Domain\nShabow and Camu's Domains ->"
                    "Back":
                        pass
            elif roomNumber == 8: #Martel's Gate
                menu:
                    "Trees":
                        "Three magicians have protected the country for a long time."
                        "After the dragon corrupted the king, they were forced to seal the castle in the darkness underground."
                    "Gate":
                        if doorMOpened == False:
                            "Martel's gate. It is a sturdy, iron-barred gate that is securely locked."
                        else:
                            "Martel's gate. It is wide open, but will not stay that way forever."
                    "Back":
                        pass
            elif roomNumber == 9: #More forest
                menu:
                    "Trees":
                        if keyMObtained == False:
                            "Prince Theo, I really saw it!"
                            theo "Huh? Saw what?"
                            "A terribly big tree monster raged about in the square!"
                            "It stole a key from a passerby pigeon!"
                            theo "I see. Thanks for the tip."
                            "Please liberate us, Prince! You are our only hope for salvation!"
                        else:
                            "Prince Theo! The tree that was hurting us has changed its ways!"
                            theo "I hope you all can get along with it, now."
                            "You think the Treant was another person cursed like us?"
                            theo "I don't know. I'll have to ask it one of these days..."
                    "Path":
                        if room9Herb == False:
                            "You watch the path and spot an herb!"
                            if herbsOwned < 7:
                                $ herbsOwned += 1
                                play sound "itemacquired.mp3"
                                "You obtained the herb!"
                            else:
                                "But you can't carry any more..."
                        else:
                            "There is nothing special on the floor."
                    "Back":
                        pass
            elif roomNumber == 10: #Forest
                menu:
                    "Trees":
                        "Prince Theo!"
                        "Your mother, Queen Remy, was a very, very kind lady."
                        "She kept the ruby charm sent to her with great care."
                        theo "Oh, mother..."
                    "Grass":
                        "The grass looks wet with dew."
                    "Sign":
                        "^ Camu's Domain\nShabow's Domain ->"
                    "Back":
                        pass
            elif roomNumber == 11: #Shabow's Gate
                menu:
                    "Trees":
                        "Martel the Wise, Shabow the Brave, Camu the Loving..."
                        "These three magicians are the finest in the land!"
                    "Gate":
                        if doorSOpened == False:
                            "Shabow's gate. It is a sturdy, iron-barred gate that is securely locked."
                        else:
                            "Shabow's gate. It is wide open, but will not stay that way forever."
                    "Back":
                        pass
            elif roomNumber == 12: #More forest
                menu:
                    "Trees":
                        "Prince Theo!"
                        "You know of the legend of the swordsman Poliniak, don't you?"
                        "He was a brave swordsman who was bested by the darkness."
                        "It wasn't long before he died from an epioemic illness."
                        "Still, he cares for his country, and watches over it from heaven."
                        theo "Poliniak... He was powerful, indeed."
                        "When King Hennessy broke the darkness seal, Poliniak mourned deeply."
                        "His tears poured down like rain on the forest for a long time."
                        "Soaked by the raining tears, we truly do sympathize with the poor man."
                        theo "Wait, but you're trees... and you soaked up the rain..."
                        theo "Does that mean you-"
                        "Whoa, whoa, whoa! Don't- Don't think about it too hard."
                        "Anyways, you can find his gravestone on the outskirts of Martel's domain. Visit there when you get the chance."
                    "Small Stone":
                        "Are those gold nuggets mixed in with the gravel...?"
                        theo "I need to stop daydreaming..."
                    "Sign":
                        "The sign reads: \"Forest shop to your left\"."
                    "Back":
                        pass
            elif roomNumber == 13: #Shop Entrance
                menu:
                    "Front Door":
                        "The entrance to the shop."
                    "Back":
                        pass
            elif roomNumber == 14:
                menu:
                    "In room":
                        "Goods are displayed in shelves behind the store counter."
                        "Who will buy them all? You, perhaps?"
                    "Shopkeeper":
                        if shopkeepVisits >= 2 and graceRoomUnlocked == False:
                            shopkeeper "Oh, Theo! I'm glad you're back!"
                            shopkeeper "I'm glad you come here often. Serving you is my pleasure!"
                            shopkeeper "You know, I have a hidden treasure chest in the back of my store."
                            shopkeeper "There is an old scroll in it. It has no value to me, but I think you could make use of it."
                            $ graceRoomUnlocked = True
                            shopkeeper "Back to business..."
                        shopkeeper "Welcome! Would you like to buy anything?"
                        menu:
                            "Yes":
                                menu:
                                    "Barley (15 gold)":
                                        if gold >= 15 and barleysOwned < 7:
                                            $ gold -= 15
                                            $ barleysOwned += 1
                                            "You bought a barley!"
                                        elif barleysOwned >= 7:
                                            shopkeeper "Whoa, you've got plenty of those already! No need to overflow your pockets..."
                                        else:
                                            shopkeeper "You don't have enough gold. Sorry."
                                    "Wheat (30 gold)":
                                        if gold >= 30 and wheatsOwned < 7:
                                            $ gold -= 30
                                            $ wheatsOwned += 1
                                            "You bought a wheat!"
                                        elif wheatsOwned >= 7:
                                            shopkeeper "Whoa, you've got plenty of those already! No need to overflow your pockets..."
                                        else:
                                            shopkeeper "You don't have enough gold. Sorry."
                                    "Herb (40 gold)":
                                        if gold >= 40 and herbsOwned < 7:
                                            $ gold -= 40
                                            $ herbsOwned += 1
                                            "You bought an herb!"
                                        elif herbsOwned >= 7:
                                            shopkeeper "Whoa, you've got plenty of those already! No need to overflow your pockets..."
                                        else:
                                            shopkeeper "You don't have enough gold. Sorry."
                                    "Silver Armor (50 gold)" if armorLevel < 2:
                                        if gold >= 50:
                                            $ gold -= 50
                                            $ armorLevel = 2
                                            "You bought a set of Silver Armor, and equip it immediately!"
                                            "You feel your stamina rise up as you don the suit!"
                                        else:
                                            shopkeeper "Sorry, Theo. I can't give credit! Come back when you're a little... mmm... richer!"
                                            shopkeeper "Ehehe... I always wanted to say that..."
                                            "Theo just gives her a deadpan glare. Guess he'll have to go swat some more bugs and skulls to get that."
                                    "Back":
                                        pass
                            "No":
                                pass
                        shopkeeper "Thank you! Come again!"
                    "Goods for sale":
                        "Barley and wheat restore your health, while herbs restore magic. You can have up to 7 of each."
                        if armorLevel < 2:
                            "There is also a suit of silver armor for sale. That ought to provide some extra stamina for the tough fights."
                    "Back":
                        pass
            elif roomNumber == 15: #Grace Room:
                menu:
                    "In room":
                        theo "Something seems strange..."
                        "Actually, no. It's just an ordinary room. Isn't there something else you should be focusing on?"
                    "Chest":
                        if graceUnlocked == False:
                            "There is a lot of dust on the chest's lid. This must be where the shopkeeper kept her scroll."
                        else:
                            "You already procured the scroll inside. There is no reason to be back here."
                    "Back":
                        pass
            elif roomNumber == 16: #More forest
                menu:
                    "Trees":
                        "Oh, great. Theo's here..."
                        theo "Excuse me?"
                        "Why don't you go bother someone else!? At least you get to walk around freely, unlike some of us."
                        theo "Look, I'm sorry about what my father did, but I will set you all free!"
                        "Oh, please! We all know that forsaken castle's buried underground! As if I give a squat!"
                        "I'll always be a tree, never a human again..."
                        theo "...I won't let that be the case."
                        "Yeah, whatever. Keep telling yourself that. Now, SCRAM!"
                    "Grass":
                        "The grass looks wet with dew."
                    "Back":
                        pass                
            elif roomNumber == 17: #Camu's Gate
                menu:
                    "Hedge":
                        "The stone wall is very high."
                        "Looks like it's impossible to climb over."
                    "Gate":
                        if doorCOpened == False:
                            "Camu's gate. It is a sturdy, iron-barred gate that is securely locked."
                        else:
                            "Camu's gate. It is wide open, but will not stay that way forever."
                    "Back":
                        pass
            elif roomNumber == 18: #Forest square
                menu:
                    "Trees":
                        "Martel's domain has a church where we can get inspiration."
                        "The forest shopkeeper used to go there, but now it's completely barren."
                    "Path":
                        "There is nothing of interest on the path."
                    "Back":
                        pass
            elif roomNumber == 19: #Treant Room
                menu:
                    "Square":
                        if keyMObtained == False:
                            "The plaza is completely quiet."
                            theo "I've got a bad feeling about this..."
                        else:
                            "The bad feeling from earlier has subsided."
                    "Treant":
                        if keyMObtained == False:
                            "It's a really tall tree."
                            theo "Argh, looking up is straining my neck..."
                        elif moonCompleted == True and treantFruitObtained == False:
                            treant "Hey, Theo! I've started growing some nutritious fruit! You can have some if you'd like!"
                        else:
                            treant "Hey, Theo! People have started warming up to me now that I've changed!"
                            theo "Actually, you wouldn't happen to be a former human, would you?"
                            treant "Oh, that? No, I'm a true-born tree, born from the seed of the great forest elder!"
                            theo "I see. Hope your rehabilitation goes well!"
                            treant "Best of luck to you too, Theo!"
                    "Treant Fruit" if moonCompleted == True and treantFruitObtained == False:
                        "A delicious fruit rests on the ground."
                        $ treantFruitObtained = True
                        play sound "itemacquired.mp3"
                        "Obtained the Treant's fruit!"
                    "Back":
                        pass
        #Martel's Domain
            elif roomNumber == 20: #Entrance to Martel's Domain
                menu:
                    "Trees":
                        "Save us, Theo!"
                    "Back":
                        pass
        #The Well
        #Shabow's Domain
        #Camu's Domain
        #The Pagoda
        #Underground Ruins
        #The Castle
        #The Mirror World
        #Postgame Dungeon
            jump gameMenu
        "Open":
            if roomNumber == 1: #Old Man Room
                menu:
                    "In room":
                        "Hrrrrrrnnnnggghh! Ugh... Unfortunately, it won't open."
                    "The Old Man":
                        oldman "Now, now, Theo. There's no need to do that. You already know how I feel."
                    "Back":
                        pass
            elif roomNumber == 2: #Mill Room
                menu:
                    "In room":
                        "Hrrrrrrnnnnggghh! Ugh... Unfortunately, it won't open."
                    "Millstone":
                        if swordLevel != 5:
                            "You attempt to push the millstone out of the way with all your might!"
                            "Sadly, it does not budge even a centimeter. It's as if the stone is glued to the ground!"
                        else:
                            "You push the millstone to the side, revealing a ladder leading underground."
                            "This must be where you are to confront your destiny. Good luck, Prince Theo."
                    "Back":
                        pass
            elif roomNumber == 3: #Old Man Gate
                menu:
                    "In room":
                        "Hrrrrrrnnnnggghh! Ugh... Unfortunately, it won't open."
                    "Front Door":
                        "The gate is open for you whenever you'd like. No need to unlock it."
                    "Back":
                        pass
            elif roomNumber == 4: #Crossroads
                menu:
                    "Trees":
                        "Theo thinks about the people who have been turned into trees."
                        theo "No, I won't hurt them. Those poor people will be saved!" with vpunch
                    "Grass":
                        theo "Hang on, what am I doing!? There's no reason to open it!"
                    "Back":
                        pass
            elif roomNumber == 5: #Shaman's Gate
                menu:
                    "Gate":
                        "The shaman's gate is open to all. No need to unlock it."
                    "Back":
                        pass
            elif roomNumber == 6: #Shaman's Room
                menu:
                    "In room":
                        "Hrrrrrrnnnnggghh! Ugh... Unfortunately, it won't open."
                    "Shaman":
                        shaman "There is no need to open me, for there is nothing inside me."
                        theo "Sheesh, ominous much?"
                    "Crystal Ball":
                        "The crystal ball looks sturdy, sure, but even attempting to break it would have nasty consequences."
                        "Theo wisely decides against it."    
                    "Back":
                        pass
            elif roomNumber == 7: #Forest
                menu:
                    "Surroundings":
                        "But there's nothing to open!"
                    "Trees":
                        "Theo thinks about the people who have been turned into trees."
                        theo "No, I won't hurt them. Those poor people will be saved!" with vpunch
                    "Sign":
                        "Hrrrrrrnnnnggghh! Ugh... Unfortunately, it won't open."
                    "Back":
                        pass
            elif roomNumber == 8: #Martel's Gate
                menu:
                    "Trees":
                        "Theo thinks about the people who have been turned into trees."
                        theo "No, I won't hurt them. Those poor people will be saved!" with vpunch
                    "Gate":
                        if doorMOpened == False:
                            "Hrrrrrrnnnnggghh! Ugh... Unfortunately, it won't open."
                            "You're going to need the key to open that."
                        else:
                            "But the gate is already open!"
                    "Back":
                        pass
            elif roomNumber == 9: #Forest
                menu:
                    "Trees":
                        "Theo thinks about the people who have been turned into trees."
                        theo "No, I won't hurt them. Those poor people will be saved!" with vpunch
                    "Path":
                        "Hrrrrrrnnnnggghh! Ugh... Unfortunately, it won't open."
                    "Back":
                        pass
            elif roomNumber == 10: #Forest
                menu:
                    "Trees":
                        "Theo thinks about the people who have been turned into trees."
                        theo "No, I won't hurt them. Those poor people will be saved!" with vpunch
                    "Grass":
                        theo "Hang on, what am I doing!? There's no reason to open it!"
                    "Sign":
                        "Hrrrrrrnnnnggghh! Ugh... Unfortunately, it won't open."
                    "Back":
                        pass
            elif roomNumber == 11: #Shabow's Gate
                menu:
                    "Trees":
                        "Theo thinks about the people who have been turned into trees."
                        theo "No, I won't hurt them. Those poor people will be saved!" with vpunch
                    "Gate":
                        if doorSOpened == False:
                            "Hrrrrrrnnnnggghh! Ugh... Unfortunately, it won't open."
                            "You're going to need the key to open that."
                        else:
                            "But the gate is already open!"
                    "Back":
                        pass
            elif roomNumber == 12: #Forest
                menu:
                    "Trees":
                        "Theo thinks about the people who have been turned into trees."
                        theo "No, I won't hurt them. Those poor people will be saved!" with vpunch
                    "Small Stone":
                        "Hrrrrrrnnnnggghh! Ugh... Unfortunately, it won't open."
                    "Sign":
                        "Hrrrrrrnnnnggghh! Ugh... Unfortunately, it won't open."
                    "Back":
                        pass
            elif roomNumber == 13: #Shop Entrance
                menu:
                    "Front Door":
                        "The door is already unlocked."
                    "Back":
                        pass
            elif roomNumber == 14: #Forest Shop
                menu:
                    "In room":
                        "Hrrrrrrnnnnggghh! Ugh... Unfortunately, it won't open."
                    "Shopkeeper":
                        shopkeeper "Huh- Hey, why the interest in me, Theo?"
                        theo "I'm... not sure, myself."
                        shopkeeper "Well, this is embarrasing, isn't it?"
                    "Goods for sale":
                        shopkeeper "Hey, now. Don't think you can rob me that easily!"
                        theo "Aww, dangit."
                        shopkeeper "Always the mischievous one, Theo. I guess some things never change."
                    "Back":
                        pass
            elif roomNumber == 15:
                menu:
                    "In room":
                        "Hrrrrrrnnnnggghh! Ugh... Unfortunately, it won't open."
                    "Chest":
                        if graceUnlocked == False:
                            "Theo opened the chest."
                            "Inside is a scroll that tells how to decode a spell."
                            theo "Hmmmm... This spell allows its caster to seek inspiration..."
                            play sound "itemacquired.mp3"
                            "Theo remembered the Grace Spell!"
                            $ graceUnlocked = True
                        else:
                            "The chest has already been opened."
                    "Back":
                        pass
            elif roomNumber == 16: #More forest
                menu:
                    "Trees":
                        "Theo thinks about the people who have been turned into trees."
                        theo "No, I won't hurt them. Those poor people will be saved!" with vpunch
                    "Grass":
                        theo "Hang on, what am I doing!? There's no reason to open it!"
                    "Back":
                        pass
            elif roomNumber == 17: #Camu's Gate
                menu:
                    "Hedge":
                        theo "Hang on, what am I doing!? There's no reason to open it!"
                    "Gate":
                        if doorCOpened == False:
                            "Hrrrrrrnnnnggghh! Ugh... Unfortunately, it won't open."
                            "You're going to need the key to open that."
                        else:
                            "But the gate is already open!"
                    "Back":
                        pass
            elif roomNumber == 18: #More forest
                menu:
                    "Trees":
                        "Theo thinks about the people who have been turned into trees."
                        theo "No, I won't hurt them. Those poor people will be saved!" with vpunch
                    "Path":
                        "Hrrrrrrnnnnggghh! Ugh... Unfortunately, it won't open."
                    "Back":
                        pass
            elif roomNumber == 19: #Treant Room
                menu:
                    "Square":
                        "Hrrrrrrnnnnggghh! Ugh... Unfortunately, it won't open."
                    "Treant":
                        if keyMObtained == False:
                            play sound "enemyappear.mp3"
                            stop music
                            "Suddenly, Treant attacks you!"
                            $ enemy1number = 0
                            $ enemy2number = 3
                            $ enemy3number = 0
                            jump battleSetup
                        else:
                            treant "Hey, knock it off! I'm trying to turn over a new leaf here!"
                    "Back":
                        pass
        #Martel's Domain
            elif roomNumber == 20: #Entrance to Martel's Domain
                menu:
                    "Trees":
                        "Save us, Theo!"
                    "Back":
                        pass
        #The Well
        #Shabow's Domain
        #Camu's Domain
        #The Pagoda
        #Underground Ruins
        #The Castle
        #The Mirror World
        #Postgame Dungeon
            jump gameMenu
        "Hit":
            if roomNumber == 1: #Old Man Room
                menu:
                    "In room":
                        "You hit it, but nothing happens."
                    "The Old Man":
                        "You strike at the old man, upsetting him." with vpunch
                        oldman "What the- Theo! I didn't raise you to be such a human as that!"
                        theo "Sorry, old man. I don't know what came over me..."
                    "Back":
                        pass
            elif roomNumber == 2: #Mill Room
                menu:
                    "In room":
                        "You hit it, but nothing happens."
                    "Millstone":
                        "Despite your best efforts, the millstone remains perfectly intact."
                    "Back":
                        pass
            elif roomNumber == 3: #Old Man Gate
                menu:
                    "Wall":
                        "You hit it, but nothing happens."
                    "Front Door":
                        theo "Wait, this is my own house. I don't need to knock!"
                    "Back":
                        pass
            elif roomNumber == 4: #Crossroads
                menu:
                    "Trees":
                        "Theo thinks about the people who have been turned into trees."
                        theo "No, I won't hurt them. Those poor people will be saved!" with vpunch
                    "Grass":
                        "You hit it, but nothing happens."
                    "Back":
                        pass
            elif roomNumber == 5: #Shaman's Door
                menu:
                    "Front Door":
                        "Theo knocks on the shaman's door."
                        shaman "Do you have any orders for me? Come in if you have."
                    "Back":
                        pass
            elif roomNumber == 6: #Shaman's Room
                menu:
                    "In room":
                        "You hit it, but nothing happens."
                    "Shaman":
                        "The Shaman casts a barrier, parrying Theo's attack with ease." with vpunch
                        shaman "You're lucky I have good instincts. Keep this up, and I'll pray for you no more."
                    "Crystal Ball":
                        "The crystal ball looks sturdy, sure, but even attempting to break it would have nasty consequences."
                        "Theo wisely decides against it."                    
                    "Back":
                        pass
            elif roomNumber == 7: #Forest
                menu:
                    "Surroundings":
                        "You hit it, but nothing happens."
                    "Trees":
                        "Theo thinks about the people who have been turned into trees."
                        theo "No, I won't hurt them. Those poor people will be saved!" with vpunch
                    "Sign":
                        "You hit it, but nothing happens."
                        "Must be made of some sturdy wood to withstand that attack."
                    "Back":
                        pass
            elif roomNumber == 8: #Martel's Gate
                menu:
                    "Trees":
                        "Theo thinks about the people who have been turned into trees."
                        theo "No, I won't hurt them. Those poor people will be saved!" with vpunch
                    "Gate":
                        "Theo knocks on the door..."
                        "But nobody came."
                        theo "Doesn't look like anyone's guarding this place."
                        theo "Well, besides the trees, but still..."
                    "Back":
                        pass
            elif roomNumber == 9: #Forest
                menu:
                    "Trees":
                        "Theo thinks about the people who have been turned into trees."
                        theo "No, I won't hurt them. Those poor people will be saved!" with vpunch
                    "Path":
                        "You hit it, but nothing happens."
                    "Back":
                        pass
            elif roomNumber == 10: #Forest
                menu:
                    "Trees":
                        "Theo thinks about the people who have been turned into trees."
                        theo "No, I won't hurt them. Those poor people will be saved!" with vpunch
                    "Grass":
                        "Hmmm... That grass looks kinda sharp."
                        "Don't want to cut your hand on it; best leave the grass alone."
                    "Sign":
                        "You hit it, but nothing happens."
                        "Must be made of some sturdy wood to withstand that attack."
                    "Back":
                        pass
            elif roomNumber == 11: #Shabow's Gate
                menu:
                    "Trees":
                        "Theo thinks about the people who have been turned into trees."
                        theo "No, I won't hurt them. Those poor people will be saved!" with vpunch
                    "Gate":
                        "Theo knocks on the door..."
                        "Nothing but silence."
                        theo "Not even a shadow to watch over this imposing gate."
                        theo "Hehe, get it? Because Shadow? And Sha\"b\"ow?"
                        "......"
                        theo "...Not even the trees. I should've taken clown classes."
                    "Back":
                        pass
            elif roomNumber == 12: #Forest
                menu:
                    "Trees":
                        "Theo thinks about the people who have been turned into trees."
                        theo "No, I won't hurt them. Those poor people will be saved!" with vpunch
                    "Small Stone":
                        "You hit it, but nothing happens."
                    "Sign":
                        "You hit it, but nothing happens."
                        "Must be made of some sturdy wood to withstand that attack."
                    "Back":
                        pass
            elif roomNumber == 13: #Shaman's Door
                menu:
                    "Front Door":
                        "Theo knocks on the shop's door."
                        shopkeeper "Hi, welcome! Feel free to come in!"
                    "Back":
                        pass
            elif roomNumber == 14: #Shopkeeper's Room
                menu:
                    "In room":
                        "You hit it, but nothing happens."
                    "Shopkeeper":
                        $ renpy.block_rollback()
                        "Before Theo could strike, the shopkeeper slams his face with a frying pan!" with vpunch
                        "Bash! Bash! Bash!" with vpunch
                        $ hp -= 1
                        shopkeeper "That ought to teach you not to be so terrible!"
                        if hp <= 0:
                            scene bg black with dissolve
                            "The thrashing knocked Theo unconscious. He should have thought twice about picking a fight with a shopkeeper."
                            jump gameOver
                    "Goods for sale":
                        "You'll probably be banned from the store if you vandalize its goods. Best leave them be."
                    "Back":
                        pass
            elif roomNumber == 15: #Grace room
                menu:
                    "In room":
                        "You hit it, but nothing happens."
                    "Chest":
                        "You hit it, but nothing happens."
                    "Back":
                        pass
            elif roomNumber == 16: #More forest
                menu:
                    "Trees":
                        "Theo thinks about the people who have been turned into trees."
                        theo "No, I won't hurt them. Those poor people will be saved!" with vpunch
                    "Small Stone":
                        "You hit it, but nothing happens."
                    "Back":
                        pass
            elif roomNumber == 17: #Camu's Gate
                menu:
                    "Hedge":
                        "You hit it, but nothing happens."
                    "Gate":
                        "Theo knocks on the door..."
                        "No answer."
                        theo "Guess whoever's watching this place is a scaredy cat."
                        theo "Or a nobody cat, from the looks of things."
                    "Back":
                        pass
            elif roomNumber == 18:
                menu:
                    "Trees":
                        "Theo thinks about the people who have been turned into trees."
                        theo "No, I won't hurt them. Those poor people will be saved!" with vpunch
                    "Path":
                        "You hit it, but nothing happens."
                    "Back":
                        pass
            elif roomNumber == 19: #Treant's Room
                menu:
                    "Square":
                        "You hit it, but nothing happens."
                    "Treant":
                        if keyMObtained == False:
                            play sound "enemyappear.mp3"
                            stop music
                            "Suddenly, Treant attacks you!"
                            $ enemy1number = 0
                            $ enemy2number = 3
                            $ enemy3number = 0
                            jump battleSetup
                        elif moonCompleted == False or treantFruitObtained == True:
                            treant "Hey, knock it off! I'm trying to turn over a new leaf here!"
                        else:
                            treant "Oww... Okay, if you wanted my fruit so badly, you could have asked... Sheesh."
                            $ treantFruitObtained = True
                            "Obtained the Treant Fruit!"
                    "Treant Fruit" if moonCompleted == True and treantFruitObtained == False:
                        "The fruit is sturdier than you think, and blocks your attack completely!"
                    "Back":
                        pass
        #Martel's Domain
            elif roomNumber == 20: #Entrance to Martel's Domain
                menu:
                    "Trees":
                        "Save us, Theo!"
                    "Back":
                        pass
        #The Well
        #Shabow's Domain
        #Camu's Domain
        #The Pagoda
        #Underground Ruins
        #The Castle
        #The Mirror World
        #Postgame Dungeon
            jump gameMenu
        "Item":
            menu:
                "Restoratives":
                    menu:
                        "Barley ([barleysOwned])" if barleysOwned > 0:
                            if hp < maxhp:
                                $ wheatsOwned -= 1
                                $ hp += 20
                                if hp > maxhp:
                                    $ hp = maxhp
                                "You consumed a barley and restored HP."
                            else:
                                "But you are already at full strength!"
                        "Wheat ([wheatsOwned])" if wheatsOwned > 0:
                            if hp < maxhp:
                                $ barleysOwned -= 1
                                $ hp += 50
                                if hp > maxhp:
                                    $ hp = maxhp
                                "You consumed a wheat and restored a lot of HP."
                            else:
                                "But you are already at full strength!"
                        "Herb ([herbsOwned])" if herbsOwned > 0:
                            if mp < maxmp:
                                $ herbsOwned -= 1
                                "You consumed a herb and restored MP."
                                if mp > maxmp:
                                    $ mp = maxmp
                            else:
                                "But your magic power is already full!"
                        "Yellow Fruit" if yellowFruitObtained == True:
                            $ renpy.block_rollback()
                            $ yellowFruitObtained = False
                            "Without thinking, you gobble up the strange yellow fruit."
                            $ mp -= 20
                            if mp < 0:
                                $ mp = 0
                            "Yuck! That thing's nasty!"
                            "You feel the fruit sap away your MP as you digest it..."
                            "...Nope. No rolling back that mistake. Just great."
                        "Treant Fruit" if treantFruitObtained == True:
                            $ treantFruitObtained = False
                            "You gobble up the fruit the Treant gave you."
                            $ hp = maxhp
                            $ mp = maxmp
                            "Your HP and MP is fully restored!"
                        "Back":
                            pass
                "Keys and Eggs":
                    menu:
                        "Martel's Key" if keyMObtained == True:
                            if roomNumber == 8:
                                $ doorMOpened = True
                                scene bg gateunlocked
                                "You slot Martel's key into the gate, opening the way forward!"
                            else:
                                "The key to unlock Martel's gate."
                                if martelFound == True:
                                    "You don't need it anymore as you can warp to him now, but it would still be good to keep on hand."
                        "Shabow's Key" if keySObtained == True:
                            if roomNumber == 11:
                                $ doorSOpened = True
                                scene bg gateunlocked
                                "You slot Shabow's key into the gate, opening the way forward!"
                            else:
                                "The key to unlock Shabow's gate."
                                if shabowFound == True:
                                    "You don't need it anymore as you can warp to him now, but it would still be good to keep on hand."
                        "Camu's Key" if keyCObtained == True:
                            if roomNumber == 17:
                                $ doorCOpened = True
                                scene bg gateunlocked
                                "You slot Camu's key into the gate, opening the way forward!"
                            else:
                                "The key to unlock Camu's gate."
                                if camuFound == True:
                                    "You don't need it anymore as you can warp to her now, but it would still be good to keep on hand."
                        "White Egg" if whiteEggObtained == True:
                            "The white egg from Martel's pigeon, representing wisdom."
                        "Blue Egg" if blueEggObtained == True:
                            "The blue egg from Shabow's pigeon, representing courage."
                        "Red Egg" if redEggObtained == True:
                            "The red egg from Camu's pigeon, representing love."
                        "Back":
                            pass                            
                "Misc":
                    menu:
                        "Magic Book":
                            "You read the magic book."
                            "\"Field Magic\""
                            "Teleport - Allows you to return to your trusted friends."
                            if recoverMinUnlocked == True: 
                                "RecoverMin - Heals 30 HP."
                            if recoverMedUnlocked == True:
                                "RecoverMed - Heals 60 HP."
                            if recoverMaxUnlocked == True:
                                "RecoverMax - Fully restores HP."
                            if graceUnlocked == True:
                                "Grace - Use it at the church to see what happens!"
                            if secretUnlocked == True:
                                "Secret - ??????????"
                            if level == 1:
                                "................!"
                                "You haven't read the book of battle magic yet!"
                                "Might want to strengthen yourself and learn some more spells."
                            else:
                                "\"Battle Magic\""
                                "Most magic can be divided into four levels."
                                "Level 1 Magic is inaccurate, sometimes firing back at its caster."
                                "Level 2 Magic always hits its mark."
                                "Level 3 Magic hits all enemies, but also harms its caster."
                                "Level 4 Magic is the strongest, attacking everybody except the person who cast it."
                                "If possible, stick to casting even-numbered magic."
                        "Charm" if charmObtained == True:
                            "A magic charm. Who knows what it could do?"
                        "Ruby" if rubyObtained == True:
                            "A beautiful ruby. It gives off a fierce aura."
                        "Spore" if sporeObtained == True:
                            "A fungal spore. You get sleepy just staring at it."
                        "Doll" if dollObtained == True:
                            "A doll you scooped out of the well. Just holding it in your hands makes you feel safe."
                        "Moon Fragment" if moonFragmentObtained == True:
                            "A fragment of a moon ornament. Surely it must go somewhere, but where exactly?"
                        "Ring" if ringObtained == True:
                            "A small ring to be worn on your finger."
                            "Perhaps it could let you speak to the visions in the lakes?"
                        "Sapphire" if sapphireObtained == True:
                            "A beautiful sapphire. Did this belong to someone?"
                        "Unicorn Horn" if unicornHornObtained == True:
                            "Camu's severed unicorn horn."
                            "Use it to unlock the pagoda!"
                        "Fairy Lamp" if fairyLampObtained == True:
                            "The lamp you received from the lake fairies."
                            "It doesn't seem to do anything at the moment."
                        "Ivy Seed" if ivySeedObtained == True:
                            "A seed of for an ivy plant."
                            "Sadly, there are no good spots to plant it right now."
                        "Back":
                            pass  
                "Back":
                    pass
            jump gameMenu
        "Magic":
            menu:
                "Teleport":
                    menu:
                        "Old Man's House":
                            scene bg black with dissolve
                            scene bg oldManRoom
                            show oldman
                            with dissolve
                            if roomNumber > 2 and roomNumber != 14 and roomNumber != 15:
                                play music "oldmanroom.mp3"
                            "Home sweet home. You've returned to the old man's room."
                            $ roomNumber = 1
                            $ monsterEncounter = renpy.random.randint(1, 20)
                        "Shaman's House":
                            scene bg black with dissolve
                            scene bg shamanRoom
                            show shaman
                            with dissolve
                            if roomNumber != 6:
                                play music "shamanroom.mp3"
                            $ roomNumber = 6
                            $ monsterEncounter = renpy.random.randint(1, 20)
                        "Forest Shop" if shopkeepVisits >= 1:
                            scene bg black with dissolve
                            scene bg shopkeeper
                            show shopkeeper
                            with dissolve
                            if roomNumber > 2 and roomNumber != 14 and roomNumber != 15:
                                play music "oldmanroom.mp3"
                            $ roomNumber = 14
                            $ monsterEncounter = renpy.random.randint(1, 20)
                        "Back":
                            pass
                "RecoverMin" if recoverMinUnlocked == True:
                    if mp >= 2 and hp < maxhp:
                        "Theo casts RecoverMin!"
                        $ mp -= 2
                        $ hp += 30
                        if hp > maxhp:
                            $ hp = maxhp
                        "Theo's health has been restored."
                        $ monsterEncounter = renpy.random.randint(1, 20)
                    elif hp >= maxhp:
                        "Theo attempts to cast RecoverMin..."
                        "But he is already at full HP."
                        $ monsterEncounter = renpy.random.randint(1, 20)
                    else:
                        "Theo attempts to cast RecoverMin..."
                        "But he does not have enough MP..."
                        $ monsterEncounter = renpy.random.randint(1, 20)
                "RecoverMed" if recoverMedUnlocked == True:
                    if mp >= 4 and hp < maxhp:
                        "Theo casts RecoverMed!"
                        $ mp -= 4
                        $ hp += 60
                        if hp > maxhp:
                            $ hp = maxhp
                        "Theo's health has been restored."
                        $ monsterEncounter = renpy.random.randint(1, 20)
                    elif hp >= maxhp:
                        "Theo attempts to cast RecoverMed..."
                        "But he is already at full HP."
                        $ monsterEncounter = renpy.random.randint(1, 20)
                    else:
                        "Theo attempts to cast RecoverMed..."
                        "But he does not have enough MP..."
                        $ monsterEncounter = renpy.random.randint(1, 20)
                "RecoverMax" if recoverMaxUnlocked == True:
                    if mp >= 6 and hp < maxhp:
                        "Theo casts RecoverMax!"
                        $ mp -= 6
                        $ hp = maxhp
                        "Theo's health has been restored."
                        $ monsterEncounter = renpy.random.randint(1, 20)
                    elif hp >= maxhp:
                        "Theo attempts to cast RecoverMax..."
                        "But he is already at full HP."
                        $ monsterEncounter = renpy.random.randint(1, 20)
                    else:
                        "Theo attempts to cast RecoverMax..."
                        "But he does not have enough MP..."
                        $ monsterEncounter = renpy.random.randint(1, 20)
                "Grace" if graceUnlocked == True:
                    "Theo casts Grace!"
                    if roomNumber == 26:
                        "Theo's mother, Queen Remy, appears!"    
                    elif roomNumber == 25 or roomNumber == 27:
                        "He can make out some sort of voice, but needs to get closer..."
                    else:
                        "But nothing happens!"
                    $ monsterEncounter = renpy.random.randint(1, 20)
                "Secret" if secretUnlocked == True:
                    "Theo casts Secret!"
                    if roomNumber == 150:
                        "The mirror shatters, revealing the entrance to the mirror dimension!"
                    else:
                        "But nothing happens!"
                    $ monsterEncounter = renpy.random.randint(1, 20)
                "Back":
                    pass
            jump gameMenu
        "Stats":
            $ monsterEncounter = renpy.random.randint(1, 20)
            $ statCheck = True
            jump levelCheck

label turnCounter:
    $ totalTurns += 1
    $ turnCounter += 1
    jump battleScene

label battleSetup:
    play music "battle.mp3"
    $ monsterssetup += 1
    #"Monster Set Up: [monsterssetup]" #Debugging; do not uncomment
    if enemy1number != 0 and monsterssetup == 2:
        $ monsternumber = enemy1number
        $ enemy1name = monstername
        #"Monster Number 1: [enemy1name]" #Debugging; do not uncomment
        $ enemy1hp = monsterhp
        $ enemy1mp = monstermp
        $ enemy1dex = monsterdex
        $ enemy1stam = monsterstam
        $ enemy1agil = monsteragil
        $ enemy1golddrop = monstergolddrop
        $ enemy1expdrop = monsterexpdrop
        $ enemy1sprite = monstersprite
    if monsterssetup == 1:
        jump bestiary
    if enemy2number != 0 and monsterssetup == 3:
        $ monsternumber = enemy2number
        $ enemy2name = monstername
        #"Monster Number 2: [enemy2name]" #Debugging; do not uncomment
        $ enemy2hp = monsterhp
        $ enemy2mp = monstermp
        $ enemy2dex = monsterdex
        $ enemy2stam = monsterstam
        $ enemy2agil = monsteragil
        $ enemy2golddrop = monstergolddrop
        $ enemy2expdrop = monsterexpdrop
        $ enemy2sprite = monstersprite
    if monsterssetup == 2:
        jump bestiary
    if enemy3number != 0 and monsterssetup == 4:
        $ monsternumber = enemy3number
        $ enemy3name = monstername
        #"Monster Number 3: [enemy3name]" #Debugging; do not uncomment
        $ enemy3hp = monsterhp
        $ enemy3mp = monstermp
        $ enemy3dex = monsterdex
        $ enemy3stam = monsterstam
        $ enemy3agil = monsteragil
        $ enemy3golddrop = monstergolddrop
        $ enemy3expdrop = monsterexpdrop
        $ enemy3sprite = monstersprite
    if monsterssetup == 3:
        jump bestiary
    $ monsterssetup = 0
    if enemy1sprite != "Null": #If there's a better way to call the enemy's sprite than this, please tell me. This'll just get unwieldly fast.
        if enemy1sprite == "moth":
            show moth1 at left
        elif enemy1sprite == "skeleton":
            show skeleton1 at left
    if enemy2sprite != "Null":
        if enemy2sprite == "moth":
            show moth2 at center
        elif enemy2sprite == "skeleton":
            show skeleton2 at center
        elif enemy2sprite == "treant":
            show treant at center
    if enemy3sprite != "Null":
        if enemy3sprite == "moth":
            show moth3 at right
        elif enemy3sprite == "skeleton":
            show skeleton3 at right
    jump turnCounter

label battleScene:
    if hp > 0 and (enemy1hp > 0 or enemy2hp > 0 or enemy3hp > 0):
        menu:
            "Attack":
                if swordLevel < 5:
                    menu:
                        "[enemy1name]" if enemy1hp > 0:
                            $ target = 1
                            $ enemy1hp -= dexterity - enemy1stam
                            "Theo attacks!"
                            "[enemy1name] takes [dexterity - enemy1stam] damage!"
                            if enemy1hp <= 0:
                                "[enemy1name] has been defeated!"
                                if enemy1number == 1:
                                    hide moth1
                                elif enemy1number == 2:
                                    hide skeleton1
                                $ enemy1number = 0
                        "[enemy2name]" if enemy2hp > 0:
                            $ target = 2
                            $ enemy2hp -= dexterity - enemy2stam
                            "Theo attacks!"
                            "[enemy2name] takes [dexterity - enemy2stam] damage!"
                            if enemy2hp <= 0:
                                "[enemy2name] has been defeated!"
                                if enemy2number == 1:
                                    hide moth2
                                elif enemy2number == 2:
                                    hide skeleton2
                                $ enemy2number = 0
                        "[enemy3name]" if enemy3hp > 0:
                            $ target = 3
                            $ enemy3hp -= dexterity - enemy3stam
                            "Theo attacks!"
                            "[enemy3name] takes [dexterity - enemy3stam] damage!"
                            if enemy3hp <= 0:
                                "[enemy3name] has been defeated!"
                                if enemy3number == 1:
                                    hide moth3
                                elif enemy3number == 2:
                                    hide skeleton3
                                $ enemy3number = 0
                else:
                    "The Sword of Hope strikes at all enemies!"
            "Item":
                menu:
                    "Restoratives":
                        menu:
                            "Barley ([barleysOwned])" if barleysOwned > 0:
                                if hp < maxhp:
                                    $ wheatsOwned -= 1
                                    $ hp += 20
                                    if hp > maxhp:
                                        $ hp = maxhp
                                    "You consumed a barley and restored HP."
                                else:
                                    "But you are already at full strength!"
                            "Wheat ([wheatsOwned])" if wheatsOwned > 0:
                                if hp < maxhp:
                                    $ barleysOwned -= 1
                                    $ hp += 50
                                    if hp > maxhp:
                                        $ hp = maxhp
                                    "You consumed a wheat and restored a lot of HP."
                                else:
                                    "But you are already at full strength!"
                            "Herb ([herbsOwned])" if herbsOwned > 0:
                                if mp < maxmp:
                                    $ herbsOwned -= 1
                                    "You consumed a herb and restored MP."
                                    if mp > maxmp:
                                        $ mp = maxmp
                                else:
                                    "But your magic power is already full!"
                            "Yellow Fruit" if yellowFruitObtained == True:
                                $ renpy.block_rollback()
                                $ yellowFruitObtained = False
                                "Without thinking, you gobble up the strange yellow fruit."
                                $ mp -= 20
                                if mp < 0:
                                    $ mp = 0
                                "Yuck! That thing's nasty!"
                                "You feel the fruit sap away your MP as you digest it..."
                                "...Nope. No rolling back that mistake. Just great."
                            "Treant Fruit" if treantFruitObtained == True:
                                $ treantFruitObtained = False
                                "You gobble up the fruit the Treant gave you."
                                $ hp = maxhp
                                $ mp = maxmp
                                "Your HP and MP is fully restored!"
                            "Back":
                                jump battleScene
                    "Keys and Eggs":
                        menu:
                            "Martel's Key" if keyMObtained == True:
                                "Theo attempts to use Martel's Key, but nothing happens."
                            "Shabow's Key" if keySObtained == True:
                                "Theo attempts to use Shabow's Key, but nothing happens."
                            "Camu's Key" if keyCObtained == True:
                                "Theo attempts to use Camu's Key, but nothing happens."
                            "White Egg" if whiteEggObtained == True:
                                "Theo attempts to use the White Egg, but nothing happens."
                            "Blue Egg" if blueEggObtained == True:
                                "Theo attempts to use the Blue Egg, but nothing happens."
                            "Red Egg" if redEggObtained == True:
                                "Theo attempts to use the Red Egg, but nothing happens."
                            "Back":
                                jump battleScene
                    "Misc":
                        menu:
                            "Magic Book":
                                "Now probably isn't a good time to study up on your magic!"
                            "Charm" if charmObtained == True:
                                "Theo attempts to use the Charm, but nothing happens."
                            "Ruby" if rubyObtained == True:
                                "Theo uses the Ruby!"
                                "His enemies are damaged!"
                            "Spore" if sporeObtained == True:
                                "Theo uses the Spore!"
                                "His enemies fall asleep!"
                            "Doll" if dollObtained == True:
                                "Theo uses the Doll!"
                                "He feels better guarded against enemy attacks!"
                            "Moon Fragment" if moonFragmentObtained == True:
                                "Theo attempts to use the Moon Fragment, but nothing happens."
                            "Ring" if ringObtained == True:
                                "Theo attempts to use the Ring, but nothing happens."
                            "Sapphire" if sapphireObtained == True:
                                "Theo attempts to use the Sapphire, but nothing happens."
                            "Unicorn Horn" if unicornHornObtained == True:
                                "Theo attempts to use the Unicorn Horn, but nothing happens."
                            "Fairy Lamp" if fairyLampObtained == True:
                                "Theo attempts to use the Fairy Lamp, but nothing happens."
                            "Ivy Seed" if ivySeedObtained == True:
                                "Theo attempts to use the Ivy Seed, but nothing happens."
                            "Back":
                                    jump battleScene
                    "Back":
                        jump battleScene
            "Magic":
                jump battleScene
            "Flee":
                if escapable == True:
                    "Theo escapes from the enemies!"
                    $ turnCounter = 0
                    $ enemy1number = 0
                    $ enemy2number = 0
                    $ enemy3number = 0
                    stop music
                    hide moth1
                    hide moth2
                    hide moth3
                    hide skeleton1
                    hide skeleton2
                    hide skeleton3
                    if roomNumber <= 19:
                        play music "riccarfield.mp3"
                    jump gameMenu
                else:
                    "Theo attempts to escape, but finds himself surrounded on all fronts!"

    if hp <= 0:
        $ dexAlter = 0
        $ stamAlter = 0
        $ agilAlter = 0
        stop music
        play sound "unused.mp3"
        "Thou art dead."
        jump gameOver

    if enemy1hp <= 0 and enemy2hp <= 0 and enemy3hp <= 0:
        $ exp += enemy1expdrop + enemy2expdrop + enemy3expdrop
        $ gold += enemy1golddrop + enemy2golddrop + enemy3golddrop
        $ escapable = True
        $ dexAlter = 0
        $ stamAlter = 0
        $ agilAlter = 0
        stop music
        play sound "victory.mp3"

        "Thou hast done well to defeat their foes."
        "Thou has gained [enemy1expdrop + enemy2expdrop + enemy3expdrop] experience points!"
        "Thou has gained [enemy1golddrop + enemy2golddrop + enemy3golddrop] gold!"
        if gold > 255:
            $ gold = 255
            "But thy wallet cannot contain all of the spoils! Thou must regrettably leave some behind..."
        if roomNumber <= 19:
            play music "riccarfield.mp3"
        jump levelCheck
    else:
        jump turnCounter

label treantDefeat:
    treant "Help! Help! I surrender!"
    theo "Wait, seriously?"
    treant "I'm sorry! I was wrong! I'll be good from now on, so please stop the torture!"
    theo "And why should I believe you?"
    treant "H-here! I stole this key from the pigeon earlier! You can have it, but please leave me alone!"
    $ keyMObtained = True
    play sound "itemacquired.mp3"
    "Treant hands over Martel's key while crying big tears."
    theo "Hmmm... I'll keep you to your promise. Thanks for the key."
    jump gameMenu

label gameOver:
    $ roomNumber = 1
    scene bg oldmanroom
    show oldman
    with dissolve
    play music "oldmanroom.mp3"
    $ hp = 20
    $ mp = 20
    theo "Ouch... That smarts..."
    oldman "Do not despair, Theo!"
    oldman "Be careful not to use up your power again!"
    theo "Sorry. I'll be more careful."
    oldman "Don't forget to speak with the shaman before you set out again."
    oldman "Now get out there and continue where you left off! Good luck, Theo!"
    jump gameMenu

label ending:
    play music "riccarfield.mp3"
    "Exhausted from the battles, Prince Theo stood before a giant painting of a dragon on the wall."
    theo "What!?"
    "To his surprise, the Sword of Hope, \"Wish\", was stuck in the chest of the dragon painting."
    unknown "Ugggghhhh..."
    "Behind him, Theo could make out an anguished cry."
    theo "Father, be brave!"
    "Theo's shout awoke the unconscious king, returning him to his senses."
    king "What... What happened...? I can't... remember anything..."
    king "It's been like a long, bad dream..."
    king "Who- Who are you...?"
    theo "Father, it's me! Your son, Theo!"
    king "My... son...?"
    king "Oh, that mark on your left arm! You are the one chosen by the Sword of Hope!"
    "Suddenly, the painting crashed onto the floor with a great thud." with vpunch
    theo "Father, quickly! We need to get out of here!"
    "Theo escorted King Hennessy out of the weird cave."
    scene bg black with dissolve
    scene bg livingroom with dissolve
    "As the two of them left the strange world, it crumbled into a shapeless mass."
    "The darkness vanished, and the country became warm and bright."
    "With peace restored, the three wizards returned the castle back to the surface."
    "They wished for peace and wealth for all of Riccar."
    "And..."
    "Theo's great deed became a legend throughout the land, remembered by all..."
    "\"He who bears the sign of hope on his left arm shall save the world!\""
    jump credits

label credits:
    scene black with dissolve
    pause 4.0
    
    $ creditsString = """
    A Game By Kaito Suzuki

    Game developed in Renpy
    No generative AI was used in the making of this game.
    Graphics made using Paint.NET
    Soundtrack pulled from original game.
    
    {u}{size=+6}Special Thanks{/size}{/u}
    The Hack the Limit Hackathon for spurning me into making this game.
    Wilson Lau, whose walkthrough for the original game I used as a reference point.
        
    {u}{size=+6}Original game credits{/size}{/u}
    {b}Music{/b}
    Hiroyuki Masuno

    {b}Original game (c)1989{/b}
    {b}Developed by Kemco{/b}    
    {b}Published by Seika{/b}    
    {b}Licensed by Nintendo{/b}

    Thank you for playing my game!
    """

    show bg black zorder 5:
        ypos 0.9

    play music "epilogue.mp3" fadein 1.0 fadeout 1.0

    show text "{size=*3}Credits" with dissolve
    pause 2.0
    hide text with dissolve

    show text "[creditsString]":
        ypos 1.5
    with dissolve

    show text "[creditsString]":
        ypos -1.5
    with MoveTransition(170)

    pause 0.5
    hide text with dissolve

    return

