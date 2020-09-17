#Formatting with the .format() method

#A good way to format objects into your string for print statements is with the string .format() method.
#Syntax: 'String here {} then also {}'.format('something1','something2').

print('This is a string {}'.format('INSERTED'))     #{} and .format() it will take the string inside the paranthesis of .format() and it will put it in the place of {}
print('The {} {} {}'.format('fox','brown','quick'))     #output: The fox brown quick
                                                        #it will insert the string in order that you gave it for the {}

#If you want to decide the order of what string to be first and second and so on you will need to specify the index of the word in the {}
#Index starts counting with 0

print('The {2} {1} {0}'.format('fox','brown','quick'))      #output: The quick brown fox
#print('The {0} {0} {0}'.format('fox','brown','quick'))      #output: The fox fox fox

#In order to do the things more easier to read it's better if you write keywords for the strings as below
print('The {q} {b} {f}'.format(f='fox',b='brown',q='quick'))


#Float formatting
#Float formatting follows "{value:width.precision f}"
result =100/777
print(result)
print('The result was {}'.format(result))   #the .format() can be use not just as a string
print('The result was {r}'.format(r=result))    #assign r as a keyword 

print('The result was {r:1.3f}'.format(r=result))   #r=value, 1=width, 3f=precision  / width=1 is general(default)
#3f means the 3 characters after the dot(.) of a float. For example if you have '0.123456789', 3f is '.123'
print('The result was {r:1.5f}'.format(r=result))   #output: 0.12870

print('The result was {r:10.3f}'.format(r=result))      #width value will make more space in front of the function

#F-strings
name='Jose'
print(f'Hello, his name is {name}.')    #replace .format() with an 'f' in front of the '' inside the print method

name='Sam'
age='3'
print(f'{name} is {age} years old.')    #multiple inputs