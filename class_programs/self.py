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
