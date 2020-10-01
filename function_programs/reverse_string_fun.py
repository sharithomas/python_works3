# Write a Python function program to reverse a string.

string_in=input("enter a string") #input string
#function definition for string reverse
def string_reverse(string_in):
    string_out=""
    index=len(string_in)-1
    while index>=0:#read each character from last of input string and append it to output string
        string_out=string_out+string_in[index]
        index=index-1
    return string_out

print("reverse of string",string_reverse(string_in))
