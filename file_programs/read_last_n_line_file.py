#  Write a Python program to read last n lines of a file

f1=open('example.txt')
count=0
n=int(input("enter number of lines required from last poistion"))
data=f1.readlines() # read all lines from file and save as a list in data
for i in range(len(data)-1,0,-1): #read n lines from last position of list data
    if count==n: # if count equal to the number of lines required exit from loop
        break
    print(data[i])
    count=count+1
f1.close()
