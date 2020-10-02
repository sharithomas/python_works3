# Write a Python program to split a given list into two parts where the length of the first part of the list is given.

size=int(input("size of the list"))
print("enter elements of list")
list1=[]
for i in range(size):
    list1.append(input())
print("given list",list1)
list2=[]
list3=[]
split_size=int(input("enter length of first part of list"))
for i in range(split_size):
    list2.append(list1[i])
for i in range(split_size,size):
    list3.append(list1[i])
list4=list((list2,list3))
print("list after spliting given list into two with given size",list4)
