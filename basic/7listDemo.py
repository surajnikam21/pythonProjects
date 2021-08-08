#example of list
#arrays are list

fruits = ['apple', 'orange', 'banana']
courses = ['java', 'python', 'aws']

print(fruits[2])  #banana
print(fruits[:2])
print(courses[1])
print(fruits[::-1])  #reverse the list fruits

fruits.append('Guava')
fruits.append('apple')
fruits.append('orange')
print(fruits)
apple_count = fruits.count('apple')
print(apple_count)

fruits.insert(0,'Kiwi')
print(fruits)

print(fruits.pop())
print(fruits)
fruits.remove('apple') #remove 1st occurrence
print(fruits)

