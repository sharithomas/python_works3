 # Write a NumPy program to create a 5x5 zero matrix with elements on the main diagonal equal to 1, 2, 3, 4, 5.
 
 import numpy as np
 a=np.zeros((5,5))
 print(a)
a[0][0]=1
a[1,1]=2
a[2][2]=3
a[3,3]=4
a[4][4]=5
print("after assiging values ")
print(a)
x=np.diag([1,2,3,4,5]) # create matrix with given diagonal elements
print(x)
