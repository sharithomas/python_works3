#  Write a Python program to rearrange positive and negative numbers in a given array using Lambda

array_nums = [-1, 2, -3, 5, 0,7, 8, 9, -10]
print("original array",array_nums)
array_out=sorted([x for x in array_nums if x<0]) +sorted([x for x in array_nums if x>=0]) # seperate positive and negative numbers and combine them
print("array after arranging positive and negative numbers",array_out)
