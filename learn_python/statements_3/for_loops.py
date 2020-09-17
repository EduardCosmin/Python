#For loops:

#Syntax
#my_iterable=[1,2,3]
#for item_name in my_iterable:
#    print(item_name)

my_list=[1,2,3,4,5,6,7,8,9,10]
for num in my_list:     #num is just a notation. | jelly, work, or anything else works as same
    print(num)

for jelly in my_list:
    print('Hello')      #will display Hello 10 times

for num in my_list:
    #check for even
    if num %2 == 0:
        print(f'Even number:{num}')
    #odd number
    else:
        print(f'Odd number:{num}')

list_sum=0
for num in my_list:
    list_sum=list_sum + num
    print(list_sum)     #it's shows how the sum work inside a list
print(f'Sum of every element of the list: {list_sum}.')

my_string='Hello world'
for letter in my_string:
    print(letter)
#or you can type
for letter in 'Hello world':
    print(letter)

#Let's say that you don't want to use a notation for your for loop
for _ in 'Santa Claus': # '_' is just a placeholder for smth. that you don't need/want to assign
    print('Present')    #will display 'present' so many times as how many letters has 'Santa Claus'(including spaces) | (for 11 times)

#Tuples
tup=(1,2,3)
for item in tup:
    print(item)

my_list=[(1,2),(3,4),(5,6),(7,8)]   #list of tuples
print(len(tup)) #output: 4, because I have 4 elements, 4 tuples
for item in my_list:
    print(item)     #print out pairs of tuples

#Tuple unpacking - duplicate the structure of the items
for a,b in my_list:   #a,b are placeholders for first and second element of the tuple
    print(a)    #print the first element of the tuple from every tuple
    print(b)    #print the second element of the tuple from every tuple

my_list=[(1,2,3),(5,6,7),(8,9,10)]
for item in my_list:
    print(item)     #print every tuple

for a,b,c in my_list:
    print(a)
    print(b)
    print(c)

#Dictionary
#By default when you iterate through a dictionary you only iterate through the keys 
dictionary={'k1':1,'k2':2,'k3':3}
for item in dictionary:
    print(item)    

for item in dictionary.items():     #will display keys and values as tuple pairs
    print(item) 

#We can do as above at the tuple unpacking to see each element of the dictionary
for key,value in dictionary.items():
    print(f'The key is: {key}.')
    print(f'The value is: {value}.')

#Let's say that you want to print just keys or just values:
#dictionary={'k1':1,'k2':2,'k3':3}
#for key/value in dictionary.key()/.value():
#   print(key/value)

