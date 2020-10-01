# Write a Python program to create and display all combinations of letters, selecting each letter from a different key in a dictionary.

dict1={'1':['a','b'], '2':['c','d'],'3':['e','f']}
#fuction to make combinations of letters from a list which contains list of values
def list_combination(list1):
    for i in range(0,len(list1)):
        for j in range(i+1,len(list1)):
            for k in list1[i]:
                for l in list1[j]:
                    print(k+l,end=" ")          
    
list1=[]
#make a list which conatin all values from given dictionary
for v in dict1.values():
    list1.append(v)
print("combinations of letters for dictionary",dict1)
list_combination(list1)
