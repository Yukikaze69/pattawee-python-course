"""
Write a Python class Rectangle with:

Private attributes for length and width
Methods to calculate area (getArea()) and perimeter getPerimeter())
A method to check if it's a square (isSquare())

"""
class Rectangle:
     def __init__(self, lenght,widht):
          self___lenght = lenght
          self___widht = widht
     def getarea(self):
         return f "area of{self.___widht} widht and {self.___lenght} lenght= {self.___widht * self.___lenght}"
     def getpreimeter(self):
         return f "preimeter of {self.___widht}widht and {self.___lenght} lenght= {2 * (self.___widht + self.___lenght )} "      
     def issquare(self):
          return self.___widht == self.___lenght
myRectangle = Rectangle(5,10)
myRectangle.__lenght = -5

print(myRectangle.getarea())