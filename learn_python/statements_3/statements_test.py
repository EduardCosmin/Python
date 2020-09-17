#Statements Assessment Test

#1.Use for, .split(), and if to create a Statement that will print out words that start with 's':
st = 'Sam, print only the words that start with s in this sentence'
#For method nr 1:
my_split=st.split()
for word in my_split:
    if word.startswith('s') or word.startswith('S'):    #works for both capital and lowercase letters
        print(word)
#For method nr. 2:
for word in my_split:s
    if word[0]=='s' or word[0]=='S':    #for both capital and lowercase letter 's/S'
        print(word)
#For method nr.3
for word in my_split:
    if word[0].lower() =='s':       #.lower() will lowercase all the string for a precise check (even if the 'S' is in capitals)
        print(word)

#List comprehension method
my_word=[word  for word in my_split if (word.startswith('s'))]  #will check just for 's' in lowercase
print(my_word)

#2.Use range() to print all the even numbers from 0 to 10.
#For method nr 1:
for num in range(0,11):
    if num %2==0:
        print(f'Even numbers between 0 and 10:\n{num}')
#For method nr. 2:
for num in range(0,11,2):   #will take numbers from 0 to 10 in jumps of 2
    print(num)

#List comprehension method
my_list=[num for num in range(0,11) if num %2==0]
print(my_list)

#3.Use a List Comprehension to create a list of all numbers between 1 and 50 that are divisible by 3.
#List comprehension method
my_list=[num for num in range(1,51) if num %3==0]   #if num % 3 == 0 *This is saying, if my number(num) is divisible by 3 leaving a 0 remainder
print(my_list)
#For method
for num in range(1,51):
    if num %3==0:
        print(num)

#4.Go through the string below and if the length of a word is even print "even!"
st = 'Print every word in this sentence that has an even number of letters'
#List comprehension method
my_split=st.split()     #separate words from the string
my_string=[word for word in my_split if len(word) %2==0]
print('The following list is filled with even words:')
print(my_string)
#For method
for word in my_split:
    if len(word) %2==0:
        print(word+ ' is even')   #will print 'even' for each time a word will have an even number of characters


#5.Write a program that prints the integers from 1 to 100. But for multiples of three print "Fizz" instead of 
#the number, and for the multiples of five print "Buzz". For numbers which are multiples of both three and 
#five print "FizzBuzz".
for num in range(1,101):
    if num % 3 == 0 and num % 5 == 0:
        print("fizzbuzz")
        continue
    elif num % 3 == 0:
        print("fizz")
        continue
    elif num % 5 == 0:
        print("buzz")
        continue
    print(num)      #print the rest of the numbers which are not divisible with 3 and 5


#6.Use List Comprehension to create a list of the first letters of every word in the string below:
#List comprehension method
st = 'Create a list of the first letters of every word in this string'
my_list=[word[0] for word in st.split()]
print(my_list)
#For method - doesn't work properly
# my_list=[]
# my_split=st.split()
# for letter in my_split:
#     my_list.append(letter[0])
#     print(my_list)