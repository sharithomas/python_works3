# Write a Python program to read a file line by line store it into a variable

def read_file(fname):
    with open(fname,'r') as f1:
        data=f1.read()
        print(data)
        
read_file('example.txt')
