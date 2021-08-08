def factorial(num):
    fact = 1
    i = 1

    while (i <= num):
        fact = fact * i
        i = i + 1

    return fact


number = int(input('Enter your factorial number:'))

result = factorial(number)

print(result)

