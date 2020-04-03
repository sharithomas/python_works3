# -*- coding: utf-8 -*-
"""
Created on Thu Apr  2 14:14:49 2020

@author: SHARI
"""

#set programs
#1. Write a Python program to create a set.
set1=() #empty set
print(set1)

set2={1,2,3} #nonempty set
print(set2)

#2.Write a Python program to iteration over sets.
set1=set(range(0,10))
for x in set1:
    print(x)

#3. Write a Python program to add member(s) in a set
set1= set((1,2,3,4,5,6,7,8))
set1.add(22) # add single items
print(set1)
set1.update((100,200)) # add multiple items
print(set1)

#4. Write a Python program to remove item(s) from set
my_set={"apple","orange","banana","plum"}
my_set.remove("apple") #remove item apple
my_set.pop() #remove random item 
my_set.discard("banana") #delete item banana
print(my_set)

#5. Write a Python program to remove an item from a set if it is present in the set
my_set={"apple","orange","banana","plum"}
my_set.discard("grapes")
my_set.discard("banana")
print(my_set)

#6.  Write a Python program to create an intersection of sets
my_set={"apple","orange","banana","plum"}
my_set1={"banana","plum","kiwi"}
set_intersection=my_set.intersection(my_set1)
print(set_intersection)

#7. Write a Python program to create a union of sets
my_set={"apple","orange","banana","plum"}
my_set1={"banana","plum","kiwi"}
set_intersection=my_set.union(my_set1)
print(set_intersection)

#8.Write a Python program to create set difference.
set1={"apple","orange","banana","plum"}
set2={"banana","plum","kiwi"}
diff1=set1-set2
diff2=set2-set1
print("set1-set2=",diff1)
print("set2-set1=",diff2)

#9.Write a Python program to create a symmetric difference
set1={"apple","orange","banana","plum"}
set2={"banana","plum","kiwi"}
print(set1.symmetric_difference(set2))

#10. Write a Python program to issubset and issuperset
set1={"apple","orange","banana","plum"}
set2={"banana","plum"}
sub_set=set2.issubset(set1)
if sub_set:
    print("set2 is subset of set1")
else:
    print("set2 is not subset of set1")
    
super_set=set1.issuperset(set2)
if super_set:
    print("set1 is superset of set2")
else:
    print("set1 is not superset of set2")
    
#11. Write a Python program to create a shallow copy of sets
setp = set(["Red", "Green"])
setq = set(["Green", "Red"])
setr=setp.copy() #shallow copy
print(setr)

#12.Write a Python program to clear a set
set1={"apple","orange","banana","plum"}
print(set1.clear())

#13.Write a Python program to use of frozensets.
x = frozenset([1, 2, 3, 4, 5])
y = frozenset([3, 4, 5, 6, 7])
print(x.isdisjoint(y)) # if disjoint is null return true else return false
print(x.difference(y)) #x-y
print(x|y) # x.union(y)

#14. Write a Python program to find maximum and the minimum value in a set.
set1 = set([10,34,10, 2, 43, 14, 5])
print("maximum value in set:",max(set1))
print("minimum value in set:",min(set1))

#15.Write a Python program to find the length of a set.
set1 = set([34,10, 2, 43, 14, 5])
print("length of set:",len(set1))
