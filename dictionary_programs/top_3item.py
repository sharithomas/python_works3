# Write a Python program to get the top three items in a shop

import heapq
import operator
items_dict={'item1': 45.50, 'item2':35, 'item3': 41.30, 'item4':55, 'item5': 24}
for key,value in heapq.nlargest(3,items_dict.items(),key=operator.itemgetter(1)):
    print(key,value)
