#  Write a Python function program to print the even numbers from a given list

list_in= [1, 2, 3, 4, 5, 6, 7, 8, 9]
list_out=[]
#check each numbers in the list and append it to a new list if it even else wont append
def list_even(list1):
    for i in list1:
        if i%2==0:
            list_out.append(i)
        else:
            pass
    return list_out
print("given list",list_in)
print("list with even numbers",list_even(list_in))
