# Write a Python program to count the number of strings where the string length is 2 or more and the first and last character 
#are same from a given list of strings

list1=['abc', 'xyz', 'aba', '1221','shhs','2442']
count=0
for i in range(len(list1)):
    if len(list1[i])>=2:
        length=len(list1[i])
        if list1[i][0]==list1[i][length-1]:
            count=count+1
        else:
            pass
print("number of strings with length is 2 or more and first and last are equal :",count)
