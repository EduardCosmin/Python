#Class Objected Attributes

class Dog():
    #Class Object Attribute
    #Same for any instance of a class
    #species = 'mammal' define "a global attribute" which is always True
    #any dog is a mammal for example
    species = 'mammal'  #class object attribute

    def __init__(self, breed, name, spots):
        self.breed = breed
        self.name = name
        self.spots = spots
my_dog=Dog(breed='Lab', name='Sam', spots=False)
print(my_dog.breed, my_dog.name, my_dog.spots)
print(my_dog.species)

#A method is a function inside of a class
#Example of methods

class Cat():
    species='mammal'    #class object attribute
    kingdom='feline'
    def __init__(self, breed, name):
        self.breed = breed  #attribute
        self.name = name    #attribute
    #OPERATIONS/Actions----->Methods
    #Methods can take outside arguments (in our case other than breed, name, etc)
    def meow(self, number): #we call self as a reference 
        print('meow meow!\nMy name is {} and the number is {}.'.format(self.name, number))
my_cat=Cat('Sfinx', 'Sandy')
#Attributes never had open in close parentheses '()' we don't need to execute them 
#ex: my_.breed | don't need '()'
print(my_cat.breed, my_cat.name, my_cat.species, my_cat.kingdom)
print(my_cat.meow)  #shows the location where the method is stored

#When we call a method we need open in close parantheses
print(my_cat.meow(10))    #display the method | '10' it's the number from above


class Circle():
    #Class Object Attribute
    pi = 3.14
    def __init__(self, radius=1):   #we set 1 as a default value for radius
        self.radius = radius
        #We can create other attributes without definding them in first place
        #For example the area of a circle
        #because pi is a class object attribute, insted of using 'self.pi' we can use 'Circle.pi'
        #Circle.pi is a reference to a class object attribute
        #Aria cercului: raza la a doua * pi
        self.area = radius*radius*self.pi    
    #Method
    def get_circumference(self):
        return self.radius * self.pi * 2    #(raza*pi*2)

my_circle=Circle()
print(my_circle.pi)
print(my_circle.radius)
#If we want to overwrite the value of the radius from 1 to 20 for example we can call my_circle=Circle(20)
#Example
# my_circle=Circle(20)
# print('The new value of the radius:')
# print(my_circle.radius)
print(my_circle.get_circumference())    #1*pi*2
print(my_circle.area)
