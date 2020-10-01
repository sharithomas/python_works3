#  Write a Python program to read a random line from a file.

import random
def read_randomline(fname):
    f1=open(fname,'r')
    data=f1.readlines() #read all line by line and save a s list
    return(random.choice(data)) # choose random element from list data

print(read_randomline('example1.txt'))  
