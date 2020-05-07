# -*- coding: utf-8 -*-
"""
Created on Sat May  2 08:28:14 2020

@author: SHARI
"""

#Numpy programs
#1.Write a NumPy program to print the NumPy version in your system.
import numpy as np
print(np.__version__)

#2.Write a NumPy program to convert a list of numeric value into a one-dimensional NumPy array
import numpy as np
list1=[12.23, 13.32, 100, 36.32]
print("list1\n",list1)
array=np.array(list1)
print("numpy array\n",array)

#3.Write a NumPy program to create a 3x3 matrix with values ranging from 2 to 10
import numpy as np
array=np.arange(2,11).reshape(3,3)
print("matrix:\n",array)

#4.Write a NumPy program to create a null vector of size 10 and update sixth value to 11
import numpy as np
array=np.zeros(10)
array[5]=11
print("array\n",array)

#5. Write a NumPy program to create an array with values ranging from 12 to 38
import numpy as np
array=np.arange(12,38)
print("array:",array)

#6. Write a NumPy program to reverse an array (first element becomes last)
import numpy as np
array=np.arange(12,38)
print("original array:",array)
print("reversed array:",array[::-1])

#7.Write a NumPy program to convert an array to a float type
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

#8.Write a NumPy program to create a 2d array with 1 on the border and 0 inside
import numpy as np
array=np.ones((4,4))
array[1:-1,1:-1]=0
print("array=\n",array)

#9.Write a NumPy program to add a border (filled with 0's) around an existing array
import numpy as np
array=np.zeros((4,4))
array[1:-1,1:-1]=1
print(array)

#10. Write a NumPy program to create a 8x8 matrix and fill it with a checkerboard pattern
import numpy as np
array=np.zeros((8,8),dtype="int")
array[::2,1::2]=1
array[1::2,::2]=1
print(array)

#11.Write a NumPy program to convert a list and tuple into arrays.
import numpy as np
list1=[1,2,3,4,5,6,7]
tuple1=([1,2,3],[2,3,4])
print("list to array\n",np.array(list1))
print("tuple to array\n",np.array(tuple1))

#12.Write a NumPy program to append values to the end of an array
import numpy as np
array=np.array([1,2,3,4])
print("original array\n",array)
array1=np.append(array,[5,6,7])
print("array after appending with new values",array1)

#13.Write a NumPy program to create an empty and a full array.
import numpy as np
array_empty=np.empty((4,4))
print("empty array\n",array_empty)
array_full=np.full((4,4),6)
print("full array\n",array_full)

#14.Write a NumPy program to convert the values of Centigrade degrees into Fahrenheit degrees #C= 5/9(F-32)
import numpy as np
data_cen=[0, 12, 45.21 ,34, 99.91]
array_C=np.array(data_cen)
array_F=9/5*(array_C)+32
print("array in Centigrade\n",array_C)
print("array in Farenheit",array_F)

#15.Write a NumPy program to find the real and imaginary parts of an array of complex numbers
import numpy as np
array=np.array([1+2j,3+4j,5+8j])
print("original array\n",array)
real_array=array.real
img_array=array.imag
print("real parts of array\n",real_array)
print("imaginary parts of array\n",img_array)

#16. Write a NumPy program to find the number of elements of an array, length of one array element in bytes and total
# bytes consumed by the elements
import numpy as np
array=np.array([1,2,3,4,5])
print("original array\n",array)
print("number of elements of array: ",array.size)
print("length of one array element: ",array.itemsize)
print("total bytes by the elements: ",array.nbytes#array.size*array.itemsize)

#17. Write a NumPy program to test whether each element of a 1-D array is also present in a second array
import numpy as np
array1=np.array([1,2,3,4,5,6])
print("array1:\n",array1)
array2=np.array([2,4,6])
print("array2:\n",array2)
print("compare 2 arrays:\n")
print(np.in1d(array1,array2))

#18.Write a NumPy program to find common values between two arrays.
import numpy as np
array1=np.array([1,2,3,4,5,6])
print("array1:\n",array1)
array2=np.array([2,4,6,8,10])
print("array2:\n",array2)
print("common elements")
print(np.intersect1d(array1,array2))

#19. Write a NumPy program to get the unique elements of an array.
import numpy as np
array=np.array([1,2,2,3,4,4,5,6,6])
print("original array\n",array)
print("unique elements of array\n")
print(np.unique(array))
    
#20. Write a NumPy program to find the set difference of two arrays. The set difference will return the sorted, unique values in array1 that are not in array2.
import numpy as np
array1=np.array([0,10,20,40,60,80])
print("array1:\n",array1)
array2=np.array([10, 30, 40, 50, 70, 90])
print("array1:\n",array2)
print("resultant array\n",np.setdiff1d(array1,array2))

#21.  Write a NumPy program to find the set exclusive-or of two arrays. Set exclusive-or will return the sorted, unique values that are in only one (not both) of the input arrays.
import numpy as np
array1=np.array([0,10,20,40,60,80])
print("array1:\n",array1)
array2=np.array([10, 30, 40, 50, 70, 90])
print("array1:\n",array2)
print("resultant array\n",np.setxor1d(array1,array2))

#22. Write a NumPy program to find the union of two arrays. Union will return the unique, sorted array of values that are in either of the two input arrays.
import numpy as np
array1=np.array([0,10,20,40,60,80])
print("array1:\n",array1)
array2=np.array([10, 30, 40, 50, 70, 90])
print("array1:\n",array2)
print("resultant array\n",np.union1d(array1,array2))

#23.Write a NumPy program to test whether all elements in an array evaluate to True
import numpy as np
array1=np.array([0,10,20,40,60,80])
print("array1:\n",array1)
print(np.all(array1)) #false- array1 contain one 0 value

#24.  Write a NumPy program to construct an array by repeating
import numpy as np
array1=np.array([0,1,2,3])
print("array1:\n",array1)
print("reapeating 2 times\n",np.tile(array1,2))

#25.  Write a NumPy program to repeat elements of an array.
import numpy as np
print(np.repeat(1,4)) # reapeat 1 four times
a=np.array([[1,2],[3,4,5]])
print(np.repeat(a,2))

