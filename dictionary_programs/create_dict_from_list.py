# Write a Python program to create a dictionary from a string

str1=input("enter string")
dict1={}
for i in str1:
    if i not in dict1:
        dict1[i]=1
    else:
        dict1[i]=dict1[i]+1
print("dictionary to count occurences of each characters in a string",dict1)
