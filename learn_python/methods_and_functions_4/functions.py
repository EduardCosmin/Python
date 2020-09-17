#Functions

#Functions allow us to create blocks of code that can be easily executed
#many times, without needing to constantly rewrite the entire block of code.
#A function can take parameters!

#Syntax:
#def name_of_function(): or def name_of_function(name):
#   '''
#   Docstring explains functions.
#   '''
#   print('Hello') or print('Hello' + name)
#To execute the function created above we need to call her by his name.

#Typically we use the return keyword to send back the result of the function,
#instead of just printing it out.
#RETURN allows us to assign the output of the function to a new variable.
#Example:
#def add_function(num1,num2):
#   return num1+num2
#Now we can assign the function a variable (ex: result=add_function(1,2))
#print(result)  Output:3

def name_function():
    print('Hello')
name_function()     #we call the function and it's outputting 'Hello'

#We can add docstrings for a better reading like below.
#Most of the time we will not use docstring, but can be very useful when ou work in a team
#If we will type: print(help(name)) we will see in terminal what kind of function we have
def name():
    '''
    DOCSTRING: Information about the function
    INPUT:  no input...
    OUTPUT: Hello
    '''
    print('Bogdan')
name()

#Hello function
def say_hello(name):
    print('Hello '+name+'.')
say_hello('Bogdan')

#Greeting function
def greeting(name):
    print('Hello %s' %(name))
greeting('Alba-ca-Zapada.')

#Return keyword
def hello(name):
    return 'Hello ' + name +'.'
result=hello('Diana')
print(result)

#Addition with return keyword
def add(n1,n2):
    return n1+n2
result=add(2,3)
print(result)

#Find out if the word 'dog' is in a string?
def dog_check(my_string):
    return 'dog' in my_string.lower() #.lower() will lowercase all the string for a precise check (even if the 'dog' is in capital ('Dog'))

print(dog_check('I see a dog under the table.'))
print(dog_check('Dog ran away.'))
print(dog_check('I love cats.'))

#Pig Latin (vowel=vocala)
#If words starts with a vowel, add 'ay' to end
#If words does not start with a vowel, put first letter at the end, then add 'ay'
#word--> ordway
#apple-->appleay

def pig_latin(word):
    first_letter = word[0]
    #check if vowel
    if first_letter in 'aeiou':
        pig_word= word + 'ay'
    else:
        pig_word= word[1:]+first_letter+'ay'
    return pig_word

print(pig_latin('word'))
print(pig_latin('apple'))

#Check if a number is prime (if it's divided only by 1 and himself)
import math
def is_prime(num):
    '''
    Check if a number is prime or not
    '''
    if num %2==0 and num>2:
        return num, ' is not prime.'
    for i in range(3,int(math.sqrt(num))+1,2):
        if num %i==0:
            return num, ' is not prime.'
    return num, ' is prime.'
print(is_prime(17))
print(is_prime(6))

#Simple way to check if a number is prime or not
def is_prime2(num):
    '''
    Naive method of checking for primes. 
    '''
    for n in range(2,num):
        if num % n == 0:
            print(num,'is not prime')
            break
    else: # If never mod zero, then prime
        print(num,'is prime!')
print(is_prime2(17))
print(is_prime2(6))