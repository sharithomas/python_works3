#  Write a Python program to check whether a given string is number or not using Lambda

string=input("enter  a string")
x=lambda string:string.isdigit()  #return true if all characters are digit
if x(string) is True :
    print(string+" is a number")
else:
    print(string+ "is not a number")
  
