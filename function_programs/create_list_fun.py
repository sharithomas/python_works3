# Write a Python function to create and print a list where the values are square of numbers between 1 and 30

# (both included)
def list_square():
    list1=[i*i for i in range(1,31) ]
    return list1
print("created list",list_square())
   
