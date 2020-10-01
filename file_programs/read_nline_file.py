# Write a Python program to read first n lines of a file

f1=open('example.txt','r')
n=int(input("enter number of lines required from first poistion"))
data=f1.readlines() # read all lines from file and save as list in data
for i in range(n): # read n lines from saved list data
    print(data[i])
f1.close()
