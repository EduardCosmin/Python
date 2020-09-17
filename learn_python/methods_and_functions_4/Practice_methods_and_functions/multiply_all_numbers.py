#Write a Python function to multiply all the numbers in a list.
#Example:
#Sample List : [1, 2, 3, -4]
#Expected Output : -24

def multiply(numbers): 
    total=1 
    for i in numbers:
        total *=i
    return total
print(multiply([1,2,3,4,-8]))