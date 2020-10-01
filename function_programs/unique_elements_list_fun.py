# Write a Python function that takes a list and returns a new list with unique elements of the first list

list_in=[1,2,3,3,3,3,4,5]
list_out=[]
#function to make a list with unique elements
def unique_numbers(list_in):
    for i in list_in:
        if i not in list_out:
            list_out.append(i)
    return list_out
print("given list",list_in)
print("list with unique elements",unique_numbers(list_in))
