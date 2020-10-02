# Write a Python program to change the position of every n-th value with the (n+1)th in a list.

list1=list(input("enter list1 elements seperated with comma").split(","))
for i in range(0,len(list1),2):
    temp=list1[i]
    list1[i]=list1[i+1]
print("list after changing positions",list1)
