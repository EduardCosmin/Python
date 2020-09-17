#Indexing and slicing strings
#spaces are countable when you try to display a value by an index

#Indexing
mystring='hello world'
print(mystring[0])             #display the first character of the string (h) by index
print(mystring[8])             #display the eighth character of the string (r) by index
print(mystring[-1])#output: d  #when try to display from the end of a string the count strats with -1 

#Slicing
#starting count from 0
mystring='abcdefghijklmnopqrstuvwxyz'
#print(mystring[start:stop:jump/step])      #default

print(mystring[2])      #output: c
print(mystring[2:])     #output from the second position included (c) to the end of the string
print(mystring[:3])     #output the first 3 characters (abc) - not included the third character
print(mystring[3:6])    #output from the third character (d) to the sixth character(g), but not included the sixth (def)
print(mystring[6:-1])   #output from the sixth character (g) to the last of the string minus the last character
print(mystring[8:16])   #output from i(8) to q(16), but q is not included
print(mystring[::])     #output all from the begining to the end of the string
print(mystring[::1])    #output all the string character by character (default stepsize)
print(mystring[::2])    #output all the string but in jumps of two (aceg...)
print(mystring[::3])    #output all the string with jumps from 3 to 3 characters (adg...)
print(mystring[2:7:2])  #output the string start from the second character to the seventh one but not included in jumps of two (ceg)
print(mystring[::-1])   #output the reverse of the string character by character
print(mystring[::-2])   #output the reverse string in jumps of two started from the end