 #  Write a NumPy program to convert a given array into a list and then convert it into a list again.
 
 import numpy as np
 array=np.array([[1,2,3],[5,6,7]])
 print("created array is ")
 print(array)
 print("converted list")
 b=array.tolist()
 print(b) #tolist act as generator tolist() print values
 print(array==b)
