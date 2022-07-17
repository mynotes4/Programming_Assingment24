"""
Question3
Your task is to create a Circle constructor that creates a circle with a radius provided by an
rgument. The circles constructed must have two getters getArea() (PIr^2) and getPerimeter()
(2PI*r) which give both respective areas and perimeter (circumference).
For help with this class, I have provided you with a Rectangle constructor which you can use
as a base example.
Examples
circy = Circle(11)
circy.getArea()
# Should return 380.132711084365
circy = Circle(4.44)
circy.getPerimeter()
# Should return 27.897342763877365
Notes
Round results up to the nearest integer.
"""

from math import pi
class Circle():

    def __init__(self,r):
        self.r = r

    def getArea(self):
        return int(round(pi*self.r*self.r,0))

    def getPerimeter(self):
        return int(round(2*pi*self.r,0))

c = float(input("Enter Radius "))
circy = Circle(c)
print("Area",circy.getArea())
print("Perimeter",circy.getPerimeter())