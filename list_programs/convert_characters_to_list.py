#  Write a Python program to convert a list of characters into a string

size=int(input("size of the list1"))
print("enter elements of list1")
list1=[]
for i in range(size):
    list1.append(input())
print("given list",list1)
string=''.join(list1)
print("converted list",string)
