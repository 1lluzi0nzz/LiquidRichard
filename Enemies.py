import random

class Skeleton:
    def __init__(self):
        ranName = ['calci', 'maro', 'femar' 'ank', 'skal']
        self.name = random.choice(ranName).lower()
        self.type = "skeleton"
        self.HP = 7
        self.strength = 6
        self.dexterity = 2
        self.intelligence = 5
        self.AC = 8
        self.weapon = ['sword']
    def __repr__(self):
        return self.name+"("+self.type+")"
class Goblin:
    def __init__(self):
        ranName = ['JiJi', 'Hava', 'Uruk', 'Indi', 'Vati', 'Yidi', 'Xam']
        self.name = random.choice(ranName).lower()
        self.type = "goblin"
        self.HP = 9
        self.strength = 4
        self.dexterity = 7
        self.intelligence = 1
        self.AC = 8
        self.weapon = ['dagger', 'shortbow']
    def __repr__(self):
        return self.name+"("+self.type+")"
class Orc:
    def __init__(self):
        ranName = ['urkdurk',"drakna", 'ruthkur', 'nugnuthal', 'thrukar']
        self.name = random.choice(ranName).lower()
        self.type = "orc"
        self.HP = 13
        self.strength = 8
        self.dexterity = 2
        self.intelligence = 2
        self.AC = 8
        self.weapon = ['axe']
    def __repr__(self):
        return self.name+"("+self.type+")"
class Necromancer:
    def __init__(self):
        ranName = ['Shalar', 'Kalamach', 'Ji-Von', 'Irithim', 'Vargul', 'Lamdahl', 'Vitrion']
        self.name = random.choice(ranName).lower()
        self.type = "necromancer"
        self.HP = 18
        self.strength = 2
        self.dexterity = 5
        self.intelligence = 8
        self.AC = 8
        self.weapon = ['witch bolt', 'raise dead']
    def __repr__(self):
        return self.name+"("+self.type+")"
class BlackKnight:
    def __init__(self):
        ranName = ['Mozgus the Purifier', 'Nyle the Slain', 'Calmor Sorrowful', 'Slin the Corrupt', 'Kilner RedHelm']
        self.name = random.choice(ranName).lower()
        self.type = "black knight"
        self.HP = 25
        self.strength = 10
        self.dexterity = 3
        self.intelligence = 6
        self.AC = 8
        self.weapon = ['greathammer', 'magic missile']
    def __repr__(self):
        return self.name+"("+self.type+")"
