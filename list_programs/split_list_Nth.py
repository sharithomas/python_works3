# Write a Python program to split a list every Nth element

list1=list(input("enter list elements seperated with comma\n").split(","))
print("given list",list1)
n=int(input("enter value of n"))
list2=[]
for i in range(0,len(list1),n):
    list2.append(list1[i:i+n])
print("resultant list",list2)
