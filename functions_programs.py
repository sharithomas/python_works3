# -*- coding: utf-8 -*-
"""
Created on Tue Apr 14 22:13:45 2020

@author: SHARI
"""

#function programs

#1. Write a Python function to find the Max of three numbers.
#function definition to find largest among 3 numbers
def max_fun(n1,n2,n3):
    large1=n1 if n1>n2 else n2
    large2=large1 if large1>n3 else n3
    return large2
print("enter 3 numbers")
n1=int(input("enter 1st number"))
n2=int(input("enter 2nd number"))
n3=int(input("enter 3rd number"))
print("largest among three numbers is: ",max_fun(n1,n2,n3))

#2. Write a Python function to sum all the numbers in a list
list1=[1,2,3,4,5,6]
#function definition to find list sum
def list_sum(list1):
    result=0
    for i in list1:
        result=result+i
    return result
print("list is ",list1)
print("sum of list is: ",list_sum(list1))

#3. Write a Python function to multiply all the numbers in a list
list1=[1,2,3,4,5,6]
#function definition to find list product
def list_product(list1):
    result=1
    for i in list1:
        result=result*i
    return result
print("list is ",list1)
print("product of list is: ",list_product(list1))

#4. Write a Python function program to reverse a string.
string_in=input("enter a string") #input string
#function definition for string reverse
def string_reverse(string_in):
    string_out=""
    index=len(string_in)-1
    while index>=0:#read each character from last of input string and append it to output string
        string_out=string_out+string_in[index]
        index=index-1
    return string_out

print("reverse of string",string_reverse(string_in))

#5. Write a Python function to calculate the factorial of a number (a non-negative integer). 
#The function accepts the number as an argument

number=int(input("enter a positive number"))
#function definiion to find factorial
def factorial(n):
    fact=1
    for i in range(1,n+1):
        fact=fact*i
    return fact

print("factorial of {} is :".format(number),factorial(number))

#6. Write a Python function to check whether a number is in a given range.
number=int(input("enter number"))
#function definition to check whether given number is in the range of 1 to 10
def test_range(n):
    if n in range(1,10):
        print( str(n) + " is in the range of (1,10)")
    else :
        print("The number is outside the given range of (1,10).")
test_range(number)
    
#7. Write a Python function that accepts a string and calculate the number of upper case letters and lower case letters

# function definition to count upper and lower case letters
def string_upper_lower():
    string_in=input("enter string")
    upper=0
    lower=0
    for i in string_in:
        if i.isupper():
            upper=upper+1
        elif i.islower():
            lower=lower+1
        else:
            pass
    return (upper,lower)

count=string_upper_lower()
print("number of uppercase letters=",count[0])
print("number of lowercase letters=",count[1])

#8. Write a Python function that takes a list and returns a new list with unique elements of the first list
list_in=[1,2,3,3,3,3,4,5]
list_out=[]
#function to make a list with unique elements
def unique_numbers(list_in):
    for i in list_in:
        if i not in list_out:
            list_out.append(i)
    return list_out
print("given list",list_in)
print("list with unique elements",unique_numbers(list_in))

#9. Write a Python function that takes a number as a parameter and check the number is prime or not.
number=int(input("enter a number"))

# function to check given number is prime or not. if it prime return flag with value 0 else return 0
def prime(n):
    flag=0
    for i in range(2,n):
        if n%i==0:
            flag=1
            break
    return flag

flag=prime(number)
if flag==0:
    print(str(number)+ " is prime number")
else:
    print(str(number)+ " is not a prime number")
    
#10. Write a Python function program to print the even numbers from a given list
list_in= [1, 2, 3, 4, 5, 6, 7, 8, 9]
list_out=[]
#check each numbers in the list and append it to a new list if it even else wont append
def list_even(list1):
    for i in list1:
        if i%2==0:
            list_out.append(i)
        else:
            pass
    return list_out
print("given list",list_in)
print("list with even numbers",list_even(list_in))

#11. Write a Python function to check whether a number is perfect or not.
number=int(input("enter a number"))
#perfect number is the sum of all positive divisors excluding the that number.i,6=1+2+3(sum of divisors of 6) 
def perfect_number(n):
    total_sum=0
    for i in range(1,n):
        if number%i==0:
            total_sum=total_sum+i
    return n==total_sum
     
print(perfect_number(number))

#12. Write a Python function that checks whether a passed string is palindrome or not
string_in=input("enter a string ")
#if string reverse is same as given string then string is palindrome else not palindrome
def string_palindrome(string):
    string_reverse=string[::-1]
    if string_reverse==string:
        return True
    else:
        return False

flag=string_palindrome(string_in)
if flag==1:
    print(string_in +" is palindrome")
else:
    print(string_in +" is not palindrome")
    
#13. Write a Python function that prints out the first n rows of Pascal's triangle
n=int(input("enter numer of rows"))
#funtcion to create a pascal's triangle and save values in sublists and return the list
def pascal(n):
    a=[]
    for i in range(n):
        a.append([]) #append the sub-lists into the list.
        a[i].append(1) #append 1 into the sub-lists
        for j in range(1,i):
            a[i].append(a[i-1][j-1]+a[i-1][j]) #Each number is the two numbers above it added together
        if(n!=0):
            a[i].append(1)
    return a
            
b=pascal(n)   
#print list in pascal's triangle format
for i in range(n):
    print(" "*(n-i),end=" ")
    for j in range(0,i+1):
        print("{} ".format(b[i][j]),end=" ")
    print()
    
#14. Write a Python function to check whether a string is a pangram or not.
    #pangram is  word which  containing every letter of the alphabet at least once
alphabet="abcdefghijklmnopqrstuvwxyz" #string with all alphabets
string_in=input("enter string")
#function check every letter of the alphabet at least once.
def string_pangram(string):
    for i in alphabet:
        if i not in string.lower():
            return False
    return True
if string_pangram(string_in)==True:
    print("string is pangram")
else:
    print("string is not  pangram")

#15. Write a Python program that accepts a hyphen-separated sequence of words as input and prints the words
# in a hyphen-separated sequence after sorting them alphabetically.  
#white-red-green-blue,  o/p:blue-green-red-white
string=input("enter words")

def word_sort(string):
    list1=string.split('-') #split string at each hypen and save as list string1
    list1=sorted(list1) #sort list
    return list1

print("words after sorting ")
string_sorted=word_sort(string) # function call
print('-'.join(string_sorted)) # join list elements with hypen

#16. Write a Python function to create and print a list where the values are square of numbers between 1 and 30
# (both included)
def list_square():
    list1=[i*i for i in range(1,31) ]
    return list1
print("created list",list_square())
   

#17.  Write a Python program to access a function inside a function.
array=[1,2,3,4,5]
def sum_square(array):
    sum=0
    for i in array:
        sum=sum+square(i)
    return sum

def square(x):
    return x*x
s=sum_square(array)
print("sum of square array elements=",s)

#18.Write a Python program to detect the number of local variables declared in a function
def abc():
    x = 1
    y = 2
    str1= "w3resource"
    z=3.4
    print("Python Exercises")

print(abc.__code__.co_nlocals)
