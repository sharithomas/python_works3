# Write a Python program to find the repeated items of a tuple.

tuple1=(1,3,1,4,5,6,2,7,6,5,8,9)
rep_list=[]
for i in tuple1:
    if tuple1.count(i)>1 and i not in rep_list:
        rep_list.append(i)
print("repeated items are",rep_list)
