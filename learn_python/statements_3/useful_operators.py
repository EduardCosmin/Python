#Useful Operators

#Range
for num in range(10):   #from 0 to 9, not including 10
    print(num)
print('')
for num in range(3,10): #start from 3 and go to the 10, but not including 10
    print(num)
print('')
for num in range(0,11,2): #start from 0 and go to the 11, but not including 11 in steps of 2
    print(num)

#List range
print(list(range(0,11,2)))  #print a list which starts from 0 and go to 10 in jumps of 2

#Enumerate
index_count=0
for letter in 'abcde':
    print('At index {} the letter is {}'.format(index_count,letter))
    index_count += 1
#the same block of code, but write different
index_count=0
word='abcde'
for letter in word:
    print(word[index_count])
    index_count += 1

#Now we will use enumerate and rewrite the examples above
word='abcde'
for item in enumerate(word):    #will display each index with each value in tuples
    print(item)
print('\n')
#We can separate tuples by typeing
word='abcde'
for index,letter in enumerate(word):
    print(index)
    print(letter)
    print('\n')

#Zip function
#Zip function is only going to be able to go and zip together as far as the list which is the shortest.
#it will ignore everything that's extra
mylist1=[1,2,3,4,5,6]   #4,5,6 is extra
mylist2=['a','b','b']
mylist3=[100,200,300]
print(zip(mylist1,mylist2)) #it returns the location in your memory where you have this zip generator
print('\n')

for item in zip(mylist1,mylist2,mylist3):
    print(item)
print('\n')

#If we want a list with zip function;
print(list(zip(mylist1,mylist2,mylist3)))

#In operator - check if smth. is somewhere
print('x' in ['x','d','f']) #can be use with characters
print('a' in ['x','d','f'])
print('a' in 'It is a nice world!') #can be use with strings
print('mykey' in {'mykey':345}) #can be use with dictionary

dictionary={'mykey':345}
print(345 in dictionary.keys())    #false
print(345 in dictionary.values())  #true

#Min and Max functions
mylist=[10,20,30,40,100]
print(max(mylist))
print(min(mylist))

#Random library
from random import shuffle  #from the random library import shuffle function
#we can't assign values to shuffle (ex.: num = shuffle(my_list) and then print(num))  | it will return nothing
my_list=[1,2,3,4,5,6,7,8,9,10]
shuffle(my_list)    #will shuffle the items inside the list
print(my_list)

from random import randint
#randint can be assign because will return what we will assign
#randit will display randomly an integer from an interval gave by the user
print(randint(0,100))  

#User input
#user input will always store data as a string and if you need smth else you need to convert that input
result = input('Enter a number here:')
print(type(result))
print('After converting:')
number=int(result) #convert user input into integer
print(type(number))
#number1=float(result)      #convert user input into float

#you can convert a datatype when you ask for the user input:
pi=float(input('What is the value of pi: '))
print(type(pi))