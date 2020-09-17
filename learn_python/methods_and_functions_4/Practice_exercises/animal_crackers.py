#ANIMAL CRACKERS

#Write a function which takes a two-word string and returns True if both words begin with same letter:
#Example
#animal_crackers('Levelheaded Llama') --> True
#animal_crackers('Crazy Kangaroo') --> False
def animal_crackers(text):
    wordlist=text.lower().split()   #use .split() to separate the words and .lower() to lowercase the words for precision
    return wordlist[0][0]==wordlist[1][0]

print(animal_crackers('Levelheaded Llama'))
print(animal_crackers('Crazy Kangaroo'))

#Another way to write this program:
def first_letter(text):
    first=text.split()
    if first[0][0]:     #if each first character is the same from the split list return True
        return True
    else:
        return False

print(animal_crackers('Levelheaded Llama'))
print(animal_crackers('Crazy Kangaroo'))