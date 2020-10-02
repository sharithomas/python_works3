#  Write a Python program to create the colon of a tuple.

from copy import deepcopy
#create a tuple
tuple1 = ("HELLO", 5,[], True) 
print(tuple1)
#make a copy of a tuple using deepcopy() function
tuple1_colon = deepcopy(tuple1)
tuple1_colon[2].append(50)
print(tuple1_colon)
print(tuple1)
