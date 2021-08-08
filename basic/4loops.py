
message = 'This is learning: session of Python'
words = message.split(':')
print(words)  # []
print(len(words)) #2

message = 'This is learning session of Python'
words = message.split(' ')
print(words)  # []
print(len(words)) #6


message = 'apple, orange, papaya, banana, kiwi'
fruits = message.split(',')   #list
print(fruits)  # []
print(len(fruits)) #6

for fruit in fruits:
    print(fruit)



students = ['suraj','rohan','amar','akash','yogesh']
for student in students:
    print(student)


nums = [1,2,3,4,5,6]
print("Start")
for num in nums:
    if(num == 5):
        break
    print(num)
print("End")


students = ['suraj','rohan','amar','akash','yogesh']
for student in students:
    if(student == 'akash'):
        break
    print(student)



days = ['Sunday', 'Monday', 'Tuesday', 'Wednesday', 'Thrusday', 'Friday', 'Staurday']

for day in days:
    if(day=='Friday'):
        print('weekend starts')


#
#
# nums = [1,2,3,4,5,6,7,8,9 ]  # list of int type
#
# for num in nums:
#     print(num)
#
#
# students = ['suraj','abhijeet','rohan','prathamesh','ajit']  #list of string type
#
# for student in students:
#     if(student == 'prathamesh'):
#         print('Hello Prathamesh!')
