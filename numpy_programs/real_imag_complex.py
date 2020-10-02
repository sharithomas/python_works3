# Write a NumPy program to find the real and imaginary parts of an array of complex numbers

import numpy as np
array=np.array([1+2j,3+4j,5+8j])
print("original array\n",array)
real_array=array.real
img_array=array.imag
print("real parts of array\n",real_array)
print("imaginary parts of array\n",img_array)
