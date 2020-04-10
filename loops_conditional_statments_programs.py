# -*- coding: utf-8 -*-
"""
Created on Wed Apr  8 07:49:14 2020

@author: SHARI
"""

#Conditional statments and loops
#1. Write a Python program to find those numbers which are divisible by 7 and multiple of 5, between 1500 and 2700 (both included)

list1=[x for x in range(1500,2700) if x%7==0 and x%5==0]#numbers divisible by 5 and 7
print(list1)

#2.Write a Python program to guess a number between 1 to 9
import random
target_num,guess_num=random.randint(1,10),0
while target_num!=guess_num:
    guess_num=int(input("guess a number between 1 and 10"))
print("well guessed")

#3. Write a Python program to construct the following pattern, using a nested for loop.

* 
* * 
* * * 
* * * * 
* * * * * 
* * * * 
* * * 
* * 
*
n=5
for i in range(1,n):
    for j in range(i):
        print('*', end=" ")
    print("\n")   
for i in range(n,0,-1):
    for j in range(i):
        print("*",end=" ")
    print("\n")
#4. Write a Python program that accepts a word from the user and reverse it
word=input("enter a word")
print("orginal word",word)
print("revesed word",word[::-1])

#5.Write a Python program to count the number of even and odd numbers from a series of numbers.
numbers=tuple(range(1,10))
print("given numbers",numbers)
even=0
odd=0
for i in numbers:
    if i%2==0:
        even=even+1
    else:
        odd=odd+1
print("number of even numbers: ",even)
print("number of odd numbers: ",odd)

#6.Write a Python program that prints each item and its corresponding type from the following list.
 data_list = [1452, 11.23, 1+2j, True, 'w3resource', (0, -1), [5, 12], {"class":'V', "section":'A'}]
 for i in data_list:
     print(i,"   type: ",type(i))
     
#7.Write a Python program that prints all the numbers from 0 to 6 except 3 and 6.
for i in range(0,6):
    if i==3:
        continue
    print(i)
    
#8.Write a Python program to get the Fibonacci series between 0 to 50
    
#function definition to generate fibannoci series
def fib(n):
    a=0
    b=1
    c=0
    while a<=n:
        print(a,end=" ")
        c=a+b
        a=b
        b=c
n=int(input("enter limit"))
fib(n)

#9. Write a Python program which iterates the integers from 1 to 50. For multiples of three print "Fizz" instead of the number 
#and for the multiples of five print "Buzz". For numbers which are multiples of both three and five print "FizzBuzz".

i=1
while i<=50:
    if i%3==0 and i%5==0:
        print("FizzBuzz")
    elif i%5==0:
        print("Buzz")
    elif i%3==0:
        print("Fizz")
    else:
        print(i)
    i=i+1
    
#10.Write a Python program which takes two digits m (row) and n (column) as input and generates a two-dimensional array. 
#The element value in the i-th row and j-th column of the array should be i*j
import numpy as np
row=int(input("enter number of rows"))
col=int(input("enter number of columns"))
a=np.zeros((row,col)) # create a matrix given with number of rows and columns

for i in range(row):
    for j in range(col):
        a[i][j]=i*j #each matrix element set as product row and column indexes
print(a)    

#11.Write a Python program that accepts a sequence of lines (blank line to terminate) 
#as input and prints the lines as output (all characters in lower case)
line=[]
# loop to accept the given datas and append it to a list line
while True:
    l=input()
    if l:
        line.append(l.lower())
    else:
        break
print("given lines: ")   
#print the list elements line by line
for i in line:
    print(i)

#12.Write a Python program that accepts a string and calculate the number of digits and letters
string1=input("enter string")
digit=letter=0
# take each character of string and count letters and digits
for i in string1:
    if i.isalpha():
        letter=letter+1
    elif i.isdigit():
        digit=digit+1
    else:
        pass
print("total letters=",letter)
print("total digits=",digit)

#13.Write a Python program to check the validity of password input by users.
#Validation :
#1.At least 1 letter between [a-z] and 1 letter between [A-Z].
#2.At least 1 number between [0-9].
#3.At least 1 character from [$#@].
#4.Minimum length 6 characters.
#5.Maximum length 16 characters.
password=input("enter password")
length=0
flag=0
special_ch=['$','#','@']
# function definition to check validty of each character of given password
def validity(ch):
    if ch.isdigit():
        flag=1
    elif ch.isalpha():
        flag=1
    elif ch in special_ch:
        flag=1
    else:
        flag=0
    return flag

pass_len=len(password)
validity_list=[]
if (pass_len>=6) and (pass_len<=16):  #check length of password 
    length=1
    
for i in password: # reading each character of password and save value 1 in validty_list if that character is valid else save 0
   validity_list.append(validity(i))
if 0 not in validity_list:
    print("valid password")
else:
    print("Invalid password")

#14.Write a Python program to print alphabet pattern 'A'
  ***                                                                   
 *   *                                                                  
 *   *                                                                  
 *****                                                                  
 *   *                                                                  
 *   *                                                                  
 *   *



result_str=""   
for row in range(7):
    for col in range(7):
        if (((col ==1  or col == 5) and row != 0) or ((row == 0 or row == 3) and (col > 1 and col < 5))):
            result_str=result_str+"*" 
        else:
            result_str=result_str+" " 
    result_str=result_str+"\n" 
print(result_str)
            
#15. Write a Python program to print alphabet pattern 'D'
 ****                                                                  
 *   *                                                                  
 *   *                                                                  
 *   *                                                                  
 *   *                                                                  
 *   *                                                                  
 ****  
cha_D=""
for row in range(7):
     for col in range(5):
         if (col==0 or (col==4 and (row!=0 and row!=6))) or ((row==0 or row ==6) and col!=4):
            cha_D=cha_D+"*"
         else:
            cha_D=cha_D+" "
     cha_D=cha_D+"\n"
print(cha_D)

#16.Write a Python program to print alphabet pattern 'E'
 *****                                                                  
 *                                                                      
 *                                                                      
 ****                                                                   
 *                                                                      
 *                                                                      
 *****
cha_E=""
for row in range(7):
    for col in range(5):
        if (row==0 or (row==3 and col!=4) or row==6) or col==0:
            cha_E=cha_E+"*"
        else:
            cha_E=cha_E+" "
    cha_E=cha_E+"\n"
print(cha_E)
            
#17.  Write a Python program to print alphabet pattern 'G'
  ***                                                                   
 *   *                                                                  
 *                                                                      
 * ***                                                                  
 *   *                                                                  
 *   *                                                                  
  *** 
cha_G=""
for row in range(7):
    for col in range(5):
        if ((col==0 or (col==4 and row!=2))and row!=0 and row!=6) or ((row==0 or row==6) and col!=0 and col!=4) or (row==3 and col!=1) :
            cha_G=cha_G+"*"
        else:
            cha_G=cha_G+" "
    cha_G=cha_G+"\n"
print(cha_G)

#18. Write a Python program to print alphabet pattern 'L'
 *                                                                      
 *                                                                      
 *                                                                      
 *                                                                      
 *                                                                      
 *                                                                      
 *****
cha_L=""
for row in range(7):
    for col in range(5):
        if col==0 or row==6:
            cha_L=cha_L+"*"
        else:
            cha_L=cha_L+" "
    cha_L=cha_L+"\n"
print(cha_L)
            
#18.Write a Python program to print alphabet pattern 'M'

                                                               
  *       *                                                             
  * *   * *                                                             
  *   *   *                                                             
  *       *                                                             
  *       *                                                             
  *       *
cha_M=""
for row in range(7):
    for col in range(5):
        if ((col==0 or col==4) and row!=0) or (row==2 and col!=2) or (row==3 and col!=1 and col!=3):
            cha_M=cha_M+"*"
        else:
            cha_M=cha_M+" "
    cha_M=cha_M+"\n"
print(cha_M)
  
#19.Write a Python program to calculate a dog's age in dog's years. Go to the editor
#Note: For the first two years, a dog year is equal to 10.5 human years. After that, each dog year equals 4 human years.
human_year=int(input("input dog's age in human years"))
dog_year=0

for i in range(1,human_year+1):
    if i==1 or i==2:
        dog_year=dog_year+10.5
    else:
        dog_year=dog_year+4

print("dog's age in dog's year=", dog_year)         

#20.Write a Python program to construct the following pattern, using a nested loop number.
1
22
333
4444
55555
666666
7777777
88888888
999999999
str1=""
for i in range(1,10):
    for j in range(1,i+1):
        str1=str1+str(i)
    str1=str1+""
    str1=str1+"\n"
print(str1)