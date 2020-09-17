#Count Primes

#Write a function that returns the number of prime numbers that exist
#up to and including a given number.
#Example
#count_primes(100) --> 25
#By convention, 0 and 1 are not prime.

def count_primes(num):
    #store our primes numbers
    primes=[2]
    #counting going up to the input num
    x=3
    if num <2 : #in case if the num is 0 an 1
        return 0
    #x is going through every number up to input num
    while x <= num:
        #check if x is prime
        for y in range(3,x,2):   #test all odd factors up to x-1
            if x%y==0:
                x+=2
                break
        else:
            primes.append(x)
            x+=2
    print (primes)
    return len(primes)

print(count_primes(100))

#Another way to count primes:
def count_primes2(num):
    primes=[2]
    x=3
    if num < 2:
        return 0
    while x <= num:
        for y in primes:     #use the primes list
            if x%y==0:
                x+=2
                break
        else:
            primes.append(x)
            x+=2
    print(primes)
    return(len(primes))

print(count_primes2(100))
