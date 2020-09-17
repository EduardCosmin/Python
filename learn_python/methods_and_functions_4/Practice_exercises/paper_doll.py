#Paper Doll

#Given a string, return a string where for every character in the
#original there are three characters
#Example:
#paper_doll('Hello') --> 'HHHeeellllllooo'
#paper_doll('Mississippi') --> 'MMMiiissssssiiippppppiii'

def multiply_word(text):
    my_split=text.split()
    for i in my_split:
        i=i*3               #given word*3
        return i

print(multiply_word('AstaziEsteZiuaUnirii'))   

def paper_doll(text):
    result=''
    for char in text:
        result=result+char*3    #multiply every char from the text given by 3  
    return result

print(paper_doll('AstaziEsteZiuaUnirii'))

def multiply_letter_in_column(text):
    for i in text:
        i=i*3       #multiply each letter of the word by 3 times and outputs the result for each letter
        print(i)

multiply_letter_in_column('AstaziEsteZiuaUnirii')