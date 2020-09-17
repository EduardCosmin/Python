#Guessing Game Challenge
#Let's use while loops to create a guessing game.
#The Challenge:
#Write a program that picks a random integer from 1 to 100, and has players guess the number. 


print("Welcome to the guessing game!")
print('Tell me your name, player:')
name=input('')
print('Welcome, '+name+'!\n'+'Now I will introduce you the rules of the game:')
print('You need to choose a number between 1 and 100!\n'+
      "If the number that you choose it's the same as mine, you won!")
print("If you don't pick the same number as me you'll have to choose another number until it matches my guess.\n"+
      "You will have some hints as 'warm' and 'cold' if your guessing is near mine by 10 digits.\n"+
      "Or you can receive 'warmer' or 'colder' if it's even near.\n"+
      "Let's play and good luck!")
from random import randint  #import randint from random library
num=randint(1,100)      #assign randint to a variable and select the range
#print(num)             #only for checking if randint works
guesses=[0]
while True:
    guess=int(input("I am thinking of a number between 1 and 100.\nWhat is your guess?\n"))
    if guess < 1 or guess >100:
        print('Out of Bunds! Try again: ')
        continue
    #now we compare the player's guess to our number
    if guess == num:
        print(f"Congratulations, you guessed it in only {len(guesses)} guesses!")
        break
    #if the guess is incorrect, and guess to the list
    guesses.append(guess)
    #when testing the first guess, guessing_list[-2]==0, which evaluates to False
    #and brings us down to the second section
    if guesses[-2]:     #if you append all new guesses to the list, then the previous guess is given as guesses[-2]
        if abs(num-guess) < abs(num-guesses[-2]):
            print('Warmer!')
        else:
            print('Colder!')
    else:
        if abs(num-guess) <= 10:
            print('Warm!')
        else:
            print('Cold!')
print('')
#The abs() takes only one argument, a number whose absolute value is to be returned. The argument can be an integer, a floating point number or a complex number.
#If the argument is an integer or floating point number, abs() returns the absolute value in integer or float.
#In case of complex number, abs() returns only the magnitude part and that can also be a floating point number.

#Examples:
# floating point number 
float = -54.26
print('Absolute value of float is:', abs(float)) 

# An integer 
int = -94
print('Absolute value of integer is:', abs(int)) 

# A complex number 
complex = (3 - 4j) 
print('Absolute value or Magnitude of complex is:', abs(complex)) 