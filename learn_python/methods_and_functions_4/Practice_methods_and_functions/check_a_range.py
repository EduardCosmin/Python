#Write a function that checks whether a number is in a given range (inclusive of high and low)
#example: ran_check(5,2,7) -> output: 5 is in the range between 2 and 7
def ran_check(num,low,high):
    if num>low and num<high:
        return (f'{num} is in the range between {low} and {high}.')
    else:
        return (f'{num} is not in the range between {low} and {high}.')
print(ran_check(9,2,7))
print(ran_check(4,2,7))

#If you only wanted to return a boolean:
#example: ran_bool(3,1,10) -> output: True
def ran_bool(num,low,high):
    return (num>low and num<high)
    #return num in range(low,high+1)    #same thing
print(ran_bool(9,2,7))
print(ran_bool(5,2,7))
