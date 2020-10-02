# Write a Python program to filter a list of integers using Lambda.

num= [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
print("original list: ",num)
x_even=list(filter(lambda a:a%2==0,num))
print("list with even numbers:",x_even)
x_odd=list(filter(lambda a:a%2!=0,num))
print("list with even numbers:",x_odd)
