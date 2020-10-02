# Write a NumPy program to convert an array to a float type

import numpy as np
data=[1,2,3,4,5,6,7,8]
array=np.array(data,dtype="float")
print("original array:",array)

#another method
import numpy as np
array=np.arange(1,10)
print("original array",array)
array_float=np.asfarray(array)
print("array of float type",array_float)
