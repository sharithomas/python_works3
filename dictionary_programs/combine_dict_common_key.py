# Write a Python program to combine two dictionary adding values for common keys.

d1 = {'a': 100, 'b': 200, 'c':300,'e':100}
d2 = {'a': 300, 'b': 200, 'd':400,'e':200}
d={}
for k,v in d1.items():
    if k in d2.keys():
        d[k]=v+d2[k]  
    else:
        d[k]=v
for k,v in d2.items():
    if k not in d.keys():
        d[k]=v
print("dictionary1",d1)
print("dictionary2",d2)
print("dictionry after combining dictionary 1 and dictionary 2: ",d)
