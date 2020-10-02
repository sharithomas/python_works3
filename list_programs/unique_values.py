# Write a Python program to get unique values from a list

size=int(input("size of the list1"))
print("enter elements of list1")
list1=[]
for i in range(size):
    list1.append(input())
print("given list",list1)
#convert list to set and again convert back to list to remove duplicate values
list2=list(set(list1))
print("list with unique values",list2)
