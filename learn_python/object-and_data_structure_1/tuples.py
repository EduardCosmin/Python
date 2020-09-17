#Tuples

#Tuples are very similar to lists. However they have one key difference - immutability.
#Once an element is inside a tuple, it cannot be reassigned.
#Tuples use parenthesis: (1,2,3)

t=(1,2,3)               #tuple
mylist=[1,2,3]          #list
print(type(t))      
print(type(mylist))
#Inside a tuple you can have more types of datatype like integer, string and so on.
#You can slice inside a tuple

t=('one',2,'three')
print(t[0])             #output: one
print(t[-2])            #output:2
print(t[1:])            #output:2, three

t=('a','a','b','a','b','c','c','v')
#Count how many times an item is in a tuple
print(t.count('a'))
#How to see the index of an item inside a tuple
print(t.index('a'))   #output:0  | display the first position of 'a' as index

