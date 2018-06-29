#Q1.1)	Name and handle the exception occured in the following program:
#a=3
 #if a<4:
    #b=a/(a-3)
  #   print(b)
try:
    a=3
 if a<4:
    b=a/(a-3)
     print(b)

except ZeroDivisionError:
    print("divided by zero")


#Q2.Name and handle the exception occurred in the following program:
                        #   l=[1,2,3]
                         #  print(l[3])
try:
     l=[1,2,3]
    print(l[3])
except IndexError:
    print("index out of bound")
    
#Q3.

An exception

#Q4.
AbyB(2.0, 3.0)
-5.0
>>> AbyB(3.0, 3.0)
a/b result in 0

#Q5.Value error
try:
        n = input("Please enter an integer: ")
        n = int(n)

except ValueError:
        print("No valid integer! Please try again ...")

        
Please enter an integer: a
No valid integer! Please try again ...

#Indexerror

try:
     l=[1,2,3]
    print(l[3])
except IndexError:
    print("index out of bound")

#import error

 try:
        lib = __import__(name)
except ImportError:
        print ("cvsfv")
