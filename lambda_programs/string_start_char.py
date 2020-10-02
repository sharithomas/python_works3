# Write a Python program to find if a given string starts with a given character using Lambda. 

string=input("enter a string")
ch=input("enter a character")
x=lambda a:True if string[0]==ch else False
print(x(string))
