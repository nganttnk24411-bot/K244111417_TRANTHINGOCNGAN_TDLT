import random #Import random module
import time#Import time-related modules

correctAns=0 #Right count, tính số câu đúng
wrongAns=0#Wrong count, tính số câu sai

while True: #dùng vòng lặp để ktra đk về dữ liệu của count
    try:
        count = int(input("How many times should I do?"))
        if count > 0:
            break
        else:
            print("Please enter an positive integer")
    except ValueError:
        print("Please enter an integer")

while count!=0:
    #Generate numbers from 3rd to 9th
    a=random.randint(3,9)
    b=random.randint(3,9)
    #If it is 5th stage, random number is generated again
    if a==5 or b==5: #do đề kêu bỏ 2 và 5
        continue

    count=count-1
    print(a," x ",b)

    # calc time= end - start
    startTime=time.time() #Measure reaction time
    product=int(input())
    endTime=time.time()

    print("I answered in seconds %1.f "%(endTime-startTime))

    # Check if the multiplication is correct
    if product==a*b:
        correctAns=correctAns+1
        print("Right!\n")
    else:
        wrongAns=wrongAns+1
        print("Try again!\n")

print("total respone ", correctAns + wrongAns, " correct  ", correctAns, " times")