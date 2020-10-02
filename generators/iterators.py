# simple Python program to demonstrate working of iterators 

#create a list
list1=list([1,2,3,4])

# create an iterator using iter()
iter1=iter(list1)

## iterate through it using next() 
print(next(iter1))
print(next(iter1))
print(next(iter1))
print(next(iter1))
print(next(iter1)) #stopIteration error
