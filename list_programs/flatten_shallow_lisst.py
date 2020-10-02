# Write a Python program to flatten a shallow list

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
