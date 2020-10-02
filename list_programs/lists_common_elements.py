# Write a Python function that takes two lists and returns True if they have at least one common member
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
