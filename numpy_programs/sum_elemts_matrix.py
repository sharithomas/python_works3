# Write a NumPy program to compute sum of all elements, sum of each column and sum of each row of a given array.

import numpy as np
array=np.arange(1,19).reshape((2,3,3))
print(array)
sum_all=array.sum(axis=None)
sum_col=array.sum(axis=1)
sum_row=array.sum(axis=2)
print("sum of all elements=",sum_all)
print("sum of column elements=\n",sum_col)
print("sum of row elements=\n",sum_row)
