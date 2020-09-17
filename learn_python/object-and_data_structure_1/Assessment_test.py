#Test your knowlegdes

#Write a brief description of all the following Object Types and Data Structures we've learned about:
#Numbers: are characters from 0 to 9(integers) or could be float
#Strings: ordered sequences of characters
#Lists:   ordered sequences of objects (muttable)
#Tuples:   ordered sequences of objects (immutable)
#Dictionaries:  are a set of values that have a set of keys for each value 

#Write an equation that uses multiplication, division, an exponent, addition, and subtraction that is equal to 100.25.
#print((2**3*9)/0.5+6-49.75)

#What is the value of the expression 4 * (6 + 5)
#44

#What is the value of the expression 4 * 6 + 5 
#29

#What is the value of the expression 4 + 6 * 5 
#34

#What is the type of the result of the expression 3 + 1.5 + 4?
#float

#What would you use to find a number’s square root, as well as its square?
# Square root: 100**0.5 = 10.0  | something at **0.5 is the square root to any number

# Square: 10**2 = 100

#Given the string 'hello' give an index command that returns 'e'.
#s = 'hello'
#print(s[1])

#Reverse the string 'hello' using slicing:
#s ='hello'
#print(s[::-1])

#Given the string hello, give two methods of producing the letter 'o' using indexing.
#s ='hello'
# Print out the 'o'​
# Method 1:print(s[4])

# Method 2:print(s[-1])

#Build this list [0,0,0] two separate ways.
# Method 1:my_list=[0,0,0]

# Method 2:my_list=3*[0]

#Reassign 'hello' in this nested list to say 'goodbye' instead:
#list3 = [1,2,[3,4,'hello']]
#list3[2][2]='goodbay'          #first [2] is the index of the second list and then the second [2] is the index of 'hello

#Sort the list below:
#list4 = [5,3,4,6,1]
#print(list4.sort())
#print(sorted(list4))          #another method to sort a list

#Using keys and indexing, grab the 'hello' from the following dictionaries:
#d = {'simple_key':'hello'}
# Grab 'hello'
#print(d['simple_key'])

#d = {'k1':{'k2':'hello'}}
# Grab 'hello'
#print(d['k1']['k2'])

## Getting a little tricker
#d = {'k1':[{'nest_key':['this is deep',['hello']]}]}
#Grab hello
#print(d['k1'][0]['nest_key'][1][0])   
#d=dictionary, k1=first key value, 0=the index of the first elem from the list, nest_key=the first keyvalue from the second dictionary, 1=index of the list 0=index of the hello item

# This will be hard and annoying! Grab hello
#d = {'k1':[1,2,{'k2':['this is tricky',{'tough':[1,2,['hello']]}]}]}
#print(d['k1'][2]['k2'][1]['tough'][2][0])

#Can you sort a dictionary? Why or why not?
#You cannot sort a dictionary because normal dictionary are mappings not sequences

#What is the major difference between tuples and lists?
#Tuples are immutable, you cannot change an item once it's inside a tuple

#How do you create a tuple?
#We can create a tuple by assigning some characters inside round brackets like a=(1,2,3)

#What is unique about a set?
#A set can contain just uniques value. A set cannot contain duplicates.

#Use a set to find the unique values of the list below:
#list5 = [1,2,2,33,4,4,11,22,3,3,2]
#print(set(list5))

#What will be the resulting Boolean of the following pieces of code:
#2>3        False
#3<=2       False
#3==2.0     False
#3.0==3     True
#4**0.5!=2  False

#What is the boolean output of the cell block below?
#l_one = [1,2,[3,4]]
#l_two = [1,2,{'k1':4}]

# True or False?
#l_one[2][0] >= l_two[2]['k1']  
#3>=4   False

