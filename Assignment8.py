#Q1.
class Circle():
  def __init__(self,radius):
    self.radius = radius
  def  getArea(self):
    return 3.14*self.radius*self.radius
  def getCircumference(self):
    return self.radius*2*3.14
obj1=Circle(10)
print(obj1.getArea())
print(obj2.getCircumference())

#Q2.
class Student():
  def __init__(self,name,roll):
    self.name = name
    self.roll= roll
  def display(self):
    print self.name
    print self.roll
obj2=Student("radhika",23)
obj3=Student("tushar",22)
obj2.display()
obj3.display()

#Q3.
class Temprature():
  
  def  convertFahrenhiet(self,celsius):
    return (celsius*(9/5))+32
  def convertCelsius(self,farenhiet):
    return (farenhiet-32)*(5/9)

#Q4.
class MovieDetails:
    def __init__(self,name,a_name,year,rate):
        self.name = name
        self.a_name = a_name
        self.year = year
        self.rate = rate
    def display(self):
        print("\nMovie Name : ",self.name)
        print("Artist Name : ",self.a_name)
        print("Year of release : ",self.year)
        print("Rating : ",self.rate)
    def update(self):
        print("Update Details")
        self.name = input("Update Movie Name : ")
        self.a_name = input("Update Artist Name : ")
        self.year = input("Update year of release : ")
        self.rate = input("Update rating : ")
        
obj4 = MovieDetails("Baaghi2","Tiger","2018","9")
obj4.display()
obj4.update()
obj4.display()

#Q5
class Expenditure:
    def __init__(self,exp1,sav1):
        self.exp1 = exp1
        self.sav1 = sav1
    def display(self):
        print("\nExpenditure : ",self.exp1)
        print("Savings : ",self.sav1)
    def calculateSalary(self):
        return self.sav1 + self.exp1
    def displaySalary(self):
        print("Total Salary : ",self.calculateSalary())

ob7 = Expenditure(400000,250000)
ob7.display()
ob7.displaySalary()
