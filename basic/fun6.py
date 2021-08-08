def Add(a, b):
    return a + b


def Subtract(a, b):
    return a - b


def Multiply(a, b):
    return a * b


def Divide(a, b):
    return a / b


print('select operation:')
print('1.Add')
print('2.Subtract')
print('3.Multiply')
print('4.Divide')

choice = input('Enter choice(1/2/3/4):')

num1 = int(input('Enter first number:'))
num2 = int(input('Enter second number:'))

if choice == '1':
    print(num1, '+', num2, '=', Add(num1, num2))

elif choice == '2':
    print(num1, '-', num2, '=', Subtract(num1, num2))

elif choice == '3':
    print(num1, '*', num2, '=', Multiply(num1, num2))

elif choice == '4':
    print(num1, '/', num2, '=', Divide(num1, num2))

else:
    print('invalid output')




