# Write a Python program to count the number of elements in a list within a specified range.

size=int(input("size of the list1"))
print("enter elements of list1")
list1=[]
for i in range(size):
    list1.append(input())
print("enter lower and upper range")
low=int(input())
high=int(input())
def count(list1,low,high):
    counter=0
    for i in list1:
        if low<=int(i)<=high:
            counter=counter+1
    return counter
counter=count(list1,low,high)
print("number  of elements between range {} and {} are : {} ".format(low,high,counter))
