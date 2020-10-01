#  Write a Python program to convert a list into a nested dictionary of keys

dict1=[1,2,3,4,5]
new_dict=curr_dict={}
#making nested dictionary
for num in dict1:
    curr_dict[num]={}
    curr_dict=curr_dict[num]
print(new_dict)
