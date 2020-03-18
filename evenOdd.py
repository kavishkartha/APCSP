i = 5
while True:
    userInput = int(input("Enter an integer: "))
    if userInput == 13:
        break
    else:
        if userInput % 2 != 0:
            print(str(userInput) + " is odd.")
        if userInput % 2 == 0:
            print(str(userInput) + " is even.")
