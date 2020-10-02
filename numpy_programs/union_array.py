
#  Write a NumPy program to find the union of two arrays. Union will return the unique, sorted array of values that are in either of the two input arrays.

import numpy as np
array1=np.array([0,10,20,40,60,80])
print("array1:\n",array1)
array2=np.array([10, 30, 40, 50, 70, 90])
print("array1:\n",array2)
print("resultant array\n",np.union1d(array1,array2))
