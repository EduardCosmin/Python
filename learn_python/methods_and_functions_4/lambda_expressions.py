#Lambda Expressions - map and filter

#.map() function will take every item from a given list for example like below
#.filter() function will filter based of the function condition as below 
def square(num):
    return num**2
my_nums=[1,2,3,4,5]
#Adding the nums list to the 'square' method using map() method
for item in map(square,my_nums):
    print(item)

#if you want the results to be showing inside a list:
print(list(map(square,my_nums)))

def splicer(mystring):
    if len(mystring)%2==0:
        return 'even'
    else:
        return mystring[0]
names=['Andy','Eve','Sally']
print(list(map(splicer,names)))

def check_even(num):
    return num%2==0
my_nums=[1,2,3,4,5]
print(filter(check_even, my_nums))  #shows the memory on the computer where it's stored
#we need as same as with map function to transform the output into a list or to iterate through a for loop
#list method
print(list(filter(check_even,my_nums)))
#iterate method
for n in filter(check_even,my_nums):
    print(n)

#Lambda expression
print('\n'+'Lambda expressions:')

def square2(num):
    return num**2
print(square(3))

#we will turn this functions above into a lambda expression
#1 step: we can write the code above in just one line
def square3(num): return num**2
#2 step: in lambda expression is also known as anonymous function and 
#the reason for that is because it's some functionality that you intend
#only use one time; because of that we don't actually give it a name nor 
# do we use the keyword.
#Instead of the name or the def keyword we replace that with the keyword lambda.
lambda num: num **2
#the above is a lambda expression; we can assign it to a value like:
square3=lambda num: num**2
print(square(4))

#We can use lambda with map function:
my_numbers=[1,2,3,4,5,6,7,8,9]
print(list(map(lambda num:num**2,my_numbers)))
#For displaying the result we need to iterate through the function or we can use list method.

#we can use lambda with filter function
print(list(filter(lambda num: num%2==0, my_numbers)))
#As well as map function, for displaying the output we need to iterate through a for loop the output or we can use a list

#For example if we want to grab the first letter from each item inside a list
my_list=['Andy','Eve','Sally']
print(list(map(lambda name:name[0],my_list)))   #name is just a notation, it works as same with anything else

#If we want to reverse the name inside the list
print(list(map(lambda name:name[::-1],my_list)))

