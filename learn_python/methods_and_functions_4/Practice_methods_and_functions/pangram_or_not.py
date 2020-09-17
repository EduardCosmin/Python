#Write a Python function to check whether a string is pangram or not.
#Note : Pangrams are words or sentences containing every letter of the alphabet at least once.
#For example : "The quick brown fox jumps over the lazy dog"
#Hint: Look at the string module

#Not working properly
str1="The quick brown fox jumps over the lazy dog"
def is_pangram(alphabet=string.ascii_lowercase): 
    if str1 in alphabet:
        return True
    else:
        return False
print(is_pangram("The quick brown fox jumps over the lazy dog"))    #true
print(is_pangram("The quick brown fox jumps over the lazy do"))     #false -> doesn't have d in the sentence
print(is_pangram('Abcdefg hijklmn opqrstu vwxyz'))                  #should be true

#Another method -> works perfect
import string
def ispangram(str1, alphabet=string.ascii_lowercase):  
    alphaset = set(alphabet)  
    return alphaset <= set(str1.lower())
print(ispangram("The quick brown fox jumps over the lazy dog"))    #true
print(ispangram("The quick brown fox jumps over the lazy do"))     #false -> doesn't have d in the sentence
print(ispangram('abcdefghijklmnopqrstuvwxyz'))                     #true

#Check:
#print(is_pangram("The quick brown fox jumps over the lazy dog")) #-> output: True
#print(string.ascii_lowercase) #-> output: 'abcdefghijklmnopqrstuvwxyz'
