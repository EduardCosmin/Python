#List comprehensions

#List comprehensions are a unique way of quickly creating a list with Python.
#If you find yourself using a for loop along with .append() to create a list, list comprehensions are a good alternative.

#Let's create a empty list and we will add items inside of it from a string
mystring='hello'
my_list=[]
for letter in mystring:
    my_list.append(letter)  #will add every character from mystring inside of my_list with .append()
print(my_list)

#The same output in less code with list comprehension
mylist=[letter for letter in mystring]
print(mylist)

#Another example
my_list =[x for x in 'word']    #x is just a placeholder, you can choose whatever you want
print(my_list)

#Another example
my_list=[dfdf for dfdf in 'hghy']
print(my_list)

#Works with other functions as range for example
my_list=[num for num in range(0,11)]
print(my_list)

#If I want to perform operation, for example to grab the square of every number in a specific range:
my_list=[num**2 for num in range(0,11)]
print(my_list)

#You can add statements as if:
my_list=[x for x in range(0,11) if x%2==0]  #grab the even numbers inside a range
print(my_list)
#Grab the square of even number in a range
my_list=[x**2 for x in range(0,11) if x%2==0 ]
print(my_list)

#Complex operations (convert celsius to fahrenheit)
celsius=[0,10,20,34,5]
fahrenheit=[((9/5)*temp +32) for temp in celsius]
print(fahrenheit)

#Same example as above with for loop:
celsius=[0,10,20,34,5]
fahrenheit =[]
for temp in celsius:
    fahrenheit.append(((9/5)*temp +32))
print(fahrenheit)

#You can use if else statement in list comprehensions, BUT is hard to read :
results=[x if x%2==0 else 'ODD' for x in range(0,11)]
print(results)

#Nested loops in list comprehensions:
my_list=[]
for x in[2,4,6]:
    for y in [100,200,300]:
        my_list.append(x*y) #will add to my_list the multiplication of every combination between elements of both lists (x and y)
print(my_list)

#The same example with list comprehension, BUT is hard to read
my_list=[x*y for x in [2,4,6] for y in [100,200,300]]
print(my_list)