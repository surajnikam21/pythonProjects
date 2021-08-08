print('Demo  for list and tuple')

students = ['suraj','abhijeet','rohan','prathamesh','ajit']  #list
print(type(students))   #<class 'list'>
students.append('Birender')
print(students)

mylist =list('abc')
print(mylist)

mylist =list('abc def xyz')
print(mylist)

mylist =list(students)
print(mylist)


emptylist =list()
print(emptylist)   #[]
emptylist.append('apple')
emptylist.append('orange')
print(emptylist)
# emptylist.clear()
# print(emptylist)  # clean data #[]

emptylist.extend(students)   # extends emptylist using list of students
print(emptylist)   #['apple', 'orange', 'suraj', 'abhijeet', 'rohan', 'prathamesh', 'ajit', 'Birender']

print(emptylist.index('ajit'))
emptylist.insert(0,'Ram')
print(emptylist)   #['Ram', 'apple', 'orange', 'suraj', 'abhijeet', 'rohan', 'prathamesh', 'ajit', 'Birender']

lastItemsfromemptylist  =emptylist.pop()
print(lastItemsfromemptylist)  # 'Birender'
print(emptylist)     #['Ram', 'apple', 'orange', 'suraj', 'abhijeet', 'rohan', 'prathamesh', 'ajit']
print(emptylist.pop())  #'ajit'

emptylist.append('prathamesh')
emptylist.append('Ram')

emptylist.remove('Ram')
print(emptylist)     # ['apple', 'orange', 'suraj', 'abhijeet', 'rohan', 'prathamesh', 'prathamesh', 'Ram']
emptylist.remove('Ram')
print(emptylist)

countOfParthmesh = emptylist.count('prathamesh')
print(countOfParthmesh)  # 2

print(emptylist.reverse())  #None
print(emptylist)

print(emptylist.sort())
print(emptylist)



#  Tuple is same like list but it can not be changed or modified.
mytuple = ('a', 'b', 'c')
mytuple1 = ()
mytuple2 = 1,     #(1,)
mytuple3 = 'q','r','s'

print(type(mytuple2))
#mytuple.add('d')    # there is no such add method
print(mytuple2)
print(mytuple3)

print(mytuple[1])
print(mytuple3[2])  #'s'

#mytuple3[2] = 'z'   #TypeError: 'tuple' object does not support item assignment

mytuple = ('a', 'b', 'c', 'a', 'b', 'z', 'y', 'b')
print(mytuple.count('a'))
print(mytuple.count('b'))
#print(mytuple.count())   #TypeError: tuple.count() takes exactly one argument (0 given)
print(mytuple.index('b'))  #1
print(len(mytuple))  #8




print('Demo of Sets')

myemptySet = set()
print(myemptySet)
print(type(myemptySet))  #<class 'set'>

myemptySet.add('suraj')
myemptySet.add(1)
print(myemptySet)   #{1, 'suraj'}

myset = {1,2,3,4}
print(type(myset))
print(myset)

myset.add(9)
print(myset)
myset.add(9)
print(myset)

myset1 = {1,2,3,4}
myset2 = {5,6,7,1}
print(len(myset1))
print(len(myset2))
print(myset1.difference(myset2))  #{2, 3, 4}
print(myset2.difference(myset1))  #{5, 6, 7}
print(myset1.intersection(myset2))  #{1}
print(myset2.intersection(myset1))  #{1}

# print(myset1.discard(3))  #None
# print(myset1)  #{1, 2, 4}

print(myset1.pop())
print(myset1)

#myset1.remove(123123)  #KeyError: 123123

myset1 = {1,2,3,4}
myset2 = {5,6,7,1}

a = myset1.union(myset2)   # {1, 2, 3, 4, 5, 6, 7}
print(myset1.union(myset2))
print(a)

a.add(90)  #{1, 2, 3, 4, 5, 6, 7, 90}

print(myset1)
print(myset1.update(a)) #none
print(myset1)

for i, v in enumerate(['tic', 'tac', 'toe']):
    print(i, v)

