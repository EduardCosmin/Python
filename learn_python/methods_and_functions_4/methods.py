#Methods

#Known methods:
my_list =[1,2,3,2,2,4,5,6]
print(my_list)
print(my_list.count(2)) #count how many times '2' appear in the list
my_list.append(4)   #add an item to the end of a list
print(my_list)
my_list.pop()   #remove the last item of a list
print(my_list)

#If we want to explore a new method we can type our value followed by a dot and it will appear a list of methods
#(ex: my_list.), and after dot will appear a list of methods or we can use 'help() function for more details about a method
#Help function will show us how to use a method, in our case will show us how to use .insert
print(help(my_list.insert))