# Write a Python program to reverse a tuple

tuple1=tuple(range(10,20))
print("given tuple",tuple1)
reverse=reversed(tuple1)
print("reversed tuple is")
print(tuple(reverse))
print(tuple1[::-1])
