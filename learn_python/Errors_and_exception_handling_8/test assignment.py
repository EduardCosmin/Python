# Test assignment

#Problem 1
#Handle the exception thrown by the code below using 'try; and except 'block'
print('Problem 1:')
try:
    for i in ['a','b','c']: #[1,2,3]:
        print(i**2)
except TypeError:   #this block execute if there is an error in try block
    print("There is a type error in the code!")
else:   #this block execute if there is no error in try block
    print("Your code is sintactically ok")

print("")
#Error before adding try/except
#TypeError                                 Traceback (most recent call last)
#<ipython-input-1-c35f41ad7311> in <module>()
#      1 for i in ['a','b','c']:
#----> 2     print(i**2)
#TypeError: unsupported operand type(s) for ** or pow(): 'str' and 'int'


#Problem 2
#Handle the exception thrown by the code below by using try and except blocks. 
#Then use a finally block to print 'All Done.
print('Problem 2:')
try:
    x = 5
    y = 0
    z = x/y
except ZeroDivisionError:
    print("There is some errors in your code!\nYou cannot divide something by zero(0)")
else:
    print("Your sintax is ok!")
finally:
    print("Let's hope that in future will be no error in the code!")

print("")
#Error before adding try/except/finally blocks
#ZeroDivisionError                         Traceback (most recent call last)
#<ipython-input-2-6f985c4c80dd> in <module>()
#      2 y = 0
#      3 
#----> 4 z = x/y
#ZeroDivisionError: division by zero

#Problem 3
#Write a function that asks for an integer and prints the square of it.
#Use a while loop with a try, except, else block to account for incorrect inputs.
#Expected output:
#Input an integer: null
#An error occurred! Please try again!
#Input an integer: 2
#Thank you, your number squared is:  4
print('Problem 3 - square numbers:')
def ask():
    while True:
        try:
            integer = int(input('Input an integer: '))
            if integer == int(integer): #condition for integer
                integer = integer **2
                print(f'Thank you, your number square is {integer}')
        except:
            print("Please try again!")
            continue    #will start again at the beginning of the while
        break   #when the answer is correct will stop the while loop
ask()

#The same problem in other way typed:
def ask_2():
    #We will assign a value for the 'TRUE' condition 
    waiting = True
    while waiting:
        try:
            n = int (input("Enter an integer: "))
        except:
            print("Please try again!")
            continue
        else:
            waiting = False
    print(f"Your number square is: {n**2}")
ask_2()