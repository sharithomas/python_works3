# Write a Python program to map two lists into a dictionary

keys=['data1','data2','data3']
values=[1,2,3]
dict1={}
for k in range(0,len(keys)) :
    dict1[keys[k]]=values[k]
print("final dictionary :",dict1)
