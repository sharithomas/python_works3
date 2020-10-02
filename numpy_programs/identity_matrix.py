
# Write a NumPy program to create a 3x3 identity matrix, i.e. diagonal elements are 1, the rest are 0

import numpy as np
array=np.diag([1,1,1])
print("3x3 identity matrix is")
print(array)

import numpy as np
x = np.eye(3) # it returns 3x3 matrix with ones on diagonal and zeros on the remaining parts
print(x)
