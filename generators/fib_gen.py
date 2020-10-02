## simple generator for Fibonacci Numbers 

def fib(limit):
    a,b=0,1
    while a<limit:
        yield a
        a,b=b,a+b
        
limit=int(input("enter limit"))        
x=fib(limit)
for i in range(0,limit):
    print(next(x))


# iterating over generator  using for loop 
for i in fib(limit):
    print(i)
