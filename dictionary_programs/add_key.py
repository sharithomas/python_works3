#2. Write a Python script to add a key to a dictionary
dictionary=dict({1:3,2:8,3:6,4:23,5:9,6:67})
print("orginal dictionary  ",dictionary)
dictionary[10]=25
dictionary.update({9:22})
print("dictionary after inserting a new key ",dictionary)
