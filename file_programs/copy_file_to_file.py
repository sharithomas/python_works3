#  Write a Python program to copy the contents of a file to another file


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
