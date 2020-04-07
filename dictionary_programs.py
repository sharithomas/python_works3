# -*- coding: utf-8 -*-
"""
Created on Fri Apr  3 07:42:44 2020

@author: SHARI
"""

#Dictionary Programs
#1. Write a Python script to sort (ascending and descending) a dictionary by value.
import operator
dictionary=dict({1:3,2:8,3:6,4:23,5:9,6:67})
print("orginal dictionary",dictionary)
sorted_asc=dict(sorted(dictionary.items(),key=operator.itemgetter(1)))
print("dictionary in ascending order of value",sorted_asc)
sorted_dec =dict(sorted(dictionary.items(),key=operator.itemgetter(1),reverse=True))
print("dictionary in ascending order of value",sorted_dec)

#2. Write a Python script to add a key to a dictionary
dictionary=dict({1:3,2:8,3:6,4:23,5:9,6:67})
print("orginal dictionary  ",dictionary)
dictionary[10]=25
dictionary.update({9:22})
print("dictionary after inserting a new key ",dictionary)

#3. Write a Python script to concatenate following dictionaries to create a new one.
#dic1={1:10, 2:20}, dic2={3:30, 4:40}, dic3={5:50,6:60}, Expected Result : {1: 10, 2: 20, 3: 30, 4: 40, 5: 50, 6: 60}
dic1={1:10, 2:20}
dic2={3:30, 4:40}
dic3={5:50,6:60}
result_dict={}
for d in (dic1,dic2,dic3):
    result_dict.update(d)
print("resultant dictionary",result_dict)

#4. Write a Python script to check whether a given key already exists in a dictionary.
dictionary=dict({1:3,2:8,3:6,4:23,5:9,6:67})
key=int(input("enter key to search"))
if key in dictionary:
    print("key exist in dictionary")
else:
    print("key not exist in dictionary")
    
#5.Write a Python program to iterate over dictionaries using for loops
dictionary=dict({1:3,2:8,3:6,4:23,5:9,6:67})
for k,v in dictionary.items():
    print(k ,":", v)
    
#6. Write a Python script to generate and print a dictionary that contains a number (between 1 and n) in the form (x, x*x)
dict1={}
n=int(input("enter value of n"))
#creating dictionary
for i in range(1,n+1):
    dict1[i]=i*i
#print dictionary
print(dict1)

#7. Write a Python script to print a dictionary where the keys are numbers between 1 and 15 (both included) and the values are square of keys.
dict1={}
#creating dictionary
for i in range(1,16):
    dict1[i]=i*i
#print dictionary
print(dict1)

#8. Write a Python script to merge two Python dictionaries
d1={1:"apple",2:"orange",3:"kiwi"}
d2={5:"pineapple",6:"grapes"}
d1.update(d2)
print("merged dictionary", d1)

#9.Write a Python program to sum all the items in a dictionary.
my_dict = {'data1':500,'data2':-54,'data3':37,'data4':17}
print("sum of dctionarry values")
print(sum(my_dict.values()))

#10.Write a Python program to multiply all the items in a dictionary.
my_dict = {'data1':2,'data2':3,'data3':5,'data4':4}
print("product of dctionarry values")
product=1
for i in my_dict.values():
    product=product*i
print(product)

#11. Write a Python program to remove a key from a dictionary
my_dict = {'data1':2,'data2':3,'data3':5,'data4':4}
print("original dictionary",my_dict)
del my_dict['data2']
print("dictionary after deleting a key")
print(my_dict)

#12.Write a Python program to map two lists into a dictionary
keys=['data1','data2','data3']
values=[1,2,3]
dict1={}
for k in range(0,len(keys)) :
    dict1[keys[k]]=values[k]
print("final dictionary :",dict1)

#13.Write a Python program to sort a dictionary by key
dictionary=dict({1:3,6:8,3:6,7:23,5:9,2:67})
dict1=dict(sorted(dictionary.items()))
print("dictionary after sorting based on keys:", dict1)

#14.Write a Python program to get the maximum and minimum value in a dictionary
dictionary=dict({1:3,6:8,3:6,7:23,5:9,2:67})
max_value=max(dictionary.values())
min_value=min(dictionary.values())
print("maximum value=", max_value)
print("minimum valuue=",min_value)

#15. Write a Python program to remove duplicates from Dictionary
dict1={'data1':100,'data2':300,'data3':200,'data4':300,'data5':200}
result={}
for k,v in dict1.items():
    if v not in result.values():
        result[k]=v
print("dictionnary without duplicate values", result)
        
#15.Write a Python program to check a dictionary is empty or not
dict1={}
dict2={1:2,2:3,3:4}
def empty_dict(dictionary):
    if dictionary is {}:
        print(dictionary," is empty")
    else:
        print(dictionary,"is not empty")
empty_dict(dict1)
empty_dict(dict2)

#16.Write a Python program to combine two dictionary adding values for common keys.
d1 = {'a': 100, 'b': 200, 'c':300,'e':100}
d2 = {'a': 300, 'b': 200, 'd':400,'e':200}
d={}
for k,v in d1.items():
    if k in d2.keys():
        d[k]=v+d2[k]  
    else:
        d[k]=v
for k,v in d2.items():
    if k not in d.keys():
        d[k]=v
print("dictionary1",d1)
print("dictionary2",d2)
print("dictionry after combining dictionary 1 and dictionary 2: ",d)

#17.Write a Python program to print all unique values in a dictionary
dictionary={"data1":"S001", "data2": "S002", "data3": "S001", "data4": "S005", "data5":"S005", "data6":"S009","data7":"S007"}
list1=[]
#check eacch values from dictionary and append to alist if it is unique
for v in dictionary.values():
    if v not in list1:
        list1.append(v)
print("unique values from dictionary\n")
for i in list1:
    print(i,end=" ")
    
#18..Write a Python program to create and display all combinations of letters, selecting each letter from a different key in a dictionary.
dict1={'1':['a','b'], '2':['c','d'],'3':['e','f']}
#fuction to make combinations of letters from a list which contains list of values
def list_combination(list1):
    for i in range(0,len(list1)):
        for j in range(i+1,len(list1)):
            for k in list1[i]:
                for l in list1[j]:
                    print(k+l,end=" ")          
    
list1=[]
#make a list which conatin all values from given dictionary
for v in dict1.values():
    list1.append(v)
print("combinations of letters for dictionary",dict1)
list_combination(list1)

#19.Write a Python program to find the highest 3 values in a dictionary.
import operator
my_dict = {'a':500, 'b':5874, 'c': 560,'d':400, 'e':5874, 'f': 20} 
#sort dictionary values in descending order
list_sort=list(sorted(my_dict.items(),key=operator.itemgetter(1),reverse=True))
value=[]
for i in list_sort:
    value.append(i[0])
print(" 3 keys with highest values in dictionary",value[:3],end=" ")

#20. Write a Python program to combine values in python list of dictionaries
dict1=[{'item': 'item1', 'amount': 400}, {'item': 'item2', 'amount': 300}, {'item': 'item1', 'amount': 750}]
dict2={}
for d in dict1:
    if d['item'] not in dict2:
        dict2[d['item']]=d['amount']
    else:
        dict2[d['item']]=d['amount']+dict2[d['item']]
print("combined values of dictionaries",dict2)

#21.Write a Python program to create a dictionary from a string
str1=input("enter string")
dict1={}
for i in str1:
    if i not in dict1:
        dict1[i]=1
    else:
        dict1[i]=dict1[i]+1
print("dictionary to count occurences of each characters in a string",dict1)

#22. Write a Python program to print a dictionary in table format
import pandas as pd
my_dict = {'C1':[1,2,3],'C2':[5,6,7],'C3':[9,10,11]}      
table_dict=pd.DataFrame(my_dict)
print(table_dict)

#23. Write a Python program to count the values associated with key in a dictionary.
student = [{'id': 1, 'success': True, 'name': 'Lary'}, {'id': 2, 'success': False, 'name': 'Rabi'},
           {'id': 3, 'success': True, 'name': 'Alex'}]
count=0
#count number of dictionary which has success with value True
for i in student:
    if i['success']==True:
        count=count+1
    else:
        pass
print("count of dictionary with value True for key sucess = ", count)

#24.  Write a Python program to convert a list into a nested dictionary of keys
dict1=[1,2,3,4,5]
new_dict=curr_dict={}
#making nested dictionary
for num in dict1:
    curr_dict[num]={}
    curr_dict=curr_dict[num]
print(new_dict)
    
#25.  Write a Python program to sort a list alphabetically in a dictionary
dict1 = {'n1': ['apple','orange','banana'], 'n2': ['kiwi','watermelon','grapes'], 'n3': ['plum','strawberry','avacado']}
sort_dict={x:sorted(y) for x,y  in dict1.items()}
print(sort_dict)

#26.Write a Python program to remove spaces from dictionary keys
student_dict = {'S  001': ['Math', 'Science'], 'S    002': ['Math', 'English']}
result_dict={}
print("original dictionary",student_dict)
for k,v in student_dict.items():
    if " " in k:
        k=k.replace(" ","")
        result_dict[k]=v
print("\n new dictionary",result_dict)

#27.Write a Python program to get the top three items in a shop
import heapq
import operator
items_dict={'item1': 45.50, 'item2':35, 'item3': 41.30, 'item4':55, 'item5': 24}
for key,value in heapq.nlargest(3,items_dict.items(),key=operator.itemgetter(1)):
    print(key,value)
    
#28.Write a Python program to get the key, value and item in a dictionary.
dict_num = {1: 10, 2: 20, 3: 30, 4: 40, 5: 50, 6: 60}
print("key  value  count")
count=0
for key,value in dict_num.items():
    count=count+1
    print(key,'  ',value,'  ',count)
    
#29.Write a Python program to print a dictionary line by line.
students_dict= {'Alex':{'class':'V','rolld_id':2}, 'Puja':{'class':'V', 'roll_id':3}}
for i in students_dict:
    print(i)
    for j in students_dict[i]:
        print(j,':',students_dict[i][j])