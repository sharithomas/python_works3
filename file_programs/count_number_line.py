# Write a Python program to count the number of lines in a text file

f1=open('example.txt','r')
data=f1.readlines() # read all lines from file and save each line as a single element in list data
print("number of lines in file=",count)
f1.close()
