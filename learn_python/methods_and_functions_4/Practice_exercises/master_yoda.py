#MASTER YODA

#Given a sentence, return a sentence with the words reversed
#Example:
#master_yoda('I am home') --> 'home am I'
#master_yoda('We are ready') --> 'ready are We'

#.join() - allows to join together strings in a list with some connector string.
#Examples:
#"--".join(['a','b','c'])      Output: 'a--b--c'
#" ".join(['Hello','world'])   Output: "Hello world"
def master_yoda(text):
    return "".join(text[::-1])     #return the reflection of a string character by character (home = emoh)
print(master_yoda('I am home'))

def reverse_str(text):
    return ' '.join(text.split()[::-1])     #returns the reverse of a string   (I am home = home am I)
print(reverse_str('I am home'))

#Another way -> output inside a list
def master_yoda2(text):
    word_list=text.split()
    reverse_word_list= word_list[::-1]
    return reverse_word_list
print(master_yoda('I am home'))

#Another way without list (same as above)
def master_yoda3(text):
    word_list=text.split()
    reverse_word_list= word_list[::-1]
    return ' '.join(reverse_word_list)
print(master_yoda('I am home'))