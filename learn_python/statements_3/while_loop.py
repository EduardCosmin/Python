#While loop
#While loops will continue to execute a block of code while some condition remains True.

#Syntax:
#while some_boolean_condition:
#   do something
#else:
#   do something different

x=0
while x<5:
    print(f'The current value of x is {x}.')    #if we run this statement we will make an infinite loop
    #update the value of x
    x += 1
else:
    print('X is greater than 5.')

#Break, continue, pass
#We can use these three statements in our loops to add additional functionality for various cases.
#break: breaks out the current closest enclosing loop
#continue: goes to the top of the closest enclosing loop
#pass: does nothing at all

#pass
x=[1,2,3]
for item in x:
    pass    #this function is a placeholder for smth. that you don't know yet what condition to assign
#Now if I continue to write a print statement, because 'pass' is above my statement will not execute that for loop.
print('end of my script')

#Continue
mystring='Sammy'
for letter in mystring:
    if letter =='a':    
        continue    #it will display the value of mystring, but when will see letter 'a', will go on after and will not display it
    print(letter)

for letter in mystring:
    if letter =='a':    
        break    #it will display the value of mystring, but when will see letter 'a', will stop to compile and will display all until that point
    print(letter)

x=0
while x<5:
    if x==2:
        break   #will display values until x will be equal with 2 and will stop
    print(x)
    x+=1
