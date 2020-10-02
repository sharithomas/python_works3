# Write a Python program to check the validity of password input by users.
#Validation :
#1.At least 1 letter between [a-z] and 1 letter between [A-Z].
#2.At least 1 number between [0-9].
#3.At least 1 character from [$#@].
#4.Minimum length 6 characters.
#5.Maximum length 16 characters.


password=input("enter password")
length=0
flag=0
special_ch=['$','#','@']
# function definition to check validty of each character of given password
def validity(ch):
    if ch.isdigit():
        flag=1
    elif ch.isalpha():
        flag=1
    elif ch in special_ch:
        flag=1
    else:
        flag=0
    return flag

pass_len=len(password)
validity_list=[]
if (pass_len>=6) and (pass_len<=16):  #check length of password 
    length=1
    
for i in password: # reading each character of password and save value 1 in validty_list if that character is valid else save 0
   validity_list.append(validity(i))
if 0 not in validity_list:
    print("valid password")
else:
    print("Invalid password")
