# Write a Python program to insert an element before each element of a list

list1=list(input("enter list elements seperated with comma\n").split(","))
print("given list",list1)
list2=[]
element=input("enter element to insert before each elemnet")
for i in range(0,len(list1)):
    temp=list1[i]
    list2.append(element)
    list2.append(temp)
print("list after inserting elements",list2)
