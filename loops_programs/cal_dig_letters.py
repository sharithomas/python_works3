# Write a Python program that accepts a string and calculate the number of digits and letters

string1=input("enter string")
digit=letter=0
# take each character of string and count letters and digits
for i in string1:
    if i.isalpha():
        letter=letter+1
    elif i.isdigit():
        digit=digit+1
    else:
        pass
print("total letters=",letter)
print("total digits=",digit)
