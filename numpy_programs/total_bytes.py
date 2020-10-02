#  Write a NumPy program to find the number of elements of an array, length of one array element in bytes and total
# bytes consumed by the elements

import numpy as np
array=np.array([1,2,3,4,5])
print("original array\n",array)
print("number of elements of array: ",array.size)
print("length of one array element: ",array.itemsize)
print("total bytes by the elements: ",array.nbytes#array.size*array.itemsize)
