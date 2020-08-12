import random
import Scenario
import Enemies
from Enemies import Skeleton
from Enemies import Goblin
from Enemies import Orc
from Enemies import Necromancer
from Enemies import BlackKnight

players = []
currentPlayer = 0
downedPlayers = []
enemyParty = []
skillPoints = 37 #Includes Ammended Race Stats
turn = 0
races = ["elf", "human", "dwarf", "halfling"]
charClasses = ["warrior", "wizard", "paladin", "rogue", "ranger", "cleric"]
items = ["ring of healing", "orb of periort", "cloak of stealth", "refillable flask", "staff of flames"]

#weapons
simpleW = ["dagger", "sword", "shortsword", "mace", "quarterstaff"]
greatW = ["longbow", "greathammer", "axe"]
magicW = ["fireball", "witchbolt", "magic missile", "smite"]
dieResult = 1

def getModifier(value):
    if(value <= 1):
        return -2
    elif((value == 2) or (value == 3)):
        return -1
    elif((value == 4) or (value == 5)):
        return 0
    elif((value == 6) or (value == 7)):
        return 1
    elif((value == 8) or (value == 9)):
        return 2
    elif(value >= 10):
        return 3

# Roll a dice between 1 and 20 or whatever number
def rolldie(value):
    dieResult = random.randint(1, int(value))
    print(dieResult)
    return dieResult

def diceCheckPass20(value):
    if(rolldie(20) >= value):
        return True
    else:
        return False

def cycleCurrentPlayer(currentPlayer):
    print(len(players))
    if(currentPlayer == (len(players)-1)):
        return 0
    else:
        return currentPlayer + 1

def updateEventCounter():
    Scenario.currentEvent = Scenario.currentEvent + 1

def setStatusCounter(value):
    Scenario.currentStatus = int(value)

def clearEnemySquad():
    new = []
    return new

def generateEnemyParty():
    enemyCount = random.randint(1, 5)
    i = 0
    while(i < enemyCount):
        val = random.randint(1, 20)
        if(val <= 8):
            skel = Skeleton()
            enemyParty.append(skel)
        elif((val > 8) and (val <= 14)):
            gob = Goblin()
            enemyParty.append(gob)
        elif((val > 14) and (val <= 17)):
            orc = Orc()
            enemyParty.append(orc)
        elif((val > 17) and (val <= 19)):
            necro = Necromancer()
            enemyParty.append(necro)
        elif(val == 20):
            bk = BlackKnight()
            enemyParty.append(bk)

        i += 1
