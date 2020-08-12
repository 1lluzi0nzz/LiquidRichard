import random
import Player
import DND

currentStatus = 0
currentEvent = 1
response = 0
message = ""
result = ""

event1Intro = "The party is approached by a same man. ""“Would you like to view my wares?"""+"\n    0 - Sure\n    1 - No\n    2 - Fuck Off\n"
event2Intro = "You encountered a chungus on the road, it be mad."

def loadEvent1(currentStatus, response):
    
    if(currentStatus == 0 and response == 0):
        #currentStatus = 1
        DND.setStatusCounter(1)
        return "The old man has a sword, a shield, and a mystery flask for sale. Would you like to buy?"+"\n\n    3 - Sword\n    4 - Shield\n    5 - Mystery Flask\n    6 - Nothing\n"
    elif(currentStatus == 0 and response == 1):
        DND.setStatusCounter(3)
        return "You leave the old man continuing onwards through the market, until you come across a Royal guard.\n    0 - Ask for dirctions to the kings palace\n    1 - Turn around and walk away"
    elif(currentStatus == 0 and response == 2):
        if(DND.diceCheckPass20(12)):
            DND.updateEventCounter()
            return f'The old man didnt take kindly to that. ""“You’ll regret that.”"" He pulls out a sword and swings.\n\nSuccess: {DND.players[DND.currentPlayer]} gracefully duck avoiding the blow entirely and then skillfully disarm the man.\n\nTHE PARTY COMPLETED THE EVENT'
        else:
            DND.players[DND.currentPlayer].health -= 4
            DND.updateEventCounter()
            return f'The old man didnt take kindly to that. """Youll regret that.”"" He pulls out a sword and swings.\n\nFail: Ouch! {DND.players[DND.currentPlayer]} have a deep slash on your arm take 4 dmg.\n\nTHE PARTY COMPLETED THE EVENT'
    elif(currentStatus == 1 and response == 3):
        DND.players[DND.currentPlayer].inventory.append("sword")
        DND.updateEventCounter()
        return f'{DND.players[DND.currentPlayer].name} bought the sword\n\nTHE PARTY COMPLETED THE EVENT'
    elif(currentStatus == 1 and response == 4):
        DND.players[DND.currentPlayer].inventory.append("shield")
        DND.updateEventCounter()
        return f'{DND.players[DND.currentPlayer].name} bought the shield\n\nTHE PARTY COMPLETED THE EVENT'
    elif(currentStatus == 1 and response == 5):
        DND.players[DND.currentPlayer].inventory.append("mystery flash")
        DND.updateEventCounter()
        return f'{DND.players[DND.currentPlayer].name} bought the mystery flask\n\nTHE PARTY COMPLETED THE EVENT'
    elif(currentStatus == 1 and response == 6):
        DND.updateEventCounter()
        return f'{DND.players[DND.currentPlayer].name} bought the nothing\n\nTHE PARTY COMPLETED THE EVENT'
    elif(currentStatus == 3 and response == 0):
        DND.updateEventCounter()
        return "Ben didnt write what happens when you ask for directions\n\nTHE PARTY COMPLETED THE EVENT"
    elif(currentStatus == 3 and response == 1):
        DND.updateEventCounter()
        return "Chode Smoker also didnt write what happens when you walk away\n\nTHE PARTY COMPLETED THE EVENT"
    return "DEBUG MESSAGE ERROR: UNSTABLE STATE"