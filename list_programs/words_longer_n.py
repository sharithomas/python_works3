# Write a Python program to find the list of words that are longer than n from a given list of words

size=int(input("size of the list"))
print("enter elements of list")
list1=[]
list2=[]
for i in range(size):
    list1.append(input())
print("given list",list1)
n=int(input("size of word"))
for i in list1:
    if len(i)>n:
        list2.append(i)
print("elemnets with more than {} words ".format(n),list2)
