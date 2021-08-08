

list1 = [1,2,3,4,5,6,7,8,9,10]

# for x in list1:
#     print('2 * {} = {}'.format(x,2*x))


print('Enter you number for table:')
num = input()     #always return str : even if you supply numeric

# print(type(num))   #str
# print(type(int(num)))  #str

for x in list1:
    print('{} * {} = {}'.format(num, x, int(num)*x))

