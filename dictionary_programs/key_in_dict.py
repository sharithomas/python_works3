#4. Write a Python script to check whether a given key already exists in a dictionary.
dictionary=dict({1:3,2:8,3:6,4:23,5:9,6:67})
key=int(input("enter key to search"))
if key in dictionary:
    print("key exist in dictionary")
else:
    print("key not exist in dictionary")
