
# Write a NumPy program to create a 2d array with 1 on the border and 0 inside

import numpy as np
array=np.ones((4,4))
array[1:-1,1:-1]=0
print("array=\n",array)
