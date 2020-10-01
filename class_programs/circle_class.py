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
     
