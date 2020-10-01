# Write a Python function to multiply all the numbers in a list

list1=[1,2,3,4,5,6]
#function definition to find list product
def list_product(list1):
    result=1
    for i in list1:
        result=result*i
    return result
print("list is ",list1)
print("product of list is: ",list_product(list1))
