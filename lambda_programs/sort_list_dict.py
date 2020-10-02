#  Write a Python program to sort a list of dictionaries using Lambda

lis = [{ "name" : "Nandini", "age" : 20},  
{ "name" : "Manjeet", "age" : 25 }, 
{ "name" : "Nikhil" , "age" : 19 }] 
print("original list: ",lis)

lis.sort(key=lambda x: x['age'])
print("\n list after sorting:",lis)
