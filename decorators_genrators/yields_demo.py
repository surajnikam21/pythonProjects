
def gen():  # defines a generator function
    yield '123'

data = gen()
#print(next(data))
print(type(next(data)))
print(type(gen()))
print(list(gen()))    #list comprehension
print(tuple(gen()))  #tuple comprehension
print(set(gen()))    #set comprehension

list1 = ['apple', 'orange', 'mango']
it_data = iter(list1)
print(set(it_data))
# print(tuple(it_data))
print(tuple(iter(list1)))


L = [('Italy', 'Rome'), ('France', 'Paris'), ('US', 'Washington DC')]
print(dict(iter(L)))



#Generators:
# 1) performing some operation for every element,
# 2) selecting a subset of elements that meet some condition


line_list = ['  line 1\n', 'line 2  \n']

# Generator expression -- returns iterator
stripped_iter = (line.strip() for line in line_list)
print(stripped_iter)


# List comprehension -- returns list
stripped_list = [line.strip() for line in line_list]
print(stripped_list)


# Set comprehension -- returns list
stripped_list = {line.strip() for line in line_list}
print(stripped_list)

stripped_list = [line.strip() for line in line_list
                 if line != ""]

print(stripped_list)


data = [x*x for x in range(1,6)]
print(data)   # List Comprehension with type 1.

sumOfData = sum((x*x for x in range(1,6)))
print(sumOfData)

sumOfData = sum((x for x in range(1,6)))
print(sumOfData)

data = [x*x for x in range(1,6) if x%2 !=0 ]    # List Comprehension with type 2.
print(data)


seq1 = 'abcd'
seq2 = (1, 2, 3)
data1 = [(x, y) for x in seq1 for y in seq2]
print(data1)



def generate_ints(N):
    for i in range(N):
        yield i

data = generate_ints(10)
print(list(data))

#print(list(generate_ints(6)))