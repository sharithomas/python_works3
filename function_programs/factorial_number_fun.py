# Write a Python function to calculate the factorial of a number (a non-negative integer). 

#The function accepts the number as an argument

number=int(input("enter a positive number"))
#function definiion to find factorial
def factorial(n):
    fact=1
    for i in range(1,n+1):
        fact=fact*i
    return fact

print("factorial of {} is :".format(number),factorial(number))
