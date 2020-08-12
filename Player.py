import random
import DND
class Player:
    #AC = conMOD + armorSTAT
    def __init__(self, name, strength, dexterity, constitution, intelligence, charisma, race, charClass, item):
        self.name = name
        self.strength = strength
        self.dexterity = dexterity
        self.constitution = constitution
        self.intelligence = intelligence
        self.charisma = charisma
        self.race = race.lower()
        self.charClass = charClass.lower()
        self.item = item.lower()
        self.health = 0
        self.gold = 0
        self.inventory = []
        self.inventory.append(item)
        #Race Buffs
        if(self.race == "elf"):
            self.dexterity = int(self.dexterity) + 2
        elif(self.race == "human"):
            self.strength = int(self.strength) + 2
        elif(self.race == "dwarf"):
            self.constitution = int(self.constitution) + 2
        elif(self.race == "halfling"):
            self.intelligence = int(self.intelligence) + 2

        #Class Item Starts
        if(self.charClass == "warrior"):
            self.health = 9 + DND.getModifier(int(self.constitution))
            self.inventory.append("sword")
            self.inventory.append("shield")
            self.inventory.append("chain vest")
        elif(self.charClass == "wizard"):
            self.health = 5 + DND.getModifier(int(self.constitution))
            self.inventory.append("quarterstaff")
            self.inventory.append("cloth robe")
            self.inventory.append("fireball")
            self.inventory.append("light")
            self.inventory.append("charm")
            self.inventory.append("magic missile")
            self.inventory.append("familiar")
        elif(self.charClass == "paladin"):
            self.health = 15 + DND.getModifier(int(self.constitution))
            self.inventory.append("greathammer")
            self.inventory.append("platemail")
        elif(self.charClass == "rogue"):
            self.health = 7 + DND.getModifier(int(self.constitution))
            self.inventory.append("longbow")
            self.inventory.append("leather armor")
        elif(self.charClass == "ranger"):
            self.health = 9 + DND.getModifier(int(self.constitution))
            self.inventory.append("longbow")
            self.inventory.append("leather armor")
        elif(self.charClass == "cleric"):
            self.health = 12 + DND.getModifier(int(self.constitution))
            self.inventory.append("mace")
            self.inventory.append("leather armor")
            self.inventory.append("goodberry")
            self.inventory.append("spare the dying")
            self.inventory.append("heal wounds")
            self.inventory.append("smite")
    def isValid(p):
        if((int(p.strength) + int(p.dexterity) + int(p.constitution) + int(p.intelligence) + int(p.charisma)) != DND.skillPoints):
            print("Skill Points not Equal to ",DND.skillPoints)
            return False
        elif(p.race not in DND.races):
            print("Race Fail")
            return False
        elif(p.charClass not in DND.charClasses):
            print("Class Fail")
            return False
        elif(p.item not in DND.items):
            print("Item Fail")
            return False
        else:
            return True

    def getAC():
        return True

    def __repr__(self):
        return self.name+"("+self.charClass+")"
