# Write a Python program to remove the K'th element from a given list, print the new list

size=int(input("size of the list"))
print("enter elements of list")
list1=[]
for i in range(size):
    list1.append(input())
print("given list",list1)
index=int(input("enter position from which element to be deleted"))
del list1[index-1]
print("list after inserting new element",list1)
