# Write a Python function to sum all the numbers in a list

list1=[1,2,3,4,5,6]
#function definition to find list sum
def list_sum(list1):
    result=0
    for i in list1:
        result=result+i
    return result
print("list is ",list1)
print("sum of list is: ",list_sum(list1))
