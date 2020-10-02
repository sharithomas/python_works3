# Write a NumPy program to add a vector to each row of a given matrix. 

import numpy as np
v1=np.array([1,2,3])
v2=np.array(([2,3,4],[1,2,3],[1,3,4]))
print("resultant matrix")
for i in v2:
    print(i+v1)
