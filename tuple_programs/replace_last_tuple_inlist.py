# Write a Python program to replace last value of tuples in a list. 

#Sample list: [(10, 20, 40), (40, 50, 60), (70, 80, 90)]
#Expected Output: [(10, 20, 100), (40, 50, 100), (70, 80, 100)]
tuple1=[(10, 20, 40), (40, 50, 60), (70, 80, 90)]
print("given tuples in a list",tuple1)
tuple_replace=[x[:-1]+(100,) for x in tuple1]
print("after replacing last value of tuple in list")
print(tuple_replace)
