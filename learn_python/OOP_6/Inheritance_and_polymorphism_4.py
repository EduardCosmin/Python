#Inheritance and polymorphism

#Inheritance
class Animal():
    def __init__(self):
        print('Animal Created')
    def who_am_i(self):
        print('I am an animal')
    def eat(self):
        print('I am eating')
my_animal = Animal()  #this is an instance of the class Animal
my_animal.eat()
my_animal.who_am_i()

class Dog(Animal):      #class Dog is a derived class from the Animal class in our case
    def __init__(self):
        Animal.__init__(self)   #instance of the Animal class
        print('Dog Created')
    #We can overwrite methods from the main class
    #Example: let's say that we want to overwrite who_am_i method
    def who_am_i(self):
        print('I am a dog')
    #We can add new methods
    def bark(self):
        print('Woof!')
my_dog = Dog()  #Output: Animal Created | Dog Created - inherited class and current class
#Because we inherit the class animal we are able to use in our Dog class both who_am_i and eat methods
my_dog.eat()
my_dog.who_am_i()
my_dog.bark()

#Polymorphism
#Refers to the way in which different object classes can share the same method name
#In our example we have two different classes with the same method name called 'speak'

class Dog():
    def __init__(self, name):
        self.name =  name
    def speak(self):    #here
        return self.name + ' says woof!'

class Cat():
    def __init__(self, name):
        self.name =  name
    def speak(self):    #here
        return self.name + ' says meow!'

niko = Dog('niko')
felix = Cat('felix')
print(niko.speak())
print(felix.speak())

#We can iterate through this methods
for pet in [niko,felix]:
    print(type(pet))
    print(pet.speak())
print('\n')

#Another way to go through methods is with a function
def pet_speak(pet):
    print(pet.speak())
pet_speak(niko)
pet_speak(felix)

#Abstract method
class Animal():
    def __init__(self, name):
        self.name  = name
    def speak(self):
        raise NotImplementedError("Subclass must implement this abstract method")

#Now we create a class to inherit the Animal abstract class
class Dog(Animal):
    def speak(self):
        return self.name+' says woof!'
class Cat(Animal):
    def speak(self):
        return self.name+' says meow!'
fido = Dog('fido')
stella = Cat('stella')
print(fido.speak())
print(stella.speak())

#Use of polymorphism 
#For example if we want to create some classes for opening files 
#1. We create a class for opening files (called: OpenFile for example)
#2. We create one class for each type of file that we want to open and inherit the OpenFile class (ex: class Pdf, Txt, etc)
#       -one class for PDF
#       -one class for txt file
#       -etc
# => we want to be able to share the same method name 