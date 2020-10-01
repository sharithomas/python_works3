# Write a Python program to read a file line by line and store it into a list

f1=open('example.txt','r')
data=f1.readlines()
print(data)
f1.close()
