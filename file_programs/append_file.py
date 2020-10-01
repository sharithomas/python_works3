# Write a Python program to append text to a file and display the text.

f1=open('example.txt','a+') # open file in append with read and write mode
f1.write("third line")
f1.seek(0) # move cursor to 0th position
data=f1.read()
print(data)
f1.close()
