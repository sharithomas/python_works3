
# Write a Python program to sort a tuple by its float element

tuple1= [('item1', '12.20'), ('item2', '15.10'), ('item3', '24.5'),('item4','18.6')]
print(sorted(tuple1,key=lambda t:t[-1])[::-1])
