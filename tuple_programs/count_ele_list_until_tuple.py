# Write a Python program to count the elements in a list until an element is a tuple.

tuple1=[23,45,33,49,(2,6,7),67]
count=0
for i in tuple1:
    if isinstance(i,tuple):
        break
    count=count+1
print("number of elements ina list until a tuple is: ",count)
