# -*- coding: utf-8 -*-
"""
Created on Tue Jun  9 18:37:06 2020

@author: SHARI
"""

#files I/O programs
###########################################3


#location:C:\Users\SHARI\Desktop\PYTHON PGMS\lectures\python_set2\files n exceptions code\Files
#pwd - current directory

#1. Write a Python program to read an entire text file
f1=open('example.txt','r') # open example.txt file in read mode
data=f1.read()
print(data)
f1.close()

#2. Write a Python program to read first n lines of a file
f1=open('example.txt','r')
n=int(input("enter number of lines required from first poistion"))
data=f1.readlines() # read all lines from file and save as list in data
for i in range(n): # read n lines from saved list data
    print(data[i])
f1.close()

#3.Write a Python program to append text to a file and display the text.
f1=open('example.txt','a+') # open file in append with read and write mode
f1.write("third line")
f1.seek(0) # move cursor to 0th position
data=f1.read()
print(data)
f1.close()

#4. Write a Python program to read last n lines of a file
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

#5. Write a Python program to read a file line by line and store it into a list
f1=open('example.txt','r')
data=f1.readlines()
print(data)
f1.close()

#6. Write a Python program to read a file line by line store it into a variable
def read_file(fname):
    with open(fname,'r') as f1:
        data=f1.read()
        print(data)
        
read_file('example.txt')
    
#7.7. Write a Python program to read a file line by line store it into an array
def file_read(fname):
    array_list=[]
    with open(fname,'r') as f1:
        for l in f1:
            array_list.append(l)
    print(array_list)
       
file_read('example.txt')

#8.Write a python program to find the longest words
def longest_word(fname):
    max_len=0
    # open file and read string into a variable data 
    f1=open(fname,'r') 
    data=f1.read() 
    #split string word by word and save as a list 
    word=data.split()
    #from list word find word with maximum length 
    for i in word:
        if len(i)>max_len:
            max_len=len(i)
            max_word=i
    return (max_len,max_word)
    f1.close()

word=longest_word('example.txt')
print("word with maximum length:",word[1])
print("length:",word[0])
    
# 9.Write a Python program to count the number of lines in a text file
f1=open('example.txt','r')
data=f1.readlines() # read all lines from file and save each line as a single element in list data
print("number of lines in file=",count)
f1.close()

#10. Write a Python program to count the frequency of words in a file
from collections import Counter
with open('example.txt','r') as f1:
    print(Counter(f1.read().split()))
    
#11. Write a Python program to get the file size of a plain file
import os # import os
file=os.stat('example.txt') #stat system call on the given path.
print(file.st_size)

#12. Write a Python program to write a list to a file
city_list=['bangalore','delhi','kochi','mumbai','hydrabad']
f1=open('city.txt','w')
for city in city_list:
    f1.write(city)
f2=open('city.txt','r')
print(f2.read())
f1.close()
f2.close()

#13. Write a Python program to copy the contents of a file to another file

# a.using inbuilt function copyfile
from shutil import copyfile
copyfile("city.txt",'new.txt') # copy from city.txt to new.txt

# b. without using function
f1=open('city.txt','r')
data=f1.read()
f2=open('new.txt','w')
f2.write(data)
f1.close()
f2.close()

#14. Write a Python program to combine each line from first file with the corresponding line in second file
with open('example1.txt','r') as f1,open('example2.txt','r') as f2: 
#zip() function returns a zip object, which is an iterator of tuples where the first item in each passed iterator is 
 #paired together, and then the second item in each passed iterator are paired together etc.
    for l1,l2 in zip(f1,f2):
        print(l1+l2)
    
    
#15. Write a Python program to read a random line from a file.
import random
def read_randomline(fname):
    f1=open(fname,'r')
    data=f1.readlines() #read all line by line and save a s list
    return(random.choice(data)) # choose random element from list data

print(read_randomline('example1.txt'))   

#16. Write a Python program to assess if a file is closed or not
f1=open('example.txt','r')
print(f1.closed) #return true if closed else return false
f1.close()
print(f1.closed)

#17.Write a Python program to remove newline characters from a file
def remove_newline(fname):
    with open(fname,'r') as f1:
        data=f1.readlines()
    return([s.strip() for s in data]) #remove newline from  each line
    
f=remove_newline('example.txt')     
print(f)

#18. Write a Python program that takes a text file as input and returns the number of words of a given text file
#Note: Some words can be separated by a comma with no space.
def file_words(fname):
    with open(fname,'r') as f1:
        data=f1.read()
        data.replace(","," ")
        print(data)
        return(len(data.split(" ")))
    
print(file_words('example.txt'))

#19. delete a file

#To delete a file, you must import the OS module, and run its os.remove() function:
import os 
os.remove('third.txt')

#20. delete an entire folder

#to delete an entire folder, use the os.rmdir() method
#Note: You can only remove empty folders.
import os
os.rmdir('sample') 
