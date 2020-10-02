# Write a NumPy program to add a border (filled with 0's) around an existing array

import numpy as np
array=np.zeros((4,4))
array[1:-1,1:-1]=1
print(array)
