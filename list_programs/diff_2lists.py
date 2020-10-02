# Write a Python program to get the difference between the two lists

size=int(input("size of the list1"))
print("enter elements of list1")
list1=[]
list2=[]]
for i in range(size):
    list1.append(input())
print("given list",list1)
size=int(input("size of the list2"))
print("enter elements of lis2")
for i in range(size):
    list2.append(input())
print("given list",list2)
list3=list(set(list1)-set(list2))
print("diffrence of 2 lists")
