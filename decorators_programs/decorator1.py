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
