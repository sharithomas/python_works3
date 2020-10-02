# Write a Python program to convert a tuple to a dictionary.

tuple1=tuple(range(10,20))
print("given tuple",tuple1)
dictionary=dict((tuple1.index(x),x) for x in tuple1 )
print("converted dictionary",dictionary)
