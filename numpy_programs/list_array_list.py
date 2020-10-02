# Write a NumPy program to convert a given list into a array and then convert it into a list again.

import numpy as np
data=[[1,2,3],[2,3,4]]
array=np.array(data)
print("array\n",array)
list1=array.tolist()
print("list\n",list1)
print(data==list1)
