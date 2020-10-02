# Write a Python program to find missing and additional values in two lists

list1=list(input("enter list1 elements seperated with comma").split(","))
list2=list(input("enter list2 elements seperated with comma").split(","))
print("missing values in 2nd list",set(list1)-set(list2))
print("additional  values in list2",set(list2)-set(list1))
