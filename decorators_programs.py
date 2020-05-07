# -*- coding: utf-8 -*-
"""
Created on Mon Mar  9 14:36:54 2020

@author: SHARI
"""

#Decorators

#1.example
def first(msg):
    print(msg)    

first("Hello")

second = first
second("Hello")

#2.example
def hello_decorator(func): 
  
    # inner1 is a Wrapper function in  which the argument is called   
    # inner function can access the outer local functions like in this case "func" 
    def inner1(): 
        print("Hello, this is before function execution") 
        # calling the actual function now inside the wrapper function. 
        func() 
  
        print("This is after function execution") 
          
    return inner1 
   
# defining a function, to be called inside wrapper 
def function_to_be_used(): 
    print("This is inside the function !!") 
  
function_to_be_used = hello_decorator(function_to_be_used) 
  #function call
function_to_be_used() 