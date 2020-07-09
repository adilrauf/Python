#                   Assignment-06 and Task 01
#                     Author: ADIL RAUF
#
# Write a Python class named Circle constructed by a radius attribute and two
# methods which will compute the area and the perimeter of a circle:
# ● The radius attribute should be passed in the class constructor.
# ● The radius attribute should be private while the methods should be public.

# IMPORTING MATH LIBRARY
import math

# DEFINING CLASS
class Circle:
  def __init__(self, Radius):           #  This Constructor is PRIVATE
    self.Radius = Radius

  def Perimeter(self):                  # This method is PUBLIC
    print("Perimeter of the Circle is : ", round(2 * math.pi * self.Radius,2))
    # Perimeter = PI x 2R
  def Area(self):                       # This method is PUBLIC
    print("Area of the Circle is : ", round(math.pi * (pow(2*self.Radius, 2))/4))
    #  Area = PI x (2R)^2/4

# INPUT
Input_Radius = int(input("Enter the radius :"))

# RADIUS ATTRIBUTE PASSING TO THE CLASS CONSTRUCTOR
p1 = Circle(Input_Radius)

# OUTPUT
p1.Perimeter()
p1.Area()
print("Radius of the Circle : ", p1.Radius)




