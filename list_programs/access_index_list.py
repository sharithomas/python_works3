# Write a Python program access the index of a list.

size=int(input("size of the list1"))
print("enter elements of list1")
list1=[]
for i in range(size):
    list1.append(input())
print("given list",list1)
for index,value in enumerate(list1):
    print(index,value)
