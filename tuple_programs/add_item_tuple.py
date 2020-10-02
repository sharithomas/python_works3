#5.Write a Python program to add an item in a tuple

tuple1=4,2,6,8,9,23
tuple1=tuple1+(34,) #merge tuple with + operator
print(tuple1)
tuple1 = tuple1[:5] + (15, 20, 25) + tuple1[5:] #adding elements at specified locations
print(tuple1)
list1=list(tuple1) #convert tuple to list 
list1.append(100)
tuple1=tuple(list1)
print(tuple1)
