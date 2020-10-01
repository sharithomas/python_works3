# Write a Python program to check a dictionary is empty or not

dict1={}
dict2={1:2,2:3,3:4}
def empty_dict(dictionary):
    if dictionary is {}:
        print(dictionary," is empty")
    else:
        print(dictionary,"is not empty")
empty_dict(dict1)
empty_dict(dict2)
