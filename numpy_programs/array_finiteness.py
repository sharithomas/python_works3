# Write a NumPy program to test a given array element-wise for finiteness (not infinity or not a Number).

import numpy as np
arr=np.array([1,0,np.nan,np.inf])
print("originl array",arr)
print("Testing infinity of array")
print(np.isfinite(arr))
