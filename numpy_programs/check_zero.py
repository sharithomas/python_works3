# Write a NumPy program to test whether none of the elements of a given array is zero

import numpy as np
array=np.array([1,2,3,4])
print("original array")
print(array)
print("if none of the elements in the array is zero")
print(np.all(array) ) #return true if all elements in arry true else return false 
array1=np.array([0,1,2,3,4])
print("original array")
print(array1)
print("if none of the elements in the array is zero")
print(np.all(array1) )
