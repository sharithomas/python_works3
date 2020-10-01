#  Write a Python program to assess if a file is closed or not

f1=open('example.txt','r')
print(f1.closed) #return true if closed else return false
f1.close()
print(f1.closed)
