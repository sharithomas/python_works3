#  Write a Python program to combine values in python list of dictionaries

dict1=[{'item': 'item1', 'amount': 400}, {'item': 'item2', 'amount': 300}, {'item': 'item1', 'amount': 750}]
dict2={}
for d in dict1:
    if d['item'] not in dict2:
        dict2[d['item']]=d['amount']
    else:
        dict2[d['item']]=d['amount']+dict2[d['item']]
print("combined values of dictionaries",dict2)
