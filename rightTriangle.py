sideList = []
small = 0
mid = 0
large = 0

sideOne = int(input("Enter length of side one: "))
sideTwo = int(input("Enter length of side two: "))
sideThree = int(input("Enter length of side three: "))

sideList.append(sideOne)
sideList.append(sideTwo)
sideList.append(sideThree)


sideList.sort()

if (sideList[0] * sideList[0]) + (sideList[1] * \
   sideList[1]) == (sideList[2] * sideList[2]):
    print("The triangle is a right triangle.")
else:
    print("The triangle is not a right triangle.")
