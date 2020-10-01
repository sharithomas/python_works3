# Write a Python function to find the Max of three numbers.

#function definition to find largest among 3 numbers
def max_fun(n1,n2,n3):
    large1=n1 if n1>n2 else n2
    large2=large1 if large1>n3 else n3
    return large2
print("enter 3 numbers")
n1=int(input("enter 1st number"))
n2=int(input("enter 2nd number"))
n3=int(input("enter 3rd number"))
print("largest among three numbers is: ",max_fun(n1,n2,n3))
