
import random
random.seed(31337)

NUM_COOPERATOR = 2
NUM_DEFECTOR = 2
NUM_TITFORTAT = 2
NUM_GRIMTRIGGER = 2
NUM_COINFLIPPER = 2
NUM_DIEROLLER = 2

POINTS_BOTH_COOPERATE = 1
POINTS_BOTH_DEFECT = 0
POINTS_BETRAYER = 2
POINTS_BETRAYED = -1

GAMES_PER_MATCH = 200

def main():
    theDilemma = Dilemma(POINTS_BOTH_COOPERATE,POINTS_BOTH_DEFECT,POINTS_BETRAYER,POINTS_BETRAYED)

    prisoners = []
    for i in range(NUM_COOPERATOR):
        prisoners.append(Cooperator())
    for i in range(NUM_DEFECTOR):
        prisoners.append(Defector())
    for i in range(NUM_TITFORTAT):
        prisoners.append(TitForTat())
    for i in range(NUM_GRIMTRIGGER):
        prisoners.append(GrimTrigger())
    for i in range(NUM_COINFLIPPER):
        prisoners.append(CoinFlipper())
    for i in range(NUM_DIEROLLER):
        prisoners.append(DieRoller())

    for i in range(len(prisoners)):
        for j in range(i+1,len(prisoners)):
            theDilemma.play(prisoners[i],prisoners[j],GAMES_PER_MATCH)

    print("\n****RESULTS****")
    for prisoner in sorted(prisoners,reverse=True):
        print(prisoner)

class Prisoner:
    
    def __init__(self):
        self.points = 0
        

    def update(self,betrayed,newPoints):
        self.betrayed = betrayed
        self.newPoints = newPoints
        self.points += self.newPoints
        
    def matchReset(self):
        pass

    def getName(self):
        return self.name

    def getPoints(self):
        return self.points

    def __lt__(self,other):
        return self.points < other.points

    def __ge__(self,other):
        return self.points >= other.points

    def __str__(self):
        return f"{self.name}: {self.points} points."
        

class Cooperator(Prisoner):
    nextId = 0
    
    def __init__(self):
        super().__init__()
        Cooperator.nextId += 1
        self.name = "Cooperator " + str(Cooperator.nextId)
        
        

    def play(self):
        return False

class Defector(Prisoner):
    nextId = 0

    def __init__(self):
        super().__init__()
        Defector.nextId += 1
        self.name = "Defector " + str(Defector.nextId)

    def play(self):
        return True
        

class TitForTat(Prisoner):
    nextId = 0
    
    def __init__(self):
        super().__init__()
        TitForTat.nextId += 1
        self.name = "TitForTat " + str(TitForTat.nextId)
        self.betrayedCounter = 0

    def play(self):
        if self.betrayedCounter == 1:
            self.betrayedCounter = 0
            return True
        else:
            return False
            
            

    def matchReset(self):
        self.betrayedCounter = 0
        return False
    

    def update(self,betrayed,newPoints):
        super().update(betrayed,newPoints)
        if self.betrayed == True:
            self.betrayedCounter += 1
        
        
        

class GrimTrigger(Prisoner):
    nextId = 0
    
    def __init__(self):
        super().__init__()
        GrimTrigger.nextId += 1
        self.name = "GrimTrigger " + str(GrimTrigger.nextId)
        self.betrayedCounter = 0

    def play(self):
        if self.betrayedCounter == 0:
            return False
        else:
            return True

    def matchReset(self):
        self.betrayedCounter = 0
        return False

    def update(self,betrayed,newPoints):
        super().update(betrayed,newPoints)
        if self.betrayed == True:
            self.betrayedCounter += 1
        
            
            
        

class CoinFlipper(Prisoner):
    nextId = 0
    
    def __init__(self):
        super().__init__()
        CoinFlipper.nextId += 1
        self.name = "CoinFlipper " + str(CoinFlipper.nextId)

    def play(self):
        return random.random() < 0.5
        

class DieRoller(Prisoner):
    nextId = 0
    
    def __init__(self):
        super().__init__()
        DieRoller.nextId += 1
        self.name = "DieRoller " + str(DieRoller.nextId)

    def play(self):
        return random.random() < 1/6
        

class Dilemma:

    def __init__(self,bothCoopOutcome,bothDefectOutcome,betrayerOutcome,betrayedOutcome):
        self.bothCoopOutcome = bothCoopOutcome
        self.bothDefectOutcome = bothDefectOutcome
        self.betrayerOutcome = betrayerOutcome
        self.betrayedOutcome = betrayedOutcome

    def play(self,playerA,playerB,numGames):

        # some Prisoner classes track information from game to game
        # ensure this information is wiped clean at the start of each match
        playerA.matchReset()
        playerB.matchReset()

        # take note of each player's points at the start of each match
        # so that we can calculate how many points were won/lost by both players
        playerAStartingScore = playerA.getPoints()
        playerBStartingScore = playerB.getPoints()

        for i in range(numGames):
        
            playerAChoice = playerA.play()
            playerBChoice = playerB.play()

            # if A defects...
            if playerAChoice:
                # ...and so does B
                if playerBChoice:
                    playerA.update(True,self.bothDefectOutcome)
                    playerB.update(True,self.bothDefectOutcome)
                # ...and player B cooperates
                else:
                    playerA.update(False,self.betrayerOutcome)
                    playerB.update(True,self.betrayedOutcome)
            # if A cooperates...
            else:
                # ...and B defects
                if playerBChoice:
                    playerA.update(True,self.betrayedOutcome)
                    playerB.update(False,self.betrayerOutcome)
                # ...and so does B
                else:
                    playerA.update(False,self.bothCoopOutcome)
                    playerB.update(False,self.bothCoopOutcome)

        # compare the starting scores we noted to the ending scores and print
        # a short description of the outcome
        playerAEndingScore = playerA.getPoints()
        playerBEndingScore = playerB.getPoints()
        changeInPlayerAScore = playerAEndingScore-playerAStartingScore
        changeInPlayerBScore = playerBEndingScore-playerBStartingScore
        print(f"{playerA.getName()} ({changeInPlayerAScore}) vs. {playerB.getName()} ({changeInPlayerBScore})")

if __name__ == "__main__":
    main()
