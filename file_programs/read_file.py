#files I/O programs
###########################################3


#location:C:\Users\SHARI\Desktop\PYTHON PGMS\lectures\python_set2\files n exceptions code\Files
#pwd - current directory

#1. Write a Python program to read an entire text file
f1=open('example.txt','r') # open example.txt file in read mode
data=f1.read()
print(data)
f1.close()
