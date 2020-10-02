# Write a Python program to find palindromes in a given list of strings using Lambda.

list_in=["aaa","java","python","php","abcd"]
print("original list",list_in)
list_out=list(filter(lambda x: x==x[::-1],list_in)) # if string equal to its reverse is palindrome
print("list with palindrome strings",list_out)
