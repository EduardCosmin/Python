#String properties and Methods

#Immutability of strings
name='Sam'
print(name)
#name[0]='P'     #you try to change the first character (S) to P, but it will result an error
                 #output error: 'str' object does not support item assignment

#Concatenation

last_letters=name[1:]   #slice function to grab the last two letters
print(last_letters)     #display the slicing
change_name= 'P' + last_letters     #assign 'P' in front of the last letters
print(change_name)      #display the result

x='Hello World'
print(x)
y = x + ", it's beautiful outside."
print(y)

letter ='z'
letter = letter * 10     #multiply the letter by 10 (zzzzzzzzzz) 
print(letter)
print(len(letter))       #print the length of 'letter' (10)

a='2'
b='3'
print(a+b)               #will concatenate(not addition) because a and b are strings (23)

x='Hello World'
print(x.upper())         #x.upper is a function that transform a string from normal case to uppercase
print(x.lower())         #x.lower is a function that transform a string from normal case to lowercase
print(x.split())         #x.split it will create a list off of a string: ['Hello', 'World']

x='Hi, this is a string'
print(x.split('i'))      #it will split off of a list, but it will erase the 'i' from the string    
