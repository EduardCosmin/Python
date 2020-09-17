#MAKES TWENTY

# Given two integers, return True if the sum of the integers is 20 or if one of the integers is 20. If not, return False
#Example:
#makes_twenty(20,10) --> True
#makes_twenty(12,8) --> True
#makes_twenty(2,3) --> False
def make_twenty(a,b):
    if (a+b==20) or a==20 or b==20:
        return True
    else:
        return False

print(make_twenty(20,12))
print(make_twenty(8,12))
print(make_twenty(10,20))
print(make_twenty(2,12))

#Same problem in a single line
#return is already a boolean!!!
def make_twenty2(n1,n2):
    return (n1+n2)==20 or n1==20 or n2==20
print(make_twenty(20,12))
print(make_twenty(8,12))
print(make_twenty(10,20))
print(make_twenty(2,12))