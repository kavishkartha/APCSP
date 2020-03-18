class calculator:
    operand1 = 0
    operand2 = 0
    operator = ""

    def __init__(self):
        self.operand1 = 10
        self.operand2 = 2

    def setOperator(self, operator):
        self.operator = operator

    def calculate(self):
        if self.operator == "addition":
            result = self.operand1 + self.operand2
            return result
        elif self.operator == "subtraction":
            result = self.operand1 - self.operand2
            return result
        elif self.operator == "multiplication":
            result = self.operand1 * self.operand2
            return result
        elif self.operator == "division":
            result = self.operand1//self.operand2

a = calculator()
s = calculator()
m = calculator()
d = calculator()
e = calculator()

a.setOperator("addition")
print("The result of the addition operaation is " + str(a.calculate()))

s.setOperator("subtraction")
print("The result of the ssubtraction operation is " + str(s.calculate()))

m.setOperator("multiplication")
print("The result of the multiplication operation is " + str(m.calculate()))

d.setOperator("division")
print("The result of the division operation is " + str(d.calculate()))

e.setOperator("error")
print(e.calculate())
