# This is file to check user input is vowel or not

def check_vowel(data1):
    vowels = ['a', 'e', 'i', 'o', 'u']
    if data1 in vowels:
        print('The user input data {} is vowel.'.format(data1))
    else:
        print('The user input data {} is not a vowel.'.format(data1))

print('Enter any character: ')
user_input = input();
#print(user_input)
check_vowel(user_input)





