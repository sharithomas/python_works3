# Write a Python program to extract a given number of randomly selected elements from a given list.

import random
size=int(input("size of the list"))
print("enter elements of list")
list1=[]
for i in range(size):
    list1.append(input())
print("given list",list1)
n=int(input("size of subset"))
print(random.sample(list1,n))
