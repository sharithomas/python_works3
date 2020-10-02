#   Write a Python program to check whether a list contains a sublist

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
