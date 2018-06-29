#Q1.Write a program to create a tuple with different data types and do the following operations.
#●	Find the length of tuples
t1=(2,"radhika",3.0,"garg")
len(t1)

#Q2. Find largest and smallest elements of a tuples.
t2=(2,4,5,67)
>>> max(t2)
67
>>> min(t2)
2

#Q3.Write a program to find the product of all elements of a tuple.
def product(tuple1):
    prod = 1
    for x in tuple1:
        prod = prod * x
    return prod
print(product(t2))

#####SETS
#Q1.1)	Create  two set using user defined values.
#●	          Calculate difference between two sets.

l3=set(map(int,input().split()))
3 4 5 6 7 8
 l4=set(map(int,input().split()))
 9 12 15 13 3 4

 print(l3-l4)
 {8, 5, 6, 7}
#●	         Compare two sets.
 l3>l4
 False
#●	         Print the result of intersection of two sets.
  l3&l4
{3, 4}






#####DICTONARIES
#Q1	Create a dictionary to store name and marks of 5 students.
d1={"radhika":98,"tushar":99,"aman":78,"abhi":88,"komal":78}
print(d1)

#Q2.	Sort the dictionary created in previous question according to marks.
import operator
d1={"radhika":98,"tushar":99,"aman":78,"abhi":88,"komal":78}
sorted_x = sorted(d1.items(), key=operator.itemgetter(1))


#Q3.3)	Count the number of occurrence of each letter in word "MISSISSIPPI". Store count of every letter with the letter in a dictionary.
var="MISSISSIPPI"
d2={}
for i in var:
    if i in d2.keys():
        d2[i]+=1
    else:
        d2[i]=1
print(d2)

