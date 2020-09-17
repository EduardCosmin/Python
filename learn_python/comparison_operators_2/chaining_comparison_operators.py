#Chaining comparison operators

#Logical operators: and, or, not
print(1<2<3)    #true
#And - both arguments needs to be true
print(1<2 and 2<3)  #true
print(('h'=='h') and (2==2))    #true
print((1==1) or ('h'=='k'))     #false

#Or - one of the argument need to be true to display true
print((100==1) or (2==200))     #false
print((1==1) or ('h'=='k'))     #true
print((2==2) or (3==3))         #true

#Not -return the opposite boolean value of what you just did
#not opperator is like !=, (kind of)
print(1==1)   #true
not (1==1)    #false
