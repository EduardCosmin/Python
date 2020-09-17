#Blackjack

#Given three integers between 1 and 11, if their sum is less than
# or equal to 21, return their sum. If their sum exceeds 21 and there's 
#an eleven, reduce the total sum by 10.
#Finally, if the sum (even after adjustment) exceeds 21, return 'BUST'
#Example:
#blackjack(5,6,7) --> 18
#blackjack(9,9,9) --> 'BUST'
#blackjack(9,9,11) --> 19

def blackjack(a,b,c):
    if sum([a,b,c])<=21:
        return sum([a,b,c])
    elif 11 in [a,b,c] and sum([a,b,c]) <=31:
        return sum([a,b,c])-10
    else:
        return 'Bust'
    
print(blackjack(5,6,7))
print(blackjack(9,9,9))
print(blackjack(9,9,11))

#Better understanding of .sum():
#sum(iterable, start)  
#iterable : iterable can be anything list , tuples or dictionaries ,
#but most importantly it should be numbers.
#start : this start is added to the sum of 
#numbers in the iterable. 
#If start is not given in the syntax , it is assumed to be 0.
#EXamples:
# numbers = [1,2,3,4,5,1,4,5] 
# # start parameter is not provided 
# Sum = sum(numbers) 
# print(Sum)          #output:25

# # start = 10 
# Sum = sum(numbers, 10)  #will add 10 to addition
# print(Sum)              #output:35