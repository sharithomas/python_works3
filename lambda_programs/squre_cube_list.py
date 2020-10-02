# Write a Python program to square and cube every number in a given list of integers using Lambda

num= [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
print("original list: ",num)
x_square=list(map(lambda x:x**2,num))
print("square of numbers: ",x_square)
x_cube=list(map(lambda x:x**3,num))
print("square of numbers: ",x_cube)
