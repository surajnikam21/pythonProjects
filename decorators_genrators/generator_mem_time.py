import memory_profiler as mem_profile
import random
import time

names = ["John", "Ram", "Shusil"]
majors = ["Math", "Java", "Python"]

print('Memory (Before): {}Mb'.format(mem_profile.memory_usage()))

def people_list(num_people):
    result_list = []
    for i in range(num_people):
        person = {
            'id':i,
            'name': random.choice(names),
            'major': random.choice(majors)
        }
        result_list.append(person)
    return  result_list


def people_generator(num_people):
    for i in range(num_people):
        person = {
            'id': i,
            'name': random.choice(names),
            'major': random.choice(majors)
        }
        yield person

t1 = time.time()
people = people_list(100000)
t2 = time.time()


# t1 = time.time()
# people = people_generator(100000)
# t2 = time.time()

print('Memory (After) : {}Mb'.format(mem_profile.memory_usage()))
print('Took {} Seconds'.format(t2-t1))

# Using people_list
# Memory (Before): [19.453125]Mb
# Memory (After) : [46.828125]Mb
# Took 0.10122203826904297 Seconds


#Using people_generator
# Memory (Before): [18.78515625]Mb
# Memory (After) : [18.79296875]Mb
# Took 0.0 Seconds


# You’re doubtless familiar with how regular function calls work in Python or C. When you call a function, it gets a private namespace where its local variables are created. When the function reaches a return statement, the local variables are destroyed and the value is returned to the caller. A later call to the same function creates a new private namespace and a fresh set of local variables. But, what if the local variables weren’t thrown away on exiting a function? What if you could later resume the function where it left off? This is what generators provide; they can be thought of as resumable functions.

#Any function containing a yield keyword is a generator function; this is detected by Python’s bytecode compiler which compiles the function specially as a result.
#When you call a generator function, it doesn’t return a single value; instead it returns a generator object that supports the iterator protocol. On executing the yield expression, the generator outputs the value of i, similar to a return statement. The big difference between yield and a return statement is that on reaching a yield the generator’s state of execution is suspended and local variables are preserved. On the next call to the generator’s __next__() method, the function will resume executing.


