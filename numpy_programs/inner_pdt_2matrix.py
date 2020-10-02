#  Write a NumPy program to compute the inner product of two given vectors

import numpy as np
v1=np.array(([1,2,3],[1,2,3]))
v2=np.array(([2,3],[2,3],[2,3]))
print("2 arrays are:")
print(v1)
print(v2)
print("inner product of 2 vectors\n",v1.dot(v2))
