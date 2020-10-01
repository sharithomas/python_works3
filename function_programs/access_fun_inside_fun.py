#  Write a Python program to access a function inside a function.

array=[1,2,3,4,5]
def sum_square(array):
    sum=0
    for i in array:
        sum=sum+square(i)
    return sum

def square(x):
    return x*x
s=sum_square(array)
print("sum of square array elements=",s)
