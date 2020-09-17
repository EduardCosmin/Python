#Find 33 (consecutive numbers from a list)

#Given a list of integers, return True if the array contains a 3 next to a 3 somewhere.
#Example:
#has_33([1, 3, 3]) → True
#has_33([1, 3, 1, 3]) → False
#has_33([3, 1, 3]) → False

def find_33(num):
    for i in range(0, len(num)-1):
        #nicer looking alternative in commented code
        #if num[i]==3 and num[i+1]==3:
        if num[i:i+2]==[3,3]:         #i:i+2 means that start to look from a character to the next one to him (consecutive)
            return True
    return False

print(find_33([1,3,3]))
print(find_33([1,3,1,3]))
print(find_33([3,1,3]))

#For a better point of view:
#num = [1,2,3,4,5] #alternative: [0,1,2,3,4] to see indexes
#print(num[1:1+2]) #replacing i with 1 for simple test-case.    1:1+2 means that start from index 1 to index 3(but index 3 not included) =>2 has index 1 and 4 has index 3
#Output = [2,3] #alternative: [1,2]

#Another way:
def find_33_second(num):
    for i in range(0,len(num)-1):
        if num[i]==3 and num[i+1]==3:
            return True
    return False
print(find_33_second([1,3,3]))
print(find_33_second([1,3,1,3]))
print(find_33_second([3,1,3]))
