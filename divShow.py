firstNum = int(input("Enter the first number: "))
secondNum = int(input("Enter the second number: "))
if secondNum == 0:
    secondNumIsZero = True
    if secondNumIsZero == True:
        print("The division answer is undefined.")
else:
        answer = firstNum/secondNum
        if answer > 0:
            positive = True
            if positive == True:
                print("The answer is " + str(answer) + " and it is a positive number.")
        if answer < 0:
            negative = True
            if negative == True:
                print("The answer is " + str(answer) + " and it is a negative number.")
