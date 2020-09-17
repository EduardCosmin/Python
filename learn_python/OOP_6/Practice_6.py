#Problem 1

#Fill in the Line class methods to accept coordinates 
#as a pair of tuples and return the slope and distance of the line.

# EXAMPLE OUTPUT
#coordinate1 = (3,2)
#coordinate2 = (8,10)
#li = Line(coordinate1,coordinate2)
#li.distance()   #Output: 9.433981132056603
#li.slope()  Output: 1.6

#formula for slope: slope = (y2-y1)/(x2-x1)
#formula for distance: distance = sqrt((x2-x1)**2+(y2-y1)**2)
class Line():
    
    def __init__(self,coor1,coor2):
        self.coor1 = coor1
        self.coor2 = coor2
    
    def distance(self):
        x1,y1 = self.coor1
        x2,y2 = self.coor2
        n = ((x2-x1)**2+(y2-y1)**2)**0.5
        return n
    
    def slope(self):
        x1,y1 = self.coor1
        x2,y2 = self.coor2
        m = (y2-y1)/(x2-x1)
        return m
coordinate1=(3,2)
coordinate2=(8,10)
li=Line(coordinate1, coordinate2)
print("The distance of a line based on the coordinates (3,2) and (8,10) is:")
print(li.distance())
print("The slope of a line based on the coordinates (3,2) and (8,10) is:")
print(li.slope())
print('\n')

#Problem 2
#Fill in the class

# EXAMPLE OUTPUT
#c = Cylinder(2,3)
#c.volume()      #Output: 56.52
#c.surface_area()    #Output: 94.2

#formula for the volume of a cylinder: pi*radius**2*height
#formula for surface_area of a cylinder: (2*pi*radius**2)+2*pi*radius*height
class Cylinder():

    pi=3.14

    def __init__(self,height=1,radius=1):
        self.height = height
        self.radius = radius
        
    def volume(self):
        return self.pi*self.radius**2*self.height
    
    def surface_area(self):
        return (2*self.pi*self.radius**2)+2*self.pi*self.radius*self.height
c=Cylinder(2,3)
print("The volume of the cylinder based on height=2 and radius=3 is:")
print(c.volume())
print("The total surface area of the cylinder based on height=2 and radius=3 is:")
print(c.surface_area())