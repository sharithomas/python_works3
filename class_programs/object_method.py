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
