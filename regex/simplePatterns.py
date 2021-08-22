import re

text_to_serach = '''
abcdefghijklmnopqrstuvwxyz
ABCDEFGHIJKLMNOPQRSTUVWXYZ
1234567890
Ha HaHa
MetaCharacters (Need to be escaped):
. ^ $ * + ? { } [ ] \ | ( )
google.com
321-555-4321
321--555---4321
123.555.3213
123-666.3453
123.999.4233
321*111*4233
800.999.4233
900.999.4233
Mr. Singh
Mr Suraj
Ms Sharma
Mrs. Verma
Mr. T
cat
mat
pat
bat
'''

# print('\t Suraj')
# print(r'\t Suraj')

#pattern = re.compile(r'.')   # everything
#pattern = re.compile(r'\.')   # pattern for only period .
#pattern = re.compile(r'google\.com')   #
#pattern = re.compile(r'\d')    # \d -  digits
#pattern = re.compile(r'\d\d\d')    # \d -  digits
#pattern = re.compile(r'\d\d\d-')    # \d -  digits
#pattern = re.compile(r'-\d\d\d-')    # \d -  digits
#pattern = re.compile(r'\d\d\d.\d\d\d.\d\d\d\d')    # \d -  digits
#pattern = re.compile(r'\D')    # \D - No digits, rest all, negate the digits

# pattern = re.compile(r'\w')  # to get words
#pattern = re.compile(r'\w+') # to gwt more then one words

# pattern = re.compile(r'\W')   # negate words, other then word, like special char etc.
# pattern = re.compile(r'\W+')  # more than one special char

# pattern = re.compile(r'\s') #matches space
# pattern = re.compile(r'\S') #matches all, not space

# pattern = re.compile(r'\bHa')   # matches all 'Ha' word boundary
# pattern = re.compile(r'\bHaHa')   # matches all 'Ha' word boundary
# pattern = re.compile(r'\BHa')   # matches all 'Ha' word boundary
#pattern = re.compile(r'\d\d\d.')   # all combination of 3 digits
# pattern = re.compile(r'\d\d\d[-.]')   # all combination of 3 digits
#pattern = re.compile(r'\d\d\d[-.]\d\d\d[-.]')   # all combination of 3 digits

# pattern = re.compile(r'[89]\d\d')   # all combination of 3 digits
# pattern = re.compile(r'[89]00')   # all combination of 3 digits

#pattern = re.compile(r'[1-5]')   # specify range digits
# pattern = re.compile(r'[a-z]')   # specify range
# pattern = re.compile(r'[a-z]+')   # specify range
# pattern = re.compile(r'[A-Z]')   # specify range
#pattern = re.compile(r'[A-Z]+')   # specify range
#pattern = re.compile(r'[a-zA-Z0-9]')
# pattern = re.compile(r'[^a-zA-Z0-9]')   # other then lower case capital case and digits

#pattern = re.compile(r'[acpb]at')   # aat cat pat bat macth
# pattern = re.compile(r'[^b]at')   # not macth bat

# pattern = re.compile(r'\d\d\d')
# pattern = re.compile(r'\d{3}')
#pattern = re.compile(r'\d{3}.\d{3}.\d{4}')

# pattern = re.compile(r'Mr')
# pattern = re.compile(r'Mr\.')

#pattern = re.compile(r'Mr\.?\s[a-zA-Z]+')
pattern = re.compile(r'(Mr|Ms|Mrs)\.?\s[A-Z]\w*')

matches = pattern.finditer(text_to_serach)

for match in matches:
    print(match)






multi = '''

This is a test

Start and begin here

end here 

'''
#
# sentance = 'Start a sentence and then bring it to an end'
#
# sentance1 = 'Suraj a sentence and then bring it to an nikam'
#
# # pattern = re.compile(r'^Start')
# # pattern = re.compile(r'nikam$')
#
# matches = pattern.finditer(sentance1)
#
# for match in matches:
#     print(match)



#print(text_to_serach[139:149])


