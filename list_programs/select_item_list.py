# Write a Python program to select an item randomly from a list

import random
size=int(input("size of the list1"))
print("enter elements of list1")
list1=[]
for i in range(size):
    list1.append(input())
print("given list",list1)
print("random item of list",random.sample(list1,k=1))
