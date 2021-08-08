print('Hello')

message = ('Hello Suraj! Welcome to the Python World')
print(message[-1])
print(message[-2])
print(message[--1])
print(message[:-1])
print(message[::])

print(message[::-1])
print(len(message))
print(type(message))
print(id(message))

# message = 'Suraj'
# print(message)
# print(message[::-1])

# list1 = message.split(' ')
# print(list1)
# print(len(list1))
# for word in list1:
#     print(word)

print(message.lower())
print(message.upper())
print(message.count('Hello'))  # how many times 'Hello' appears in string variable message
print(message.find('Python'))  # return first index value 27
print(message.replace('Python', 'Java'))

name = 'Suraj'
greeting = 'Welcome'

print(name + ', ' + greeting)

# Formatting text


#print(dir(message))
#print(help(str))
