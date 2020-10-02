# Write a Python program to remove an empty tuple(s) from a list of tuples.

list1=[(), (), ('',), ('a', 'b'), ('a', 'b', 'c'), ('d')]
list1=[x for x in list1 if x]
print(list1)
