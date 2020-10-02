# Write a Python program to construct the following pattern, using a nested loop number.

1
22
333
4444
55555
666666
7777777
88888888
999999999
str1=""
for i in range(1,10):
    for j in range(1,i+1):
        str1=str1+str(i)
    str1=str1+""
    str1=str1+"\n"
print(str1)
