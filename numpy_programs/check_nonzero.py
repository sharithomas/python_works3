# Write a NumPy program to test whether any of the elements of a given array is non-zero

import numpy as np
array=np.array([0,3,0,0,0])
print(np.dtype)
print("original array")
print(array)
print("test if any elements in array is non zero ")
print(np.any(array)) # any() returns True if any item in an iterable are true, otherwise it returns False
array1=np.array([0,0,0,0,0])
print("original array")
print(array1)
print("test if any elements in array is non zero ")
print(np.any(array1))
