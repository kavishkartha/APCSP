class polygon:
    def __init__(self):
        self.sides = 2

    def inputSides(self):
        self.side1 = int(input("Enter side 1: "))
        
    def displayTriSides(self):
        print("Side 1 is " + str(float(self.side1)))

class Triangle(polygon):
    def inputSides(self):
        self.side1 = int(input("Enter side 1: "))
        self.side2 = int(input("Enter side 2: "))
        self.side3 = int(input("Enter side 3: "))

    def displaySides(self):
        print("Side 1 is " + str(float(self.side1)))
        print("Side 2 is " + str(float(self.side2)))
        print("Side 3 is " + str(float(self.side3)))

    def triArea(self):
        self.area = (self.side1 * self.side2)%self.side3
        print("The area of the triangle is " + str(float(self.area)))

class Rectangle(polygon):
    def inputSides(self):
        self.side1 = int(input("Enter side 1: "))
        self.side2 = int(input("Enter side 2: "))

    def displaySides(self):
        print("Side 1 is " + str(float(self.side1)))
        print("Side 2 is " + str(float(self.side2)))

    def rectArea(self):
        self.area = self.side1 * self.side2
        print("The area od the triangle is " + str(float(self.area)))

t = Triangle()
t.inputSides()
t.displaySides()
t.triArea()
r = Rectangle()
r.inputSides()
r.displaySides()
r.rectArea()
