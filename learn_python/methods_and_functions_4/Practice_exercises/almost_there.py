#Almost there

#Given an integer n, return True if n is within 10 of either 100 or 200
#Example:
#almost_there(90) --> True
#almost_there(104) --> True
#almost_there(150) --> False
#almost_there(209) --> True
#Note: abs(num) returns the absolute value of a number

def almost_there(n):
    if abs(n<=110 and n>=90) or abs(n<=210 and n>=190):
        return True
    else:
        return False
print(almost_there(90.9))
print(almost_there(104))
print(almost_there(150))
print(almost_there(209))

print('')

#Another way to construct this function
def almost_there2(n):
    return ((abs(100-n) <= 10) or (abs(200-n) <=10))       #return it's a boolean

print(almost_there2(90))
print(almost_there2(104))
print(almost_there2(150))
print(almost_there2(209))