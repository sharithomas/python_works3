# -*- coding: utf-8 -*-
"""
Created on Mon Apr 20 16:03:03 2020

@author: I325377
"""

#Class programs
#1. create a calss and object
class Myclass:
    x=5
    
p1=Myclass()
print(p1.x)

#2.create init function
class Person:
    def __init__(self,name,age):
        self.name1=name
        self.age1=age
        
p1=Person("john",30)
print(p1.age1)
print(p1.name1)

#3.object methods
#The self parameter is a reference to the current instance of the class, and is used to access variables that belong to the class.
class Person:
    def __init__(self,name,age):
        self.name1=name
        self.age1=age
    def myfunc(self):
        print("my name is ",self.name1)
        
p1=Person("john",30)
print(p1.age1)
print(p1.name1)
p1.myfunc()

#4.The self parameter is a reference to the current instance of the class, and is used to access variables that belongs to the class.
#It does not have to be named self , you can call it whatever you like, but it has to be the first parameter of any function in the class:
class Person:
    def __init__(myinstance,name,age): #myinstance instead of self
        myinstance.name1=name
        myinstance.age1=age
    def myfunc(myinstance):
        print("my name is ",myinstance.name1)
        
p1=Person("john",30)
print(p1.age1)
p1.age1=40 #modify an object property age1
print("after modifying age is ",p1.age1)
del p1.age1 #delete an object property
print("after deleting age",p1.age1)
print(p1.name1)
p1.myfunc()
del p1 #delete an object

#5.Write a Python class to find validity of a string of parentheses, '(', ')', '{', '}', '[' and ']. These brackets must be close in the correct order,
# for example "()" and "()[]{}" are valid but "[)", "({[)]" and "{{{" are invalid.
string=input("enter a string of parenthesis")
class Validity:
    def __init__(self):
        self.stack=[]
        self.par={'(':')','[':']','{':'}',}
    def validity_check(self,string):
        for i in string:
            if i in self.par:
                self.stack.append(i)
            elif len(self.stack)!=0 and self.par[self.stack.pop()]!=i:
                return False
        return len(self.stack)==0

v=Validity()   
check=v.validity_check(string)
if check==True:
    print("valid parenthesis")
else:
    print("not valid")
 
#6. Write a Python program to get the class name of an instance in Python.

class Sample:
    print("class created")
    
sample_in=Sample()
print(type(sample_in).__name__) # get name of class ie,Sample

#7. Write a Python class named Circle constructed by a radius and
# two methods which will compute the area and the perimeter of a circle

class Circle:
    pi=3.14
    def  __init__(self,r):
        self.radius=r
    def Area(self):
        self.area=self.pi*self.radius*self.radius
        return self.area

    def Perimeter(self):
        self.p=2*self.pi*self.radius
        return self.p
        

r=int(input("enter radius of a circle"))        
circle=Circle(r)

print("Area of circle:",circle.Area())
print("Perimeter of circle:",circle.Perimeter())
     
#8.Write a Python class named Rectangle constructed by a length and width and a method which will compute the area of a rectangle
class Rectangle:
    def __init__(self,l,w):
        self.length=l
        self.width=w
    def area(self):
        print("Area of rectangle=",2*self.length*self.width)
        
length=int(input("enter length of rectangle"))
width=int(input("enter width of rectangle"))

new_rectangle=Rectangle(length,width)
new_rectangle.area()

#9. Write a Python class which has two methods get_String and print_String. get_String accept a string from the user and
# print_String print the string in upper case
class String:
    def __init__(self):
        pass
    
    def get_string(self):
        string=input("input a string")
        self.string=string
        
    def print_string(self):
        print("string in upper case",self.string.upper())
        
new_class=String()
new_class.get_string()
new_class.print_string()

#10.  Write a Python class to reverse a string word by word
class Reverse:
    string_out=""
    def __init__(self,string):
        self.string_list=string.split(" ") #divide string word by word and save as a list ie,#["hai","am","python"]
    def _reverse(self):
        for i in range(len(self.string_list)-1,-1,-1): # take each word from list from last to 1st word ie, [python,am,hai] 
            self.string_out=self.string_out+" "+self.string_list[i]#make string by concatenating list words in reverse order
        return self.string_out                                      #ie, "python am hai"
string=input("enter a string word by word")
print("original string",string) #"hai am python"
new_class=Reverse(string)
print("output string  word by word reverse: ",new_class._reverse())

#11. Write a Python class to implement pow(x, n)
class Power:
    def __init__(self,x,n):
        self.x=x
        self.n=n
    def power(self):
        return self.x**self.n
x=int(input("enter x:"))
n=int(input("enter n:"))
new_class=Power(x,n)
print("{}^{}=".format(x,n),new_class.power())

