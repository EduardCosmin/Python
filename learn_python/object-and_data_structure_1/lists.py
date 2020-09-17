#Lists in Python

my_list=[1,2,3]     #a list of integers
print(my_list)
my_list=['string',100,23.2]     #a list can contain different types
print(my_list)
print(len(my_list))

my_list=['one','two','three']
print(my_list[0])       #displays the character with the index 0 in the list
print(my_list[1:])      #slicing from first character to the end

another_list=['four','five']
print(my_list + another_list)   #concatenate two lists

new_list=my_list + another_list
new_list[0] = "ONE ALL CAPS"        #changeing an element of a list by his index
print(new_list)

new_list.append('six')      #.append() is adding a new element at the end of a list
print(new_list)

new_list.pop()      #it delete the last element of a list
print(new_list)

new_list.pop(1)     #remove the item in the list with index of 1 (two) 
print(new_list)

string_list=['a','v','b','r','z']
num_list=[4,5,2,1,9]

string_list.sort()      #sort the list in alphabetical order
print(string_list)

num_list.reverse()
print(num_list)         #it will display the list from the end to the begining
