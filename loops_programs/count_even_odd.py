# Write a Python program to count the number of even and odd numbers from a series of numbers.

numbers=tuple(range(1,10))
print("given numbers",numbers)
even=0
odd=0
for i in numbers:
    if i%2==0:
        even=even+1
    else:
        odd=odd+1
print("number of even numbers: ",even)
print("number of odd numbers: ",odd)
