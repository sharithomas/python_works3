# Write a Python program to find the index of an item in a specified list.

size=int(input("size of the list1"))
print("enter elements of list1")
list1=[]
for i in range(size):
    list1.append(input())
print("given list",list1)
item=input("item:")
print("index of item",list1.index(item))
