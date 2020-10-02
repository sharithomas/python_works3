#  Write a Python program to convert a list of multiple integers into a single integer.

list1=list(input("enter list elements seperated with comma").split(","))
print("given list",list1)
print("single integer after combining all integers from given list")
for i in list1:
    print(i,end="")
