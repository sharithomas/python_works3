#  Write a Python function that takes a number as a parameter and check the number is prime or not.

number=int(input("enter a number"))

# function to check given number is prime or not. if it prime return flag with value 0 else return 0
def prime(n):
    flag=0
    for i in range(2,n):
        if n%i==0:
            flag=1
            break
    return flag

flag=prime(number)
if flag==0:
    print(str(number)+ " is prime number")
else:
    print(str(number)+ " is not a prime number")
    
