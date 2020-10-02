#  Write a NumPy program to create a vector with values from 0 to 20 and change the sign of the numbers in the range from 9 to 15.

import numpy as np
array=np.arange(0,21)
array[(array>=9) &(array<=15 )]*=-1
print("array\n",array)
