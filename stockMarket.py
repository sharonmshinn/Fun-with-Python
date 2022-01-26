import random

NUMBER_OF_DAYS = 10
STARTING_CASH = 100
NUMBER_OF_STOCK_SYMBOLS = 5
MINIMUM_DIE_FACE = 1
MAXIMUM_DIE_FACE = 12

def main():
    while True:
        initializeGame()

        mainGameLoop()
        
        playAgain = input("Do you want to play again, Y/N: ")
        if playAgain.upper() != "Y":
            break

def mainGameLoop():
    day = 0
    while day < NUMBER_OF_DAYS:

        dailyDisplay(day)
        determineDailyPrices()

        print("Buy? Sell? Or Press enter for skip to next day.")
        print("Example: BUY 15 FOO")
        print("Example: SELL 10 BAR")
        print("Example: NEXT")
        userInput = input(">> ")
        inputTokens = userInput.split(" ")
        command = inputTokens[0].upper()
        if command == "BUY":
            buyQuantity = int(inputToken[1])
            symbolToBuy = inputToken[2].upper()
            symbolIndex = stockSymbols.index(symbolToBuy)
            currentPrice = sharePrices[symbolIndex]
            totalPrice = buyQuantity * currentPrice
            if totalPrice <- moneyOnHand:
                moneyOnHand -= totalPrice
                sharesOwned[symbolIndex] =+ buyQuantity
            else:
                print("Not enough cash!")
            
        elif command == "SELL":
            pass
        elif command == "NEXT":
            determineDailyPrices()
            day += 1
        else:
            print(f"\"{command}\" is not a valid command.")

def determineDailyPrices():
    for i in range(len(sharePrices)):
        sharePrices[i] = sharePriceFunctions[i]()

              
def dailyDisplay(day):
    print("**************************")
    print(f"Day {day+1}/{NUMBER_OF_DAYS}")
    for i in range(len(stockSymbols)):
        print(f"{stockSymbols[i]}:\t${sharePrices[i]}")
    print(f"Cash on hand: ${moneyOnHand}")
    print("**************************")    

def initializeGame():
    global stockSymbols
    stockSymbols = generateStockSymbols()
    global moneyOnHand
    moneyOnHand = STARTING_CASH
    global sharesOwned
    sharesOwned = [0] * NUMBER_OF_STOCK_SYMBOLS
    global sharePrices
    sharePrices = [0] * NUMBER_OF_STOCK_SYMBOLS
    global sharePriceFunctions
    sharePriceFunctions = []
    for i in range(NUMBER_OF_STOCK_SYMBOLS):
        sharePriceFunctions.append(initializeStockDistribution())

def generateStockSymbols():
    stockSymbols = []
    while len(stockSymbols) < NUMBER_OF_STOCK_SYMBOLS:
        newStockSymbol = generateStockSymbol()
        if newStockSymbol not in stockSymbols:
            stockSymbols.append(newStockSymbol)
    return stockSymbols

def generateStockSymbol():
    lengthOfSymbol = random.randint(3,4)
    symbol = ""
    for i in range(lengthOfSymbol):
        symbol += chr(random.randint(ord("A"),ord("Z")))
    return symbol
    
def initializeStockDistribution():
    return lambda: random.randint(MINIMUM_DIE_FACE,random.randint(MINIMUM_DIE_FACE,MAXIMUM_DIE_FACE)) + \
            random.randint(MINIMUM_DIE_FACE,random.randint(MINIMUM_DIE_FACE,MAXIMUM_DIE_FACE))



if __name__ == "__main__":
    main()
