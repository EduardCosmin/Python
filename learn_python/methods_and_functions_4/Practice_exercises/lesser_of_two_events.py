#LESSER OF TWO EVENS

#Write a function that returns the lesser of two 
#given numbers if both numbers are even, but returns the greater if 
#one or both numbers are odd.
#Example:
#lesser_of_two_evens(2,4) --> 2
#lesser_of_two_evens(2,5) --> 5
def lesser_of_two_numbers(a, b):
    if a %2==0 and b %2==0:
        if a<b:
            result = a
        elif a>b:
            result = b
    else:
        if a>b:
            result = a
        else:
            result = b
    return result
print(lesser_of_two_numbers(9,7))
print(lesser_of_two_numbers(2,4))
print(lesser_of_two_numbers(7,5))

#Another way:
def lesser_of_two_events(a, b):
    if a %2==0 and b %2==0:
        return min(a,b)
    else:
        return max(a,b)
lesser_of_two_events(9,7)
lesser_of_two_events(2,4)
lesser_of_two_events(2,5)

#Another example - better way:
def lesser_of_two_evens(a,b):
    if a%2==0 and b%2==0:
        return min(a,b)
    else:
        return max(a,b)

lesser_of_two_evens(9,7)
lesser_of_two_evens(2,4)
lesser_of_two_evens(2,5)