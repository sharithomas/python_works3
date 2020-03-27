# -*- coding: utf-8 -*-
"""
Created on Sun Mar 22 13:30:47 2020

@author: SHARI
"""

#######################################
#List Programs
#######################################
#1.Write a Python program to extract a given number of randomly selected elements from a given list.
import random
size=int(input("size of the list"))
print("enter elements of list")
list1=[]
for i in range(size):
    list1.append(input())
print("given list",list1)
n=int(input("size of subset"))
print(random.sample(list1,n))

#2. Write a Python program to insert an element at a specified position into a given list
size=int(input("size of the list"))
print("enter elements of list")
list1=[]
for i in range(size):
    list1.append(input())
print("given list",list1)
print("enter inserting item and position")
item=input()
index=int(input())
list1.insert(index-1,item)
print("list after inserting new element",list1)

#3. Write a Python program to remove the K'th element from a given list, print the new list
size=int(input("size of the list"))
print("enter elements of list")
list1=[]
for i in range(size):
    list1.append(input())
print("given list",list1)
index=int(input("enter position from which element to be deleted"))
del list1[index-1]
print("list after inserting new element",list1)

#4.Write a Python program to split a given list into two parts where the length of the first part of the list is given.
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

#5. Write a Python program to decode a run-length encoded given list.eg:Original encoded list:[[2, 1], 2, 3, [2, 4], 5, 1]
#Decode a run-length encoded said list: [1, 1, 2, 3, 4, 4, 5, 1]
list1=[[2, 1], 2, 3, [2, 4], 5, 1]
list2=[]
for i in range(len(list1)):
    if type(list1[i])==list:
        print("list")
        count=0
        while count<list1[i][0]:
            list2.append(list1[i][1])
            count=count+1
    else:
        list2.append(list1[i])
print("decoded list",list2)
            
##6.Write a Python program to count the number of strings where the string length is 2 or more and the first and last character 
#are same from a given list of strings
list1=['abc', 'xyz', 'aba', '1221','shhs','2442']
count=0
for i in range(len(list1)):
    if len(list1[i])>=2:
        length=len(list1[i])
        if list1[i][0]==list1[i][length-1]:
            count=count+1
        else:
            pass
print("number of strings with length is 2 or more and first and last are equal :",count)
            
     

#7. Write a Python program to get a list, sorted in increasing order by the last element in each tuple from a given list 
#of non-empty tuples
list1=[(2, 5), (1, 2), (4, 4), (2, 3), (2, 1)]
list2=[]
list_out=[]
dict1={}
for i in list1:
    list2.append(i[1])
    dict1[i[1]]=i[0]
list2.sort()
for i in list2:
        list_out.append((dict1[i],i))
        
#8.Write a Python program to remove duplicates from a list.
size=int(input("size of the list"))
print("enter elements of list")
list1=[]
for i in range(size):
    list1.append(input())
print("given list",list1)
list2=[]
for i in list1:
    if i not in list2:
        list2.append(i)
print("list after removing duplicate values",list2)

#9. Write a Python program to check a list is empty or not.
l=[]
if not l:
    print("list emmpty")

#10.Write a Python program to find the list of words that are longer than n from a given list of words
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

#11. Write a Python function that takes two lists and returns True if they have at least one common member

#function returns 1 if at least one lement common in list1 and list2 else return 0
def lists_intersection(list1,list2):
    flag=0
    if len(list1)>len(list2):
       for i in list1:
           if i in list2:
               flag=1
               break
           else:
               pass
    else:
        for i in list2:
           if i in list1:
               flag=1
               break
           else:
               pass
    return flag
    
size=int(input("size of the list1"))
print("enter elements of list1")
list1=[]
list2=[]
for i in range(size):
    list1.append(input())
print("given list",list1)
size=int(input("size of the list2"))
print("enter elements of lis2")
for i in range(size):
    list2.append(input())
print("given list",list2)
flag=lists_intersection(list1,list2)
if flag==1:
    print("True")
else:
    print("False")
    
# 12. Write a Python program to print a specified list after removing the 0th, 4th and 5th elements.
size=int(input("size of the list with greater than 6: "))
print("enter elements of list1")
list1=[]
for i in range(size):
    list1.append(input())
print("given list",list1)
del list1[5]
list1.pop(4)
del list1[0]
print("list after removing 0th,4th and 5th elemnets",list1)

#13. Write a Python program to shuffle and print a specified list
import random
size=int(input("size of the list : "))
print("enter elements of list1")
list1=[]
for i in range(size):
    list1.append(input())
print("given list",list1)
random.shuffle(list1)
print("after shuffle the list",list1)

#14. Write a Python program to get the difference between the two lists
size=int(input("size of the list1"))
print("enter elements of list1")
list1=[]
list2=[]]
for i in range(size):
    list1.append(input())
print("given list",list1)
size=int(input("size of the list2"))
print("enter elements of lis2")
for i in range(size):
    list2.append(input())
print("given list",list2)
list3=list(set(list1)-set(list2))
print("diffrence of 2 lists")

#15.Write a Python program access the index of a list.
size=int(input("size of the list1"))
print("enter elements of list1")
list1=[]
for i in range(size):
    list1.append(input())
print("given list",list1)
for index,value in enumerate(list1):
    print(index,value)
    
#16. Write a Python program to convert a list of characters into a string
size=int(input("size of the list1"))
print("enter elements of list1")
list1=[]
for i in range(size):
    list1.append(input())
print("given list",list1)
string=''.join(list1)
print("converted list",string)

#17.Write a Python program to find the index of an item in a specified list.
size=int(input("size of the list1"))
print("enter elements of list1")
list1=[]
for i in range(size):
    list1.append(input())
print("given list",list1)
item=input("item:")
print("index of item",list1.index(item))

#18. Write a Python program to flatten a shallow list
list1=[[1,2,3],5,6,[8,9]]
list2=[]
print("given list",list1)
for i in range(0,len(list1)):
    if type(list1[i])==list:
        count=0
        while count<len(list1[i]):
            list2.append(list1[i][count])
            count=count+1
    else:
        list2.append(list1[i])
print("flatten list",list2)

#19.Write a Python program to select an item randomly from a list
import random
size=int(input("size of the list1"))
print("enter elements of list1")
list1=[]
for i in range(size):
    list1.append(input())
print("given list",list1)
print("random item of list",random.sample(list1,k=1))

#20. Write a Python program to get unique values from a list
size=int(input("size of the list1"))
print("enter elements of list1")
list1=[]
for i in range(size):
    list1.append(input())
print("given list",list1)
#convert list to set and again convert back to list to remove duplicate values
list2=list(set(list1))
print("list with unique values",list2)


#21.Write a Python program to count the number of elements in a list within a specified range.
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

# 22. Write a Python program to check whether a list contains a sublist
list1=list(input("enter list1 seperated with comma").split(","))
sublist=list(input("enter sublist seperated with comma").split(","))
for i in sublist:
    flag=0
    if i in list1:
        flag=1
    else:
        flag=0
        break
if flag==1:
    print("{} contains sublist {}".format(list1,sublist))
else:
    print("{} not contains sublist {}".format(list1,sublist))
    
 #23.. Write a Python program to generate all sublists of a list   
from itertools import combinations
def sub_list(list1):
    subl=[]
    for i in range(0,len(list1)+1):
        temp=[list(x) for x in combinations(list1,i)]
        if len(temp)>0:
            subl.extend(temp)
    return subl

list1=list(input("enter list elements seperated with comma").split(","))
sublist=sub_list(list1)
print("sublists of given list",sublist)
        
#24.Write a Python program to find common items from two lists
list1=list(input("enter list1 elements seperated with comma").split(","))
list2=list(input("enter list2 elements seperated with comma").split(","))
set1=set(list1)
set2=set(list2)
common_set=set1&set2
common_list=list(common_set)
print("common items from 2 lists",common_list)

#25.Write a Python program to change the position of every n-th value with the (n+1)th in a list.
list1=list(input("enter list1 elements seperated with comma").split(","))
for i in range(0,len(list1),2):
    temp=list1[i]
    list1[i]=list1[i+1]
print("list after changing positions",list1)
    
#26. Write a Python program to convert a list of multiple integers into a single integer.
list1=list(input("enter list elements seperated with comma").split(","))
print("given list",list1)
print("single integer after combining all integers from given list")
for i in list1:
    print(i,end="")
    
#27.Write a Python program to split a list based on first character of word
from itertools import groupby
from operator import itemgetter
list1=list(input("enter list elements seperated with comma").split(","))
print("given list",list1)
for letter,words in groupby(sorted(list1),itemgetter(0)): # groupby()-This method calculates the keys for each element present in iterable.
                                                            #It returns key and iterable of grouped items.
    print(letter)                                   #itemgetter(0) returns 0th index charcter from each word and based on it return group
    for word in words:
        print(word)

#28.Write a Python program to find missing and additional values in two lists
list1=list(input("enter list1 elements seperated with comma").split(","))
list2=list(input("enter list2 elements seperated with comma").split(","))
print("missing values in 2nd list",set(list1)-set(list2))
print("additional  values in list2",set(list2)-set(list1))

#29.. Write a Python program to generate groups of five consecutive numbers in a list
list1=[[5*j+i for i in range(1,6)] for j in range(0,6)]
print(list1)

#30. Write a Python program to generate groups of five consecutive numbers in a list
list1= [(1, 2), (3, 4), (1, 2), (5, 6), (7, 8), (1, 2), (3, 4), (3, 4),
 (7, 8), (9, 10)]
print("orginal list",list1)
list2=[]
for i in list1:
    list2.append(i[0])
    list2.append(i[1])
set2=set(list2)
print("sorted unique data",sorted(list(set2)))   
#print("sorted unique data",sorted(set().union(*list1))) # another choice 

#31.Write a Python program to select the odd items of a list
list1=list(input("enter list elements seperated with comma\n").split(","))
print("given list",list1)
list_out=[x for x in list1 if int(x)%2 !=0]
print("odd items from list",list_out)

#32.Write a Python program to insert an element before each element of a list
list1=list(input("enter list elements seperated with comma\n").split(","))
print("given list",list1)
list2=[]
element=input("enter element to insert before each elemnet")
for i in range(0,len(list1)):
    temp=list1[i]
    list2.append(element)
    list2.append(temp)
print("list after inserting elements",list2)
    
#33.Write a Python program to split a list every Nth element
list1=list(input("enter list elements seperated with comma\n").split(","))
print("given list",list1)
n=int(input("enter value of n"))
list2=[]
for i in range(0,len(list1),n):
    list2.append(list1[i:i+n])
print("resultant list",list2)

##########################################################
#programs on packing and unpacking list
####################################################

my_list = [1, 2, 3, 4] 
def func(a,b,c,d):
    print(a,b,c,d)
#unpacking list into 4 arguments
func(*my_list)

#packing
#function uses packing to sum
def sum_values(*values):
    Sum=0
    for i in range(0,len(values)):
        Sum=Sum+values[i]
    return Sum
# Driver code 
print(sum_values(1, 2, 3, 4, 5)) 
print(sum_values(10, 20))

## A sample program to demonstrate unpacking of 
# dictionary items using **
def function_dict(a,b,c,d):
    print(a,b,c,d)
    
dictionary={'a':10,'b':20,'c':30,'d':40}
function_dict(*dictionary) # a b c d
function_dict(**dictionary) # 10 20 30 40
