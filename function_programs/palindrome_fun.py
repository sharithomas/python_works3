# Write a Python function that checks whether a passed string is palindrome or not

string_in=input("enter a string ")
#if string reverse is same as given string then string is palindrome else not palindrome
def string_palindrome(string):
    string_reverse=string[::-1]
    if string_reverse==string:
        return True
    else:
        return False

flag=string_palindrome(string_in)
if flag==1:
    print(string_in +" is palindrome")
else:
    print(string_in +" is not palindrome")
