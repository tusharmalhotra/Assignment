#Q1.
class Animal:
    def animal_attribute(self):
        print("In class Animal")

class Elephant(Animal):
    def __init__(self):
        print("In classElephant")
        self.animal_attribute()
        print("Again in class Elephant")

ob1 = Elephant()




#Q2.
Output :
A B
A B


#Q4.
class Shape:
    def __init__(self,l,b):
        self.l = l
        self.b = b
    def area(self):
        return self.l*self.b

class Rectangle(Shape):
    def area(self):
        print("\n
              Area of Rectangle : ",super().area())
        
class Square(Shape):
    def area(self):
        print("Area of Square : ",super().area())

ob4 = Rectangle(40,60)
ob4.area()
ob5 = Square(20,20)
ob5.area()
