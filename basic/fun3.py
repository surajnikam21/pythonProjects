def Factorial(Num):
    fact = 1

    for i in range(1,Num+1):
        fact = fact*i
    return fact


Number = int(input('Enter your factorial number:'))

Result = Factorial(Number)

print('The factorial of given %d = %d'%(Number,Result))

#print(Result)




