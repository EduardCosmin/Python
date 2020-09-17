#Dictionaries
#Syntax: {'key1':'value1','key2':'value2'}

#Dictionaries are objects that can be retrieved by the key name. Are unordered and cannot be stored
#vs
#Lists are objects retrieved by location. Are ordered sequence that can be indexed or sliced

my_dict={'key1':'value1','key2':'value2'}
print(my_dict)
print(my_dict['key1'])      #output:value1

prices_lookup={'apple':2.99,'oranges':1.99,'milk':5.80}
print(prices_lookup['milk'])

#A dictionary can store a number, a string, a list and even a new dictionary

d={'k1':123,'k2':[0,3,5],'k3':{'insideKey1':100,'insideKey2':200}}      #k1=integer, k2=list, k3=another dictionary
print(d['k3'])      #output: {'insideKey1':100,'insideKey2':200}}

#For displaying the integer 100 from insideKey1 from k3 we will type the key value from the first dictionary and then 
#the key value from the second dictionary, both in [] brackets.
print(d['k3']['insideKey1'])        #output: 100 

#For displaying an item from a list inside a dictionary we will type the key value from the first dictionary and then
#the index of the item in the list
print(d['k2'][1])   #output:3  | The second [] it's indicateing the index

#How to extract an item by his index from a list inside a dictionary and applying a function on it
mylist={'key1':['a','b','c','d']}
print(mylist['key1'])               #display the list by his key    | optional step
letter=mylist['key1'][2]            #grab the item by his index 
letter=letter.upper()               #applying the .upper() function
print(letter)        #output:C      #display the result

#The same example above but in less lines of code
mylist={'key1':['a','b','c','d']}
print(mylist['key1'][2].upper())    #grab the key from the dictionary, grab the index from the list, apply function .upper()

#Adding new items to a dictionary
d={'key1':100,'key2':200}
print(d)
d['key3']=300       #adding a new value to a dictionary
print(d)

#Overwrite a value which is already in a dictionary
d={'key1':100,'key2':200}
print(d)
d['key1']='New Value'       #assign a new value for key1
print(d)

d={'key1':100,'key2':200,'key3':300,'key4':400,'key5':500}
print(d)
#To see all the keys from a dictionary
print(d.keys())
#To see all the values from a dictionary
print(d.values())
#To see both keys and values grouped together
print(d.items())
