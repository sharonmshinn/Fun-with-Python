def main():
    ourRational = Rational(3,4)
    print(ourRational.getNumerator())
    print(ourRational.getDenominator())

class Rational:

    def __init__(self,num,denom):
        self.num = num
        self.denom = denom

    def getNumerator(self):
        return self.num

    def getDenominator(self):
        return self.denom
    
    def __str__(self):
        return(f"{self.num}/{self.denom}"


    def __lt__(self,other):
        extremes = self.num * other.denom
        means = self.denom * other.num
        return extremes < means

    def __ge__(self,other)
        extremes = self.num * other.denom
        means = self.denom * other.num
        return extremes >= means

    if __name__ == "__main__":
        main()
