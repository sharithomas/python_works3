#  Write a Python program to get the file size of a plain file

import os # import os
file=os.stat('example.txt') #stat system call on the given path.
print(file.st_size)
