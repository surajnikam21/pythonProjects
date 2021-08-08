#Run this code from command prompt

from sys import argv

file, a, b, c = argv
print(type(argv))
print('The script is: ', file)
print('The script  first argument is: ', a)
print('The script  second argument is: ', b)
print('The script  third argument is: ', c)

# print('The script is: ', argv[0])
# print('The script  first argument is: ', argv[1])
# print('The script  second argument is: ', argv[2])
# print('The script  third argument is: ', argv[3])