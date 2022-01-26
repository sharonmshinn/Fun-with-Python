# x number of days
# y differnt stocks
# Player starts with z dollars
# Every day, every stock price is randomized to 2d6
# Every day, player has the option of buying or selling some amount of one stock

import random
#avoid "magic numbers"
TOTAL_DAYS = 10
STARTING_MONEY = 100

fooSharesOwned = 0
barSharesOwned = 0
bazSharesOwned = 0
moneyOnHand = STARTING_MONEY

for day in range(TOTAL_DAYS):
    fooSharePrice = random.randint(1,6)+random.randint(1,6)
    barSharePrice = random.randint(1,6)+random.randint(1,6)
    bazSharePrice = random.randint(1,6)+random.randint(1,6)
    while True:
        print("******Day" + str(day+1) + ":******")
        print("FOO:", str(fooSharePrice), "\t(" + str(fooSharesOwned), ")", sep="")
        print("BAR:" + str(barSharePrice), "\t(" + str(barSharesOwned), ")", sep="")
        print("BAZ:" + str(bazSharePrice),"\t(" + str(bazSharesOwned), ")", sep="" )
        print("Cash on hand: $" + str(moneyOnHand))
        print("\n\n")
        print("1: Buy FOO")
        print("2: Buy BAR")
        print("3: Buy BAZ")
        print("4: Sell FOO")
        print("5: Sell BAR")
        print("6: Sell BAZ")
        print("Enter to end day")
        userSelection = input("> ")
        if userSelection == "":
            break
        elif userSelection == "1":
            print("How many shares of FOO do you want to buy?")
            orderQty = int(input("> "))
            orderTotal = fooSharePrice * orderQty
            if moneyOnHand >= (orderTotal):
                fooSharesOwned += orderQty
                moneyOnHand -= orderTotal
            else:
                print("Not enough cash! ($" + str(orderTotal) + ")")
        elif userSelection == "2":
            print("How many shares of BAR do you want to buy?")
            orderQty = int(input("> "))
            orderTotal = barSharePrice * orderQty
            if moneyOnHand >= (orderTotal):
                barSharesOwned += orderQty
                moneyOnHand -= orderTotal
            else:
                print("Not enough cash! ($" + str(orderTotal) + ")")
        elif userSelection == "3":
            print("How many shares of BAZ do you want to buy?")
            orderQty = int(input("> "))
            orderTotal = bazSharePrice * orderQty
            if moneyOnHand >= (orderTotal):
                bazSharesOwned += orderQty
                moneyOnHand -= orderTotal
            else:
                print("Not enough cash! ($" + str(orderTotal) + ")")
        elif userSelection == "4":
            print("How many shares of FOO do you want to buy?")
            sharesToSell = int(input("> "))
            if sharesToSell <= fooSharesOwned:
                fooSharesOwned -= sharesToSell
                moneyOnHand += (sharesToSell*fooSharePrice)
            else:
                print("Not enough shares to sell!")
        elif userSelection == "5":
            print("How many shares of BAR do you want to buy?")
            sharesToSell = int(input("> "))
            if sharesToSell <= barSharesOwned:
                barSharesOwned -= sharesToSell
                moneyOnHand += (sharesToSell*barSharePrice)
            else:
                print("Not enough shares to sell!")
        elif userSelection == "6":
           print("How many shares of BAZ do you want to buy?")
            sharesToSell = int(input("> "))
            if sharesToSell <= bazSharesOwned:
                bazSharesOwned -= sharesToSell
                moneyOnHand += (sharesToSell*bazSharePrice)
            else:
                print("Not enough shares to sell!")
        else:
            print("Invalid input!")
    
        print("\n\n")
        
fooSharePrice = random.randint(1,6)+random.randint(1,6)
barSharePrice = random.randint(1,6)+random.randint(1,6)
bazSharePrice = random.randint(1,6)+random.randint(1,6)
print("******END OF GAME******")
print("FOO:", str(fooSharePrice), "\t(" + str(fooSharesOwned), ")", sep="")
print("BAR:" + str(barSharePrice), "\t(" + str(barSharesOwned), ")", sep="")
print("BAZ:" + str(bazSharePrice),"\t(" + str(bazSharesOwned), ")", sep="" )
print("Cash on hand: $" + str(moneyOnHand))
print("\n\n")
finalScore = moneyOnHand + (fooSharesOwned * fooSharePrice) + \
             (barSharesOwned * barSharePrice) + \
             (bazSharesOwned * bazSharePrice) - \
             STARTING_MONEY
    
