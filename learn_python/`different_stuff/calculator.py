#First method

# print('Welcome to simple calculator!')
# num_1=float(input('Number 1: '))
# num_2=float(input('Number 2: '))
# print("What operation do you want to make: '+', '-', '*', '/'")
# operation=(input(''))
# if operation == '+':
#     print('{}+{}={}'.format(num_1, num_2, num_1+num_2))
# elif operation == '-':
#     print('{}-{}={}'.format(num_1, num_2, num_1-num_2))
# elif operation == '*':
#     print('{}*{}={}'.format(num_1, num_2, num_1*num_2))
# elif operation == '/':
#     print('{}/{}={}'.format(num_1, num_2, num_1/num_2))
# else:
#     print("You need to choose one of these: '+', '-', '*', '/'.")

#Second method

def addition(num_1,num_2):
    return num_1 + num_2

def substraction(num_1,num_2):
    return num_1 - num_2

def multiplication(num_1,num_2):
    return num_1 * num_2

def division(num_1,num_2):
    return num_1 / num_2

def to_the_power(num_1,num_2):
    return num_1**num_2

def modulo(num_1,num_2):
    return num_1%num_2

print("Welcome to simple calculator:")
print("1. Addition")
print("2. Substraction")
print("3. Multiplication")
print("4. Division")
print('5. To the power')
print("6. Modulo")
print("Choose one of: 1/2/3/4/5/6")
operation=input('')
num_1=float(input("First number: "))
num_2=float(input("Second number: "))

if operation == "1":
    print('{}+{}={}'.format(num_1, num_2, addition(num_1,num_2)))

if operation == "2":
    print('{}-{}={}'.format(num_1, num_2, substraction(num_1,num_2)))

if operation == "3":
    print('{}*{}={}'.format(num_1, num_2, multiplication(num_1,num_2)))

if operation == "4":
    print('{}/{}={}'.format(num_1, num_2, division(num_1,num_2)))

if operation == '5':
    print('{}^{}={}'.format(num_1, num_2, to_the_power(num_1, num_2)))

if operation == '6':
    print('{}%{}={}'.format(num_1, num_2, modulo(num_1, num_2)))