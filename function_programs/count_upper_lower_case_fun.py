# Write a Python function that accepts a string and calculate the number of upper case letters and lower case letters

# function definition to count upper and lower case letters
def string_upper_lower():
    string_in=input("enter string")
    upper=0
    lower=0
    for i in string_in:
        if i.isupper():
            upper=upper+1
        elif i.islower():
            lower=lower+1
        else:
            pass
    return (upper,lower)

count=string_upper_lower()
print("number of uppercase letters=",count[0])
print("number of lowercase letters=",count[1])
