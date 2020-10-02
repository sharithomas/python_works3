##########################################################
#programs on packing and unpacking list
####################################################

my_list = [1, 2, 3, 4] 
def func(a,b,c,d):
    print(a,b,c,d)
#unpacking list into 4 arguments
func(*my_list)

#packing
#function uses packing to sum
def sum_values(*values):
    Sum=0
    for i in range(0,len(values)):
        Sum=Sum+values[i]
    return Sum
# Driver code 
print(sum_values(1, 2, 3, 4, 5)) 
print(sum_values(10, 20))

## A sample program to demonstrate unpacking of 
# dictionary items using **
def function_dict(a,b,c,d):
    print(a,b,c,d)
    
dictionary={'a':10,'b':20,'c':30,'d':40}
function_dict(*dictionary) # a b c d
function_dict(**dictionary) # 10 20 30 40
