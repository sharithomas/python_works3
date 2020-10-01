# Write a Python program to remove duplicates from Dictionary

dict1={'data1':100,'data2':300,'data3':200,'data4':300,'data5':200}
result={}
for k,v in dict1.items():
    if v not in result.values():
        result[k]=v
print("dictionnary without duplicate values", result)
