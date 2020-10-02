# Write a NumPy program to find the set difference of two arrays. The set difference will return the sorted, unique values in array1 that are not in array2.

import numpy as np
array1=np.array([0,10,20,40,60,80])
print("array1:\n",array1)
array2=np.array([10, 30, 40, 50, 70, 90])
print("array1:\n",array2)
print("resultant array\n",np.setdiff1d(array1,array2))
