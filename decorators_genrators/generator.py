def counter(maximum):
    i = 0
    while i < maximum:
        val = (yield i)
        # If value provided, change counter
        if val is not None:
            i = val
        else:
            i += 1


it = counter(10)
print(next(it))  #0
print(next(it))  #1
it.send(8)   # move position of iterator to the 8th position
print(next(it))  #9



def upper(s):
    return s.upper()

print(list(map(upper, ['sentence', 'fragment'])))

def is_even(x):
    return (x % 2) == 0   # T / F

print(list(filter(is_even, range(10))))
