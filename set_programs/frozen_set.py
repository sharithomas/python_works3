# Write a Python program to use of frozensets.

x = frozenset([1, 2, 3, 4, 5])
y = frozenset([3, 4, 5, 6, 7])
print(x.isdisjoint(y)) # if disjoint is null return true else return false
print(x.difference(y)) #x-y
print(x|y) # x.union(y)
