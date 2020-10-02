
#  Write a NumPy program to find the set exclusive-or of two arrays. Set exclusive-or will return the sorted, unique values that are in only one (not both) of the input arrays.

import numpy as np
array1=np.array([0,10,20,40,60,80])
print("array1:\n",array1)
array2=np.array([10, 30, 40, 50, 70, 90])
print("array1:\n",array2)
print("resultant array\n",np.setxor1d(array1,array2))
