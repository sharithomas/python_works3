# Write a Python program to remove duplicates from a list.

size=int(input("size of the list"))
print("enter elements of list")
list1=[]
for i in range(size):
    list1.append(input())
print("given list",list1)
list2=[]
for i in list1:
    if i not in list2:
        list2.append(i)
print("list after removing duplicate values",list2)
