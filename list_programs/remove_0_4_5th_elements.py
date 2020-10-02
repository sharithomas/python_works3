#  Write a Python program to print a specified list after removing the 0th, 4th and 5th elements.

size=int(input("size of the list with greater than 6: "))
print("enter elements of list1")
list1=[]
for i in range(size):
    list1.append(input())
print("given list",list1)
del list1[5]
list1.pop(4)
del list1[0]
print("list after removing 0th,4th and 5th elemnets",list1)
