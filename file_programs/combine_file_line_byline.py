#  Write a Python program to combine each line from first file with the corresponding line in second file

with open('example1.txt','r') as f1,open('example2.txt','r') as f2: 
#zip() function returns a zip object, which is an iterator of tuples where the first item in each passed iterator is 
 #paired together, and then the second item in each passed iterator are paired together etc.
    for l1,l2 in zip(f1,f2):
        print(l1+l2)
    
