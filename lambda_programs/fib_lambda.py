#  Write a Python program to create Fibonacci series upto n using Lambda


n=int(input("enter limit"))

    #function definition to generate fibannoci series
def fib(n):
    fib_list=[0,1]
     #the list fib_list which already has 0 and 1. Then in the next iteration, 
     #this will be used as input and result of their sum will append to the list for range 2 to n
    any(map(lambda x: fib_list.append(sum(fib_list[-2:])),range(2,n))) # add 
    return fib_list[:n]

print(fib(n))
