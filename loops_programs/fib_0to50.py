# Write a Python program to get the Fibonacci series between 0 to 50
    
#function definition to generate fibannoci series
def fib(n):
    a=0
    b=1
    c=0
    while a<=n:
        print(a,end=" ")
        c=a+b
        a=b
        b=c
n=int(input("enter limit"))
fib(n)
