import random



class BRFighter:
    """
    Defines one fighter in battle royale simulator.
    """

    def __init__(self, name, startingHP, minAtt, maxAtt, figherType):
        self.name = name
        self.hp = startingHP
        self.minAtt = minAtt
        self.maxAtt = maxAtt
        self.type = fighterType


    def attack(self,other):
        """
        Calculates damage for a single attack by else on other,
        applies damage and checks for elimination.
        """
        print(f"{self.name} attacks {other.name}!")
        attackRoll = random.randint(self.minAtt, self.maxAtt)
        print(f"{self.name} rolls {attackRoll} damage!")
        if self.advantage(other):
            print("It's super effective!")
            attackRoll *= 2
        if other.takeDamage(attackRoll):
            print(f"{other.name} has been eliminated!")
            return True
        else:
            print(f"{other.name} is down to {other.hp} hit points.")
            return False
                   


    def advantage(self,other):
        """
        Returns True if self has type advantage over other,
        false otherwise.
        """
        if self.type == "rock" and other.type == "scissors":
            return True
        elif self.type == "scissors" and other.type == "paper":
            return True
        elif self.type == "paper" and other.type == "rock":
            return True
        else:
            return False
        

    def takeDamage(self,damage):
        """
        Reduces self's HP by damage. Returns true if HP has been
        reduced to <= 0.
        """
        self.hp -= damage
        return self.hp <= 0

def simulate(figherList):
    """
    Has randomly-selected members of fighterList attack
    other randomly-selected members of fighterList
    until there is only one member of fighterList
    """
    while len(fighterList) > 1:
        attIndex = random,randint(0, len(figherList)-1)
        defIndex = random.randint(0, len(fighterList) -2)
        if defIndex >= attackIndex:
            defIndex +=1
        if figherList[attIndex].attack(figherList[defIndex]):
            fighterList.pop(defIndex)
        
