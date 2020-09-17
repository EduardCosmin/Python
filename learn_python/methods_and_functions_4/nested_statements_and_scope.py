#Nested Statements and Scope

x=25
def printer():
    x=50
    return x
print(x)    #output:25
print(printer())    #output:50

#LEGB Rules:
#L: Local - Names assigned in any way within a function (def or lambda), and not declared global in that function.
#E: Enclosing function locals - Names in the local scope of any and all enclosing functions(def or lambda), from inner to outer.
#G: Global(module) - Names assigned at the top-level of a module file, or declared global in a def within the file.
#B: Built-in(Python) - Names preassigned in the build-in names module: open, range, SyntaxError,...

#Example of Local
lambda num:num**2

#Example enclosing function locals
#global
name='This is a global string'
def greet():
    #enclosing
    name='Sammy'    #overwrite the name variable
    def hello():
        #local
        name='Bogdan'   #overwrite again the variable name
        print('Hello, '+name+'!')
    hello()
greet() #when we calling greet we will display Hello Sammy!

#Example of global(module):
x=50
def func(x):
    print(f'X is {x}')
    #Local reassignment
    x=200   #this reassignment works just inside this function, otherwise x=50
    print(f'I locally changed x to {x}')
print(func(x))
print(x)
print('\n')

#Another example using global keyword:
x=20
def func2():
    global x    #global keyword
    print(f'X is {x}')
    #Local reassignment on a global variable
    x='New Value'   
    print(f'I locally changed x to {x}')
print(x)    #output: x=20
print(func2())  #output: I locally changed x to New Value
print(x)    #output: New Value
print('\n')

#For a better way to do the same thing as above we can do:
x=30
def func3(x):
    print(f'X is {x}')
    #Local reassignment on a global variable
    x='New Value'   
    print(f'I locally changed x to {x}')
    return x
print(x)    #output: x=30
x=func3(x)  #make x a global keyword
print(x)  #output: x is 30/I locally changed x to New Value/New Value


