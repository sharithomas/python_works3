# Write a NumPy program to test whether each element of a 1-D array is also present in a second array

import numpy as np
array1=np.array([1,2,3,4,5,6])
print("array1:\n",array1)
array2=np.array([2,4,6])
print("array2:\n",array2)
print("compare 2 arrays:\n")
print(np.in1d(array1,array2))
