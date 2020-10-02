#  Write a Python program to select the odd items of a list

list1=list(input("enter list elements seperated with comma\n").split(","))
print("given list",list1)
list_out=[x for x in list1 if int(x)%2 !=0]
print("odd items from list",list_out)
