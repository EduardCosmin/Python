#Write a Python function that checks whether a passed in string is palindrome or not.
#Note: A palindrome is word, phrase, or sequence that reads the same backward as forward, e.g., madam or nurses run.
#Example: 
#palindrome('helleh') -> output:True

def palindrome(s):
    s=s.replace(' ','') #replace all spaces with no spaces
    s=s.lower()
    if s == s[::-1]:
        return (f'The word {s} is a palindrome.')
    else:
        return (f'The word {s} is not a palindrome.')
print(palindrome('helleh'))
print(palindrome('nurses run'))
print(palindrome('dadac'))
