# Write a Python program that accepts a hyphen-separated sequence of words as input and prints the words
# in a hyphen-separated sequence after sorting them alphabetically.  
#white-red-green-blue,  o/p:blue-green-red-white

string=input("enter words")

def word_sort(string):
    list1=string.split('-') #split string at each hypen and save as list string1
    list1=sorted(list1) #sort list
    return list1

print("words after sorting ")
string_sorted=word_sort(string) # function call
print('-'.join(string_sorted)) # join list elements with hypen
