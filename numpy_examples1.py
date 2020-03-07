# -*- coding: utf-8 -*-
"""
Created on Sat Mar  7 09:18:25 2020

@author: SHARI
"""

#Numpy examples
#1.Write a NumPy program to get the numpy version and show numpy build configuration.
import numpy as np
print(np.__version__)
print(np.__config__)
print(np.show_config())

#2. Write a NumPy program to test whether none of the elements of a given array is zero
import numpy as np
array=np.array([1,2,3,4])
print("original array")
print(array)
print("if none of the elements in the array is zero")
print(np.all(array) ) #return true if all elements in arry true else return false 
array1=np.array([0,1,2,3,4])
print("original array")
print(array1)
print("if none of the elements in the array is zero")
print(np.all(array1) )

#3.Write a NumPy program to test whether any of the elements of a given array is non-zero
import numpy as np
array=np.array([0,3,0,0,0])
print(np.dtype)
print("original array")
print(array)
print("test if any elements in array is non zero ")
print(np.any(array)) # any() returns True if any item in an iterable are true, otherwise it returns False
array1=np.array([0,0,0,0,0])
print("original array")
print(array1)
print("test if any elements in array is non zero ")
print(np.any(array1))

#4.Write a NumPy program to compute the x and y coordinates for points on a sine curve
# and plot the points using matplotlib.
 import numpy as np
 import numpy as pi
 import matplotlib.pyplot as plt
 
 x=np.arange(0,2*np.pi,0.2)
 y=np.sin(x)
 plt.plot(x,y)
 
 #5. Write a NumPy program to convert a given array into a list and then convert it into a list again.
 import numpy as np
 array=np.array([[1,2,3],[5,6,7]])
 print("created array is ")
 print(array)
 print("converted list")
 b=array.tolist()
 print(b) #tolist act as generator tolist() print values
 print(array==b)
 
 #6. Write a NumPy program to create a 5x5 zero matrix with elements on the main diagonal equal to 1, 2, 3, 4, 5.
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

#7.Write a NumPy program to create a 10x10 matrix,
# in which the elements on the borders will be equal to 1, and inside 0
import numpy as np
array=np.ones((10,10))
array[1:9,1:9]=0
print("matrix is")
print(array)

#8. Write a NumPy program to create a 3x3 identity matrix, i.e. diagonal elements are 1, the rest are 0

import numpy as np
array=np.diag([1,1,1])
print("3x3 identity matrix is")
print(array)

import numpy as np
x = np.eye(3) # it returns 3x3 matrix with ones on diagonal and zeros on the remaining parts
print(x)

#9. Write a NumPy program to find the number of rows and columns of a given matrix
import numpy as np
x=np.arange(0,20).reshape(4,5)
print("array is")
print(x)
print("no. of rows and columns")
print(x.shape)

#10. Write a NumPy program to create a 3x4 matrix filled with values from 10 to 21
import numpy as np
array=np.arange(10,22).reshape(3,4)
print(array)


#11.Write a NumPy program to multiply the values ​​of two given vectors
import numpy as np
x=np.array([1,2,3,4])
print("1st array")
print(x)
y=np.random.randint(1,11,4)
print(y)
print("multiplied value of vectors")
print(x*y)

#12.Write a NumPy program to create a vector of length 5 filled with arbitrary integers from 0 to 10.
import numpy as np
x=np.random.randint(0,10,5)
print("vector is")
print(x)


#13.Write a NumPy program to create a vector with values from 0 to 20 
#and change the sign of the numbers in the range from 9 to 15
import numpy as np
array=np.arange(0,20)
print("vector with values 0 to 20")
print(array)
print("after changing values")
array[(array>=9)&(array<=15)]*=-1
print(array)

#14. Write a NumPy program to create a vector of length 10 with values evenly distributed between 5 and 50
import numpy as np
y=np.linspace(5,50,10)
print("array is")
print(y)

#15.Write a NumPy program to create a 3X4 array using and iterate over it.
import numpy as np
x=np.arange(0,12).reshape(3,4)
for i in x.flat:
    print(i)
    
#16.Write a NumPy program to create a vector with values ranging from 15 to 55 and 
#print all values except the first and last
import numpy as np
a=np.arange(15,55)
print("original array")
print(a)
print("array except 1st and last element")
print(a[1:-1])

#17.Write a NumPy program to generate an array of 15 random numbers from a standard normal distribution
import numpy as np
x=np.random.normal(0,1,15)