# Write a Python program to find all anagrams of a string in a given list of strings using lambda

#An anagram of a string is another string that contains same characters, 
#only the order of characters can be different. eg: silent==listen
from collections import Counter 
texts = ["bcda", "abce", "cbda", "cbea", "adcb"]
print("original list",texts)
string="abcd"
list_out=list(filter(lambda x: Counter(x)==Counter(string),texts)) #Counter(abcd) return a:1 b:1 c:1 d:1
print("Anagrams of 'abcd' in the above list:",list_out)
