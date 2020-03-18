firstNum == float(input("Enter the first number: "))
secondNum = float(input("Enter the second number: "))
operation = input("Enter an operation (addition, multiplication, divison, or subtraction): ")

def calculator(x, y, op = "addition"):
    if op == "addition":
        answer = x + y
        print(round(answer))
    elif op == "multiplication":
        answer = x * y
        print(round(answer))
    elif op == "division":
        answer = x % y
        print(round(answer))
    elif op == "subtraction":
        answer = x - y
        print(round(answer))
    else:
        print("ERROR")
        
calculator(firstNum, secondNum, operation)
