#1. Write a Python script to sort (ascending and descending) a dictionary by value.

import operator
dictionary=dict({1:3,2:8,3:6,4:23,5:9,6:67})
print("orginal dictionary",dictionary)
sorted_asc=dict(sorted(dictionary.items(),key=operator.itemgetter(1)))
print("dictionary in ascending order of value",sorted_asc)
sorted_dec =dict(sorted(dictionary.items(),key=operator.itemgetter(1),reverse=True))
print("dictionary in ascending order of value",sorted_dec)
