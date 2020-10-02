
# Write a NumPy program to multiply the values of two given vectors

import numpy as np
v1=np.array([1,2,3,4])
v2=np.arange(5,9)
print("given vectors",v1,v2)
print("product of 2 vectors",v1*v2)
#15.Write a NumPy program to create a 3X4 array using and iterate over it.
import numpy as np
x=np.arange(0,12).reshape(3,4)
for i in x.flat:
    print(i)
    
