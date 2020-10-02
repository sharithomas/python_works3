#class portion
    
ee=range(0,10)
for i in range(0,10):
    print(i)
    
list1=range(0,10)
type(list1)

id(list1)

list1=list(range(0,10))
type(list1)

#9.# Generator function for the square of numbers (power of 2)
def square_num(limit):
    for i in range(1,limit+1):
        yield i**2

limit=int(input("enter limit"))
for i in square_num(limit):
    print(i)

#without using generators
def square_num(limit):
    for i in range(1,limit+1):
        print (i**2)

limit=int(input("enter limit"))
square_num(limit)   

#without using generators , list
def square_num(limit):
    list1=[]
    for i in range(1,limit+1):
        list1.append(i**2)
    return list1

limit=int(input("enter limit"))
square_num(limit)   

#10.fibannoci series using generators
def fib_num(limit):
    a,b=0,1
    for i in range(0,limit):
        yield a
        a,b=b,a+b

limit=int(input("enter limit"))
for i in fib_num(limit):
    print(i)
    
# fibannoci without generators using list
def fib_num(limit):
    list1=[]
    a,b=0,1
    for i in range(0,limit):
        list1.append(i)
        a,b=b,a+b
    return list1

limit=int(input("enter limit"))
fib_num(limit)
    
    
#Iterate over string
str1=iter("hello")
next(str1)
