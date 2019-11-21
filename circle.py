import math

class Circle:
    
    def __init__(self,radius):
        self.radius = radius
        
    def perimeter(self):
        peri = 2 * math.pi * self.radius
        return(peri)
        
    def area(self):
        ar = math.pi * self.radius ** 2
        return(ar)
        

##### TEST #####
        
radius = int(input('Enter the radius : '))
circle1 = Circle(radius)
print("The perimeter is " + str(circle1.perimeter()))     
print("The area is " + str(circle1.area()))   
        
        
        