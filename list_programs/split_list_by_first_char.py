# Write a Python program to split a list based on first character of word

from itertools import groupby
from operator import itemgetter
list1=list(input("enter list elements seperated with comma").split(","))
print("given list",list1)
for letter,words in groupby(sorted(list1),itemgetter(0)): # groupby()-This method calculates the keys for each element present in iterable.
                                                            #It returns key and iterable of grouped items.
    print(letter)                                   #itemgetter(0) returns 0th index charcter from each word and based on it return group
    for word in words:
        print(word)
