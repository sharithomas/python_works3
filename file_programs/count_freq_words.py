#  Write a Python program to count the frequency of words in a file

from collections import Counter
with open('example.txt','r') as f1:
    print(Counter(f1.read().split()))
