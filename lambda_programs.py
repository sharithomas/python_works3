# -*- coding: utf-8 -*-
"""
Created on Sun Apr 19 14:29:30 2020

@author: I325377
"""

#Lambda functions programs
#lambda arguments : expression

#1. add 10 to a number
x=lambda a:a+10
print(x(20))

#2. multiply 2 numbers
x=lambda a,b:a*b
print(x(2,3))

#3.sum of 3 numbers
x=lambda a,b,c:a+b+c
print(x(10,20,30))

#4.multiply number with 2 use function
def myfunc(n):
  return  lambda a: a * n

mydoubler = myfunc(2)

print(mydoubler(11))

#5.multiply number with 2 and 3 use function
def myfunc(n):
  return  lambda a: a * n

mydoubler = myfunc(2)
mytripler = myfunc(3)

print(mydoubler(11))
print(mytripler(11))

#6.Write a Python program to create a lambda function that adds 15 to a given number passed in as an argument,
# also create a lambda function that multiplies argument x with argument y and print the result.
x=lambda a:a+15
print(x(5))
x=lambda a,b:a*b
print(x(2,3))

#7. Write a Python program to create a function that takes one argument, and that argument will be multiplied with an unknown given number.
x=lambda a:a*3
print(x(2))

#8. Write a Python program to sort a list  using Lambda.
a=[2,3,7,4,6,
x=lambda a:sorted(a)
print(x(a))

#9.Write a Python program to sort a list of tuples using Lambda.
a = [('English', 88), ('Science', 90), ('Maths', 97), ('Social sciences', 82)]
print("original list: ",a)

a.sort(key= lambda x:x[1])
print("\n list after sorting: ",a)

#10. Write a Python program to sort a list of dictionaries using Lambda
lis = [{ "name" : "Nandini", "age" : 20},  
{ "name" : "Manjeet", "age" : 25 }, 
{ "name" : "Nikhil" , "age" : 19 }] 
print("original list: ",lis)

lis.sort(key=lambda x: x['age'])
print("\n list after sorting:",lis)

#11.Write a Python program to filter a list of integers using Lambda.
num= [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
print("original list: ",num)
x_even=list(filter(lambda a:a%2==0,num))
print("list with even numbers:",x_even)
x_odd=list(filter(lambda a:a%2!=0,num))
print("list with even numbers:",x_odd)

#12.Write a Python program to square and cube every number in a given list of integers using Lambda
num= [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
print("original list: ",num)
x_square=list(map(lambda x:x**2,num))
print("square of numbers: ",x_square)
x_cube=list(map(lambda x:x**3,num))
print("square of numbers: ",x_cube)

#13.Write a Python program to find if a given string starts with a given character using Lambda. 
string=input("enter a string")
ch=input("enter a character")
x=lambda a:True if string[0]==ch else False
print(x(string))

#14.Write a Python program to extract year, month, date and time using Lambda
import datetime
now=datetime.datetime.now()
print(now)
year=lambda x:x.year
month=lambda x:x.month
date=lambda x:x.day()
date=lambda x:x.date()
time=lambda x:x.time()

print(month(now))
print(year(now))
print(day(now))
print(date(now))
print(time(now))

#15. Write a Python program to check whether a given string is number or not using Lambda
string=input("enter  a string")
x=lambda string:string.isdigit()  #return true if all characters are digit
if x(string) is True :
    print(string+" is a number")
else:
    print(string+ "is not a number")
  
#16. Write a Python program to create Fibonacci series upto n using Lambda

n=int(input("enter limit"))

    #function definition to generate fibannoci series
def fib(n):
    fib_list=[0,1]
     #the list fib_list which already has 0 and 1. Then in the next iteration, 
     #this will be used as input and result of their sum will append to the list for range 2 to n
    any(map(lambda x: fib_list.append(sum(fib_list[-2:])),range(2,n))) # add 
    return fib_list[:n]

print(fib(n))

#17. Write a Python program to find intersection of two given arrays using Lambda
list1=[2,3,4,5,6,7,8]
list2=[1,3,5,7,8,9]
list_in=[]
intersection=list(filter(lambda x:  x in list1,list2)) # filter return value if x in list1,list2 is true else igore that value
print("intersection of two lists",intersection)
    
#18. Write a Python program to rearrange positive and negative numbers in a given array using Lambda
array_nums = [-1, 2, -3, 5, 0,7, 8, 9, -10]
print("original array",array_nums)
array_out=sorted([x for x in array_nums if x<0]) +sorted([x for x in array_nums if x>=0]) # seperate positive and negative numbers and combine them
print("array after arranging positive and negative numbers",array_out)

#19. Write a Python program to count the even, odd numbers in a given array of integers using Lambda
list_in=[2,5,6,7,19,10,23]
print("original array",list_in)
even_count=len(list(filter((lambda x:x%2==0),list_in))) #if x%2==0 is true accept that number from list_in and make a new list
print("number of even numbers=",even_count)
even_count=len(list(filter((lambda x:x%2!=0),list_in)))
print("number of odd numbers=",odd_count)
#another method
#list_count=list(map((lambda x: x%2 ),list_in))
#even_count=list_count.count(0)
#odd_count=list_count.count(1)
#print("number of even numbers=",even_count)
#print("number of odd numbers=",odd_count)

#20.Write a Python program to filter a given list whether the values in the list are having 
#length of 6 using Lambda.
list_in=["apple","orange","kiwi","banana","grapes","pomogranate","mango"]
print("original list",list_in)
list_out=list(filter(lambda x: len(x)==6,list_in)) 
print("list after filtering:")
for i in list_out:
    print(i,end=" ")

#21.Write a Python program to add two given lists using map and lambda
list1=[1,2,3,4]
list2=[2,4,6,8]
print("given lists are:",list1,list2)
list_add=list(map((lambda x,y:x+y),list1,list2))
print("after adding 2 lists:",list_add)

#22.Write a Python program to find the second lowest grade of any student(s) from the given names and grades
#of each student using lists and lambda.Input number of students, names and grades of each student.
n=int(input("input number of students"))
list_students=[]
for i in range(n):
    name=input("name:")
    grade=int(input("grade"))
    list_students.append([name,grade])
print("names and grades of all students",list_students)
sort_list=sorted(list_students,key=lambda x:x[1])
length=len(sort_list)
print("second lowest grade is",sort_list[length-2][1])

#23.Write a Python program to find numbers divisible by nineteen or thirteen from a list of numbers using Lambda
num_in = [19, 65, 57, 39, 152, 639, 121, 44, 90, 190]
print("original list",num_in)
num_out=list(filter(lambda x: x%19==0 or x%13==0 ,nums))
print("numbers divisible by 13 or 19",num_out)

#24.Write a Python program to find palindromes in a given list of strings using Lambda.
list_in=["aaa","java","python","php","abcd"]
print("original list",list_in)
list_out=list(filter(lambda x: x==x[::-1],list_in)) # if string equal to its reverse is palindrome
print("list with palindrome strings",list_out)

#25.Write a Python program to find all anagrams of a string in a given list of strings using lambda
#An anagram of a string is another string that contains same characters, 
#only the order of characters can be different. eg: silent==listen
from collections import Counter 
texts = ["bcda", "abce", "cbda", "cbea", "adcb"]
print("original list",texts)
string="abcd"
list_out=list(filter(lambda x: Counter(x)==Counter(string),texts)) #Counter(abcd) return a:1 b:1 c:1 d:1
print("Anagrams of 'abcd' in the above list:",list_out)

