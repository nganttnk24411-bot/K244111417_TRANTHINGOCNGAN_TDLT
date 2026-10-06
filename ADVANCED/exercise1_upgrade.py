print ("Please tell me the drink you want ordered.")

while True:
    try:
        noA = int(input("number of Americano (cups): "))
        if noA >= 0:
            break
        else:
            print ("Please enter a possitive integer")
    except ValueError:
        print("Please enter a number.")

while True:
    try:
        noL = int(input("Number of cafe late (cups): "))
        if noL >= 0:
            break
        else:
            print ("Please enter a possitive integer")
    except ValueError:
        print ("Please enter a number.")

while True:
    try:
        noC = int(input("Number of cappucinos (cups): "))
        if noC >= 0:
            break
        else:
            print ("Please enter a possitive integer")
    except ValueError:
        print ("Please enter a number.")

sum = 0
sum += noA * 2500
sum += noL * 3500
sum += noC * 3000

print ("The total amount is: ", sum, " money")

while True:
    try:
        money = int(input("enter the amount to be paid: "))
        if money>=0:
            break
        else:
            print("Please enter a positive integer")
    except ValueError:
        print ("Please enter an integer")

if money < sum:
    print ("Not enough money to buy bạn ơi")
else:
    print ("Chang is ", money-sum," money")