#if else

num1 = 2
num2 = 3

if (num1 == num2):
    print('Equals')
else:
    print('Not Equals')


# multi if elif els
if(num1 != num2):
    print('Not Equal')
elif(num1 == num2):
    print("Equals")
elif(num1 > num2 ):
    print("num1 > num2")
else:
    print("some data")


str1 = 'Suraj'
str2 = 'suraj'

if(str1== str2):
    print("String equals")
else:
    print('String not equals')

if(str1.lower() == str2.lower()):
    print("String equals")
else:
    print('String not equals')

str3='birender'
if(str1.lower() == str2.lower() == str3.lower()):
    print("String equals")
else:
    print('String not equals')