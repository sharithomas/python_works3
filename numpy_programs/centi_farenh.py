# Write a NumPy program to convert the values of Centigrade degrees into Fahrenheit degrees #C= 5/9(F-32)

import numpy as np
data_cen=[0, 12, 45.21 ,34, 99.91]
array_C=np.array(data_cen)
array_F=9/5*(array_C)+32
print("array in Centigrade\n",array_C)
print("array in Farenheit",array_F)
