# Function defined outside the class
def f1(self, x, y):
    return min(x, y)

class C:
    f = f1

    def g(self):
        return 'hello world'

    h = g

class suraj:
    pass


c1 = C()

print(c1.h)
print(type(c1.h))
print(c1.f)
print(type(c1.f))


print(c1.g())
print(c1.f(1,2))
print(f1(c1,1,3))

print(c1.h)
print(c1.h())

print(f1(suraj(), 9, 4))
