# Write a Python program to shuffle and print a specified list

import random
size=int(input("size of the list : "))
print("enter elements of list1")
list1=[]
for i in range(size):
    list1.append(input())
print("given list",list1)
random.shuffle(list1)
print("after shuffle the list",list1)
