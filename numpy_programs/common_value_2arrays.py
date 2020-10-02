# Write a NumPy program to find common values between two arrays.

import numpy as np
array1=np.array([1,2,3,4,5,6])
print("array1:\n",array1)
array2=np.array([2,4,6,8,10])
print("array2:\n",array2)
print("common elements")
print(np.intersect1d(array1,array2))
