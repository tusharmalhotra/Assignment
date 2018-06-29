#Q1.What is Time Tuple?
Many of Pythons time functions handle time as a tuple of 9 numbers, 

Index	Field	Values
0	4-digit year	2008
1	Month	1 to 12
2	Day	1 to 31
3	Hour	0 to 23
4	Minute	0 to 59
5	Second	0 to 61 (60 or 61 are leap-seconds)
6	Day of Week	0 to 6 (0 is Monday)
7	Day of year	1 to 366 (Julian day)
8	Daylight savings	-1, 0, 1, -1 means library determines DST

#Q2.Write a program to get formatted time.
import time
time.strftime("%H :%M:%S")

#Q3.Extract month from the time
import datetime
d = datetime.date.today()
d.month


#Q4.Extract day from the time
import datetime
d = datetime.date.today()
d.day


#Q5.Extract date (ex : 11 in 11/01/2021) from the time.
import datetime
d = datetime.date.today()
d.day

#Q6.6)	Write a program to print time using localtime method.
import time
print(time.localtime())



#Q7.Find the factorial of a number input by user using math package functions

import math
>>> math.factorial(3)

#Q8.1)	** Find the GCD of a number input by user using math package functions.
import math
math.gcd(4,12)

#Q9.9)	Use OS package and do the following tasks:
#●	                  Get current working directory.
#●	                   Get the user environment.
import os

>>> os.getcwd()

