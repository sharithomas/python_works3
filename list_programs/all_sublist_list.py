 #  Write a Python program to generate all sublists of a list   
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
