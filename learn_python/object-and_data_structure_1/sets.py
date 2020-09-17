#Sets

#Sets are unordered collections of unique elements.
#Meaning there can only be one representative of the same object.

my_set=set()        #create a set
print(my_set)

my_set.add(1)       #adding an item to the set
print(my_set)
my_set.add(2)       #adding another item to the set
print(my_set)
#If you try to add an item which is already inside the set you will not succeed
my_set.add(2)
print(my_set)

my_list=[1,1,1,1,2,2,2,4,4,4,5,5,5,3,3,3,]
print(my_list)
print(set(my_list))     #take input from the list and will merge all the same items into an unique element for each value from the list
                        #output:{1,2,3,4,5}

