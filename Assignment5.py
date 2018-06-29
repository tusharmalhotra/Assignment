#q1. 1.	Take 10 integers from user and print it on screen.

L1=[ ]
for i in range(10):
    L1.append(i+1)

print(L1)

#Q2.Write an infinite loop.An infinite loop never ends. Condition is always true.
while True:
    print("infinite loop")

#Q3.Create a list of integer elements by user input. Make a new list which will store square of elements of previous list.
l2=list(map(int,input().split()))
l3=[i*i for i in l2]
print(l2)
print("Square of list elemnts:" , l3)

#Q.4From a list containing ints, strings and floats,print the types of each element.
l=["radhika",4,5.7,'radhika']
[(print(i,type(i)) for i in l)]

#Q5Using range(1,101), make a list containing even and odd numbers.
numbers = []
for i in range(1, 101):
    allElements = int(input("Enter element:"))
    numbers.append(allElements)
 
even_lst = []
odd_lst = []
 
for j in numbers:
    if j % 2 == 0:
        even_lst.append(j)
    else:
        odd_lst.append(j)
 
print("Even numbers list \t", even_lst)
print("Odd numbers list \t", odd_lst)

#Q6.6.	Print the following patterns:
#*
#**
#***
#****

for i range(5):
    for j in range(i):
        print('*',end='  ')
    print(' ')


#Q7.Create a user defined dictionary and get  keys corresponding to  the value using for   loop.

dictionary = {'george' : 16, 'amber' : 19}
search_age = int(input("Provide age"))
for age in dictionary.values():
    if age == search_age:
        name = dictionary[age]
        print name
#Q8.Take inputs from user to make a list. Again take one input from user and search it in the list and delete that element, if found. Iterate over list using for loop
l6=list(map(int,input().split()))
x=int(input("enter the element to be deleted:"))
for i in len(l6):
    if x==l6[i]:
        del l6[i]
        break;
print("after deleting the element:",l6)
