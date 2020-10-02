# Write a Python program to find numbers divisible by nineteen or thirteen from a list of numbers using Lambda

num_in = [19, 65, 57, 39, 152, 639, 121, 44, 90, 190]
print("original list",num_in)
num_out=list(filter(lambda x: x%19==0 or x%13==0 ,nums))
print("numbers divisible by 13 or 19",num_out)
