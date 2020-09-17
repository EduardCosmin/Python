#Errors and exceptions handling

#We use three keywords for this:

# try:     This is the block of code to be attempted (may lead to an error).
# except:  Block of code will execute in case there is an error in try block.
# finally: A final block of code to be executed , regardless of an error.

#Example
def add(n1, n2):
    print(n1+n2)

add(10,20)  #works perfect

#The code below will produce an error (intentionally) if uncomment

# #Now let's imagine the following situation:
# number1 = 10
# number2 = input("Please enter a number")    #the number will be a string
# add(number1,number2)
# #Now, after the line above, the code line below(doesn't matter how many) will not execute
# print("Somthing happend! ")

#We can proceed like below:
try:
    #want to attemp this code
    #may have an error
    result = 10 + 10
except:
    print("It looks like you aren't adding correctly")
print(result)   #output: 20 because the lines are correct

#Now for the same example, but we will insert an error in try block

try:
    #want to attemp this code
    #may have an error
    result2 = 10 + '10'
except:
    print("It looks like you aren't adding correctly")
else:
    #the code below will execute if there is no error in try block code
    print("add function went well")
    print(result2)

#Example try except ana finally

try:
    f = open('testfile', 'w')
    f.write("Write a test file")
except TypeError:  
    print("There was a type error!")
except OSError: #specific error for opening documents
    print("You don't have an OS Error")
finally:
    #this block will execute no matter what even if there is an error or not
    print("I always run")

#Now let's make some errors
try:
    f = open('testfile', 'r')   #we change from w to r
    f.write("Write a test file")
except TypeError:  
    print("There was a type error!")
except OSError: #specific error for opening documents
    print("You don't have an OS Error")
finally:
    #this block will execute no matter what even if there is an error or not
    print("I always run")

#try/except/finally in a function
def ask_for_int():
    try:
        result = int(input("Please provide number"))
    except:
        print("That is not a number")
    finally:
        print("End of try/except/finally")
ask_for_int()   #will display just finally block of code
                #if we will type a word will be displayed block except and finally

print('')

#try/except/finally in a loop
def ask_for_int_2():
    while True:
        try:
            result = int(input("Please provide number: "))
        except:
            print("That is not a number!")
            continue    #will continue to ask for an integer until you will type one in case that you type a string for example
        else:
            print("Yes thank you")
            break
        finally:
            print("End of try/except/finally.")
ask_for_int_2() #display else statement and finally statement
                #if we type an string we will have displayed except statement and finally statement
