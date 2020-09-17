#Decorators in Python

#Python use decorators that allow you to track on extra functionality to
#an already existing function.
#We use the '@' operator; and we placed on the top of the original function.

#Syntax:
# @some_decorator
# def simple_func():
#   null 

# \t = tab

def hello(name="Jose"):
    print('The hello() function has been executed!')

    #The greet function is dependent to hello() function
    #Can't be executed alone(without hello() function)
    def greet():
        return'\tThis is greet() function inside hello() function!'

    #Same as greet()
    def welcome():
        return'\tThis is welcome inside hello!'

    print(greet())
    print(welcome())
hello()

print('\n')

#This example will show us how to return a function inside another function
def hello_2(name="Jose"):
    print('The hello() function has been executed!')

    def greet():
        return'\tThis is greet() function inside hello() function!'

    def welcome():
        return'\tThis is welcome inside hello!'
    
    print('I am going to return a function1')

    if name == 'Jose':
        return greet
    else:
        return welcome

my_new_func=hello_2('Jose') #because the name is Jose it's returned the greet func
print(my_new_func) # <function hello_2.<locals>.greet at 0x037872B0>

#Now if we call my_new_func() it will return the greet() function
print(my_new_func())

#The welcome() function
#If the name is not Jose it will display the other func which in our case is welcome()
my_new_func2=hello_2('') 
print(my_new_func2())

print('\n')

#Example of decorator - long way:

def new_decorator(original_func):
    def wrap_func():
        print('Some extra code before the original function.')
        original_func()
        print('Some extra code after the original function.')
    return wrap_func

def func_needs_decorator():
    print('I want to be decorated!')

func_needs_decorator() #the function without decoration

decorated_func = new_decorator(func_needs_decorator)
decorated_func()

print('\n')

#Example of decorator - short and better way:

def new_decorator_1(original_func):
    def wrap_func_1():
        print('Some extra code before the original function.')
        original_func()
        print('Some extra code after the original function.')
    return wrap_func_1

@new_decorator  # This syntax passes the func_needs_decorator_1 as the original_func from new_decorator_1
def func_needs_decorator_1():
    print('I want to be decorated!')

func_needs_decorator_1()