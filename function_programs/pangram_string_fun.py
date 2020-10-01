#  Write a Python function to check whether a string is a pangram or not.

    #pangram is  word which  containing every letter of the alphabet at least once
alphabet="abcdefghijklmnopqrstuvwxyz" #string with all alphabets
string_in=input("enter string")
#function check every letter of the alphabet at least once.
def string_pangram(string):
    for i in alphabet:
        if i not in string.lower():
            return False
    return True
if string_pangram(string_in)==True:
    print("string is pangram")
else:
    print("string is not  pangram")
