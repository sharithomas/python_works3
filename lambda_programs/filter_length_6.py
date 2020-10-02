# Write a Python program to filter a given list whether the values in the list are having 
#length of 6 using Lambda.

list_in=["apple","orange","kiwi","banana","grapes","pomogranate","mango"]
print("original list",list_in)
list_out=list(filter(lambda x: len(x)==6,list_in)) 
print("list after filtering:")
for i in list_out:
    print(i,end=" ")
