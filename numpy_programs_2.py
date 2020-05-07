# -*- coding: utf-8 -*-
"""
Created on Thu Apr 30 13:14:50 2020

@author: SHARI
"""

#Numpy Programs
#1. Write a NumPy program to test a given array element-wise for finiteness (not infinity or not a Number).
import numpy as np
arr=np.array([1,0,np.nan,np.inf])
print("originl array",arr)
print("Testing infinity of array")
print(np.isfinite(arr))

#2. Write a NumPy program to create an array with the values 1, 7, 13, 105 and 
#determine the size of the memory occupied by the array
import numpy as np
arr=np.array([1,7,13,105])
print("original array",arr)
print("%d bytes"%(arr.size*arr.itemsize))

#3. Write a NumPy program to create an array of 10 zeros,10 ones, 10 fives.
import numpy as np
array1=np.zeros(10)
print("array with 10 zeros",array1)
array2=np.ones(10)
print("array with 10 ones",array2)
array3=np.full(10,5)
print("array with 10 fives",array3)
array4=np.ones(10)*5
print("array with 10 fives",array4)

#4. Write a NumPy program to create an array of the integers from 30 to70
import numpy as np
array=np.arange(30,71)
print("array with integers from 30 to 70: ",array)

#5.Write a NumPy program to create an array of all the even integers from 30 to 70
import numpy as np
array=np.arange(30,71,2)
print("array with all even numbers from 30 to 70=",array)

#6.Write a NumPy program to create a 3x3 identity matrix
import numpy as np
array1=np.diag([1,1,1])
print("3x3 identity matrix\n",array1)
array2=np.identity(3)
print("3x3 identity matrix\n ",array2)

#7.Write a NumPy program to generate a random number between 0 and 1
import numpy as np
rand_num=np.random.normal(0,1)
print("random number between 0 and 1 :",rand_num)

#8.Write a NumPy program to generate an array of 15 random numbers from a standard normal distribution
import numpy as np
rand_nums=np.random.normal(0,1,15)
print("15 random numbers from standard normal distribution :",rand_nums)

#9.Write a NumPy program to create a vector with values ranging from 15 to 55 and 
#print all values except the first and last
import numpy as np
array=np.arange(15,56)
print("original array\n",array)
print("array values except first and last\n",array[1:-1])

#10. Write a NumPy program to create a 3X4 array using and iterate over it
import numpy as np
array=np.arange(1,13).reshape(3,4)
for i in array.flat:
    print(i)
    
#11.Write a NumPy program to create a vector of length 10 with values evenly distributed between 5 and 50
import numpy as np
array=np.linspace(5,50,10)
print("array with length 10 with values 5 to 50\n",array)

#12. Write a NumPy program to create a vector with values from 0 to 20 and change the sign of the numbers in the range from 9 to 15.
import numpy as np
array=np.arange(0,21)
array[(array>=9) &(array<=15 )]*=-1
print("array\n",array)

#13. Write a NumPy program to create a vector of length 5 filled with arbitrary integers from 0 to 10.
import numpy as np
array=np.random.randint(0,10,5)
print("vector with length 5 integers from 0 to 10\n",array)

#14. Write a NumPy program to multiply the values of two given vectors
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
    
#16.Write a NumPy program to create a 3x4 matrix filled with values from 10 to 21
import numpy as np
array=np.arange(10,22).reshape(3,4)
print("array\n",array)
    
#17.Write a NumPy program to create a vector with values ranging from 15 to 55 and 
#print all values except the first and last
import numpy as np
a=np.arange(15,55)
print("original array")
print(a)
print("array except 1st and last element")
print(a[1:-1])

#18.Write a NumPy program to create a 3x4 matrix filled with values from 10 to 21
import numpy as np
array=np.arange(1,11).reshape(2,5)
print("created array\n",array)
print("number of rows and columns of array:",array.shape)

#19.Write a NumPy program to create a 3x3 identity matrix, i.e. diagonal elements are 1, the rest are 0.
import numpy as np
array=np.eye(3)
print("3x3 identity matrix\n",array)

#20.Write a NumPy program to create a 10x10 matrix, in which the elements on the borders will be equal to 1, and inside 0
import numpy as np
array=np.ones((10,10))
array[1:9,1:9]=0
print("10x10 matrix=\n",array)

#21.  Write a NumPy program to create a 5x5 zero matrix with elements on the main diagonal equal to 1, 2, 3, 4, 5.
import numpy as np
array=np.diag((1,2,3,4,5))
print(array)

#22.Write a NumPy program to create a 4x4 matrix in which 0 and 1 are staggered, with zeros on the main diagonal
import numpy as np
array=np.zeros((4,4))
array[::2,1::2]=1
array[1::2,::2]=1

#23.Write a NumPy program to create a 3x3x3 array filled with arbitrary values
import numpy as np
array=np.random.random((3,3,3))
print(array)

#24.Write a NumPy program to compute sum of all elements, sum of each column and sum of each row of a given array.
import numpy as np
array=np.arange(1,19).reshape((2,3,3))
print(array)
sum_all=array.sum(axis=None)
sum_col=array.sum(axis=1)
sum_row=array.sum(axis=2)
print("sum of all elements=",sum_all)
print("sum of column elements=\n",sum_col)
print("sum of row elements=\n",sum_row)

#25. Write a NumPy program to compute the inner product of two given vectors
import numpy as np
v1=np.array(([1,2,3],[1,2,3]))
v2=np.array(([2,3],[2,3],[2,3]))
print("2 arrays are:")
print(v1)
print(v2)
print("inner product of 2 vectors\n",v1.dot(v2))

#26.Write a NumPy program to add a vector to each row of a given matrix. 
import numpy as np
v1=np.array([1,2,3])
v2=np.array(([2,3,4],[1,2,3],[1,3,4]))
print("resultant matrix")
for i in v2:
    print(i+v1)

#27. Write a NumPy program to convert a given array into a list and then convert it into a list again.
import numpy as np
data=[[1,2,3],[2,3,4]]
array=np.array(data)
print("array\n",array)
list1=array.tolist()
print("list\n",list1)
print(data==list1)

#28.Write a NumPy program to compute the x and y coordinates for points on a sine curve and plot the points using matplotlib. 
import numpy as np 
import matplotlib.pyplot as plt
x=np.arange(0,3*np.pi,0.2)   
y=np.sin(x)
f=plt.plot(x,y)
plt.show()
