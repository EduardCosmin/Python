#*args and **kwargs

def myfunc(a,b):    #now i am limitted at 2 parameters a and b
    #returns 5% of the sum of a and b
    return sum((a,b))*0.05
print(myfunc(40,60))
#return the result as a tuple

def my_func(*args):     #now i can assign how many parameters as I want
    return sum (args)*0.05
print(my_func(10,20,30,40,50,60,70,80,90,100))
#by convention is *args from arguments, but you can choose after the '*' whatever you want
#it works as same with *num for example

def my_funcion(*args):
    for item in args:
        print(item)
my_func(10,20,30,40,50,60,70,80,90)

#**kwargs return back a dictionary
def my_function(**kwargs):
    print(kwargs)   #just to see how it looks like
    if 'fruit' in kwargs:
        print("My fruit of choice is {}.".format(kwargs['fruit']))
    else:
        print('No fruits')
print(my_function(fruit='apple', veggie='lettuce'))
#**kwargs is set by default, you can use whatever notation that you want
#**dict is good as well for example

#We can use both *args and **kwargs
def myfunction(*args,**kwargs):     #when we will gave values we need to respect the order of args and kwargs
    print(args)    #just to see how it looks like
    print(kwargs) #just to see how it looks like
    print('I would like {} {}.'.format(args[0],kwargs['food']))
print(myfunction(10,20,30,fruit='orange',food='eggs',animal='dog'))
