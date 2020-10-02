# Write a Python program to get a list, sorted in increasing order by the last element in each tuple from a given list 
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
