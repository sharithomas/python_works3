# Write a NumPy program to create a 3X4 array using and iterate over it.

import numpy as np
x=np.arange(0,12).reshape(3,4)
for i in x.flat:
    print(i)
