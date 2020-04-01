# -*- coding: utf-8 -*-
"""
Created on Mon Mar 30 23:01:35 2020

@author: SHARI
"""

#Tuples_programs
#1. Write a Python program to create a tuple.

tuple1=tuple(range(0,10))
tuple2=(1,"hai",2,3,4)
tuple3=1,"hai"
print("created tuples are")
print(tuple1)
print(tuple2)
print(tuple3)

#2. Write a Python program to create a tuple with different data types.

tuple1=(1,3.14,False,1+9j,"tuple")
print("craeted tuple")
print(tuple1)

#3.Write a Python program to create a tuple with numbers and print one item.
tuple1=tuple(range(1,5))
print("given tuple")
print(tuple1)
print("one item of tuple1 =",tuple1[1])

#4. Write a Python program to unpack a tuple in several variables
tuple1=1,2,3,4
w,x,y,z =tuple1 #unpacking tuple in variables
print("sum=",w+x+y+z)
print("w=",w)
print("x=",x)
print("y=",y)
print("z=",z)

#5.Write a Python
 program to add an item in a tuple
tuple1=4,2,6,8,9,23
tuple1=tuple1+(34,) #merge tuple with + operator
print(tuple1)
tuple1 = tuple1[:5] + (15, 20, 25) + tuple1[5:] #adding elements at specified locations
print(tuple1)
list1=list(tuple1) #convert tuple to list 
list1.append(100)
tuple1=tuple(list1)
print(tuple1)

#6. Write a Python program to convert a tuple to a string
tuple1='p','y','t','h','o','n'
string1=''.join(tuple1) # convert tuple into string by joining each character of tuple 
print(string1)

#7.Write a Python program to get the 4th element and 4th element from last of a tuple
tuple1=tuple(range(0,10))
print("given tuple is",tuple1)
print("4th element",tuple1[3])
print("4th element from last",tuple1[-4])

#8. Write a Python program to create the colon of a tuple.
from copy import deepcopy
#create a tuple
tuple1 = ("HELLO", 5,[], True) 
print(tuple1)
#make a copy of a tuple using deepcopy() function
tuple1_colon = deepcopy(tuple1)
tuple1_colon[2].append(50)
print(tuple1_colon)
print(tuple1)

#9. Write a Python program to find the repeated items of a tuple.
tuple1=(1,3,1,4,5,6,2,7,6,5,8,9)
rep_list=[]
for i in tuple1:
    if tuple1.count(i)>1 and i not in rep_list:
        rep_list.append(i)
print("repeated items are",rep_list)

#10.Write a Python program to check whether an element exists within a tuple.
tuple1=1,2,3,'a','e','i',5,8,9
element=input("enter element to check")
if element in tuple1:
    print("{} exist in ".format(element),tuple1)
else:
    print("{} not exist in ".format(element),tuple1)
    
#11. Write a Python program to convert a list to a tuple
list1=list(range(0,10))
print("given list",list1)
tuple1=tuple(list1)
print("converted tuple",tuple1)

#12.Write a Python program to convert a tuple to a dictionary.
tuple1=tuple(range(10,20))
print("given tuple",tuple1)
dictionary=dict((tuple1.index(x),x) for x in tuple1 )
print("converted dictionary",dictionary)

#13.Write a Python program to unzip a list of tuples into individual lists
l=[(1,2),(3,4),(5,6)]
print(list(zip(*l)))

#14. Write a Python program to reverse a tuple
tuple1=tuple(range(10,20))
print("given tuple",tuple1)
reverse=reversed(tuple1)
print("reversed tuple is")
print(tuple(reverse))
print(tuple1[::-1])

#15. Write a Python program to replace last value of tuples in a list. 
#Sample list: [(10, 20, 40), (40, 50, 60), (70, 80, 90)]
#Expected Output: [(10, 20, 100), (40, 50, 100), (70, 80, 100)]
tuple1=[(10, 20, 40), (40, 50, 60), (70, 80, 90)]
print("given tuples in a list",tuple1)
tuple_replace=[x[:-1]+(100,) for x in tuple1]
print("after replacing last value of tuple in list")
print(tuple_replace)

#16.Write a Python program to remove an empty tuple(s) from a list of tuples.
list1=[(), (), ('',), ('a', 'b'), ('a', 'b', 'c'), ('d')]
list1=[x for x in list1 if x]
print(list1)

#17.Write a Python program to sort a tuple by its float element
tuple1= [('item1', '12.20'), ('item2', '15.10'), ('item3', '24.5'),('item4','18.6')]
print(sorted(tuple1,key=lambda t:t[-1])[::-1])

#18.Write a Python program to count the elements in a list until an element is a tuple.
tuple1=[23,45,33,49,(2,6,7),67]
count=0
for i in tuple1:
    if isinstance(i,tuple):
        break
    count=count+1
print("number of elements ina list until a tuple is: ",count)