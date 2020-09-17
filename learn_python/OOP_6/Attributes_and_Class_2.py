#Attributes and Class

#The simple class 
def Sample():
    pass

#Another example of a class
#my_sample = Sample()
#print(type(my_sample))

class Dog():
    def __init__(self, breed):
        self.breed = breed
my_dog = Dog(breed='Lab')
print(type(my_dog))
print(my_dog.breed)

#The class above but in some other way
class Cat():
    def __init__(self,mybreed):     #mybreed is just a parameter name
        #Attributes
        #We take in the argument
        #Assign mybreed to self.attribute_name (self.breed)
        self.breed = mybreed    #breed play as an attribute (ex: self.my_attribute = mybreed)
my_cat=Cat(mybreed='Sfinx')
print(type(my_cat))
print(my_cat.breed)

#Another example more explicitly
class Pig():
    def __init__(self, color):
        self.my_attribute_color = color
my_color = Pig(color='Pink')
print("Below we print the attribute(my_attribute_color) with the specific parametre(color).")
print(my_color.my_attribute_color)

#Let's make a class a bit more complex:

class Human():
    def __init__(self, color, nationality, age, sick):
        self.color = color
        self.nationality = nationality
        #Expect integer / float
        self.age = age
        #Expect boolean True / False
        self.sick = sick
# my_human = Human(color='white', nationality='Romanian', age=23, sick=False)       #Output: white Romanian 23 False
my_human = Human(color='white', nationality='Romanian', age='23', sick='False')     #I put age and sick as strings to use .join method
result = (my_human.color, my_human.nationality, my_human.age, my_human.sick)        #It works as well with age as int and sick as boolean, but .join doesn't work that way
hyphen = " - ".join(result)
print(hyphen)
