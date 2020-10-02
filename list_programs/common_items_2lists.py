# Write a Python program to find common items from two lists

list1=list(input("enter list1 elements seperated with comma").split(","))
list2=list(input("enter list2 elements seperated with comma").split(","))
set1=set(list1)
set2=set(list2)
common_set=set1&set2
common_list=list(common_set)
print("common items from 2 lists",common_list)
