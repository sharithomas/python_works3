# example of a generator that reverses a string.

string=input("enter a string")

def gen_string_fun(string):
    str1=string[::-1]
    yield str1
    
for i in gen_string_fun(string):
    print(i)
