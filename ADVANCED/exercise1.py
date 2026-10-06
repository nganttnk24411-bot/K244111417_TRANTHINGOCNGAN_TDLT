print ("Please tell me the drink you want ordered.")
noA = int(input("number of Americano (cups): "))
noL = int(input("Number of cafe late (cups): "))
noC = int(input("Number of cappucinos (cups): "))

sum = 0
sum += noA * 2500
sum += noL * 3500
sum += noC * 3000

print ("The total amount is: ", sum, " money")

money = int(input("enter the amount to be paid: "))

if money < sum:
    print ("Not enough money to buy bạn ơi")
else:
    print ("Chang is ", money-sum," money")