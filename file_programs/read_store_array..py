# Write a Python program to read a file line by line store it into an array

def file_read(fname):
    array_list=[]
    with open(fname,'r') as f1:
        for l in f1:
            array_list.append(l)
    print(array_list)
       
file_read('example.txt')
