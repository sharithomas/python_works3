# Write a Python program to issubset and issuperset

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
