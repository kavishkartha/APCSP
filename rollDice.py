import random

exampleNum = 14
while True:
    userInput1 = input("Do you want to roll the dice?")
    if userInput1 == "n":
        break;
    elif userInput1 == "no":
        break;
    elif userInput1 == "y":
        userInput2 = input("How many times would you like to roll the dice?")
        intUserInput2 = int(userInput2)
    elif userInput1 == "yes":
        userInput2 = input("How many times would you like to roll the dice?")
        intUserInput2 = int(userInput2)
    else:
        print("yes or y to roll the dice. n or no to exit.")
    randDice = [1, 2, 3, 5, 6]
    if userInput1 == "yes":
        i = 5;
        while True:
            while intUserInput2 > 0:
                intUserInput2 -= 1
                print(random.choice(randDice))
    if userInput1 == "y":
        i = 5;
        while True:
            while intUserInput2 > 0:
                intUserInput2 -= 1
                print(random.choice(randDice))
                





