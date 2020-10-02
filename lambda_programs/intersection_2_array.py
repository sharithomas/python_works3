
#  Write a Python program to find intersection of two given arrays using Lambda

list1=[2,3,4,5,6,7,8]
list2=[1,3,5,7,8,9]
list_in=[]
intersection=list(filter(lambda x:  x in list1,list2)) # filter return value if x in list1,list2 is true else igore that value
print("intersection of two lists",intersection)
