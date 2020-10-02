#1 Write a Python program to check whether an element exists within a tuple.

tuple1=1,2,3,'a','e','i',5,8,9
element=input("enter element to check")
if element in tuple1:
    print("{} exist in ".format(element),tuple1)
else:
    print("{} not exist in ".format(element),tuple1)
