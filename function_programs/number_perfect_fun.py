# Write a Python function to check whether a number is perfect or not.

number=int(input("enter a number"))
#perfect number is the sum of all positive divisors excluding the that number.i,6=1+2+3(sum of divisors of 6) 
def perfect_number(n):
    total_sum=0
    for i in range(1,n):
        if number%i==0:
            total_sum=total_sum+i
    return n==total_sum
     
print(perfect_number(number))
