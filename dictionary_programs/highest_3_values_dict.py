# Write a Python program to find the highest 3 values in a dictionary.

import operator
my_dict = {'a':500, 'b':5874, 'c': 560,'d':400, 'e':5874, 'f': 20} 
#sort dictionary values in descending order
list_sort=list(sorted(my_dict.items(),key=operator.itemgetter(1),reverse=True))
value=[]
for i in list_sort:
    value.append(i[0])
print(" 3 keys with highest values in dictionary",value[:3],end=" ")
