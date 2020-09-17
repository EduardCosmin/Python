#If, Elif, Else statements

if True:
    print("It's true.")

hungry=True
if hungry:
    print('Feed me!')
else:
    print("I'm full!")

hungry=False
if hungry:
    print('Feed me!')
else:
    print("I'm full!")

loc='Bank'
if loc =='Auto Shop':
    print('Cars are cool')
elif loc=='Bank':
    print('Money are cool.')
elif loc=='Store':
    print('Welcome to the store')
else:
    print('I do not know much.')

name="Sammy"
if name=='Sammy':
    print('Hello Sammy')
elif name=='Frankie':
    print('Hello Sammy')
else:
    print('What is your name')