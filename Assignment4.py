#Q1.Take an input year from user and decide whether it is a leap year or not.
year=int(input("enter the year:"))
if (year % 4) == 0:
   if (year % 100) == 0:
       if (year % 400) == 0:
           print("{0} is a leap year".format(year))
       else:
           print("{0} is not a leap year".format(year))
   else:
       print("{0} is a leap year".format(year))
else:
   print("{0} is not a leap year".format(year))

#Q2Take length and breadth input from user and check whether the dimensions are of square or rectangle.
length=int(input("enter the length:"))
breadth=int(input("enter the breadth:"))
if length==breadth:
    print("the dimensions are of square")
else:
    print("the dimensions are of rectangle")

#Q3.Take the input age of 3 people and determine oldest and youngest among them.
    
first = int(input( "Enter first age"))

second = int(input( "Enter second age"))

third = int(input("third age"))

if first >= second and first >= third:
  print "Oldest is",first
elif second >= first and second >= third:
  print "Oldest is",second
elif third >= first and third >= second:
  print "Oldest is",third
else:
  print "All are equal"
  
  if first < second and first < third:
  print "Youngest is",first
elif second < first and second < third:
  print "Youngestt is",second
elif third < first and third< second:
  print "Youngest is",third
else:
  print "All are equal"


 # Q4.
 def which_prize(points):
    if  points <= 50:
        return "No prize"
    elif points <=150 :
        return "Congratulations! You have won a wooden box!"
    elif points <=180 :
        return "Congratulations! You have won a book!"
    else :
        return "Congratulations! You have won chocolates!"


#Q5.)  A shop will give discount of 10% if the cost of purchased quantity is more than 1000.Ask user for quantity. Assume one unit will cost 100.
##Judge and print total cost for user.
 
q= int(input("Enter quantity"))
if q*100 > 1000:
  print "Cost is",((q*100)-(.1*q*100))
else:
  print "Cost is",q*100
    
