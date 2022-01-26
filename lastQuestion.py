class Horse:
    def talk(self):
        return "Neigh!"

    def trot(self):
        return "Clip-clop, clip-clop!"

    def sleep(self):
        return "zzz"

class TalkingHorse(Horse):
    def talk(self):
        return "Hello!"

    def trot(self):
        super().trot(Horse)
        return "Tally ho!"
    

    def sleep(self):
        super().sleep(Horse)
        
    
        
