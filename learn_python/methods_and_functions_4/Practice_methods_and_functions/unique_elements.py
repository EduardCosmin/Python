#Write a Python function that takes a list and returns a new list with unique elements of the first list.
#Exemple:
#Sample List : [1,1,1,1,2,2,3,3,3,3,4,5]
#Unique List : [1, 2, 3, 4, 5]

def unique_list(lst):
    return list(set(lst))
print(unique_list([1,1,1,2,2,2,3,3,3,4,4,5,6,7,8,8,8]))

#Another way -> not as nice as above
def unique_list2(lst):
    x=[]
    for a in lst:
        if a not in x:
            x.append(a)
    return x
print(unique_list2([1,1,1,2,2,2,3,3,3,4,4,5,6,7,8,8,8]))