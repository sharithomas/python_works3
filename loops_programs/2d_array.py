# Write a Python program which takes two digits m (row) and n (column) as input and generates a two-dimensional array. 
#The element value in the i-th row and j-th column of the array should be i*j

import numpy as np
row=int(input("enter number of rows"))
col=int(input("enter number of columns"))
a=np.zeros((row,col)) # create a matrix given with number of rows and columns

for i in range(row):
    for j in range(col):
        a[i][j]=i*j #each matrix element set as product row and column indexes
print(a)    
