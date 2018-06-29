l5=list(map(int,input().split()))
2 3 5 6 7
>>> list1=['google','apple','facebook','microsoft','tesla']
>>> l5+list1
[2, 3, 5, 6, 7, 'google', 'apple', 'facebook', 'microsoft', 'tesla']
>>> l5.count(2)
1
>>> list1.count(a)
Traceback (most recent call last):
  File "<pyshell#59>", line 1, in <module>
    list1.count(a)
NameError: name 'a' is not defined
>>> list2=[78,12,45,67,34,78]
>>> list2.sort()
>>> list2
[12, 34, 45, 67, 78, 78]
>>> list3=(l5+list2).sort()
>>> list
<class 'list'>
>>> list3
>>> print(list3)
None
>>> l5
[2, 3, 5, 6, 7]
>>> l3=l5+list3
Traceback (most recent call last):
  File "<pyshell#68>", line 1, in <module>
    l3=l5+list3
TypeError: can only concatenate list (not "NoneType") to list
>>> l3=l5+list2
>>> l3
[2, 3, 5, 6, 7, 12, 34, 45, 67, 78, 78]
>>> l3.sort()
>>> l3
[2, 3, 5, 6, 7, 12, 34, 45, 67, 78, 78]
>>> 