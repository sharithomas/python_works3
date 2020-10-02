#  Write a Python program to decode a run-length encoded given list.eg:Original encoded list:[[2, 1], 2, 3, [2, 4], 5, 1]

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
