# Write a Python program to add two given lists using map and lambda

list1=[1,2,3,4]
list2=[2,4,6,8]
print("given lists are:",list1,list2)
list_add=list(map((lambda x,y:x+y),list1,list2))
print("after adding 2 lists:",list_add)
