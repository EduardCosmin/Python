#Write a Python function that accepts a string and calculates the number of upper case letters and lower case letters.

#Sample String : 'Hello Mr. Rogers, how are you this fine Tuesday?'
#Expected Output : 
#No. of Upper case characters : 4
#No. of Lower case Characters : 33
#HINT: Two string methods that might prove useful: .isupper() and .islower()
#If you feel ambitious, explore the Collections module to solve this problem!

s = 'Hello Mr. Rogers, how are you this fine Tuesday?'
def up_low(s):
    d={'upper':0, 'lower':0}
    for i in s:
        if i.isupper():
            d['upper']+=1
        elif i.islower():
            d['lower']+=1
        else:
            pass
    print("Original String : ", s)
    print("No. of Upper case characters : ", d["upper"])
    print("No. of Lower case Characters : ", d["lower"])
    print(d)    #just to see how the dictionary looks like after the function was outputting the results
up_low(s)
