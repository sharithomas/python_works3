# Write a Python program to remove newline characters from a file

def remove_newline(fname):
    with open(fname,'r') as f1:
        data=f1.readlines()
    return([s.strip() for s in data]) #remove newline from  each line
    
f=remove_newline('example.txt')     
print(f)
