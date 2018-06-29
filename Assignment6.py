#Q1.Create a function to calculate the area of a circle by taking radius from user.
radius=int(input("enter the radius:"))
def area(radius):
    area1=3.14*radius*radius
    return area1
print(area(radius))


#Q2.Write a function “perfect()” that determines if parameter number is a perfect number. Use this function in a program that determines and prints all the perfect numbers between 1 and 1000.
def isPerfect( n ):
    
    sum = 1
    i = 2
    while i * i <= n:
        if n % i == 0:
            sum = sum + i + n/i
        i += 1
    return (True if sum == n and n!=1 else False)
n=2
for n in range (10000):
    if isPerfect (n):
        print(n , " is a perfect number")

#Q3.Print multiplication table of 12 using recursion
def table(n):
    if n>0:
        table(n-1)
        print("12 x ",n,"=",12*n)
table(10)

#Q4.Write a function to calculate power of a number raised to other 
#( a^b ) using recursion.
def power(base,exp):
    if(exp==1):
        return(base)
    if(exp!=1):
        return(base*power(base,exp-1))
base=int(input("Enter base: "))
exp=int(input("Enter exponential value: "))
print("Result:",power(base,exp))

#Q5.Write a function to find factorial of a number but also store the factorials calculated in a dictionary

def factorial(n):
    if(n <= 1):
        return 1
    else:
        return(n*factorial(n-1))
n = int(input("Enter number:"))
print("Factorial:")
print(factorial(n))

