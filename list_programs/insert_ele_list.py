# Write a Python program to insert an element at a specified position into a given list

size=int(input("size of the list"))
print("enter elements of list")
list1=[]
for i in range(size):
    list1.append(input())
print("given list",list1)
print("enter inserting item and position")
item=input()
index=int(input())
list1.insert(index-1,item)
print("list after inserting new element",list1)
