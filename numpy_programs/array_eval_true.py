# write a NumPy program to test whether all elements in an array evaluate to True

import numpy as np
array1=np.array([0,10,20,40,60,80])
print("array1:\n",array1)
print(np.all(array1)) #false- array1 contain one 0 value
