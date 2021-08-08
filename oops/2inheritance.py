class Mapping:
    def __init__(self, iterable):
        self.items_list = []
        self.__update(iterable)

    def update(self, iterable):
        for item in iterable:
            self.items_list.append(item)

    __update = update   # private copy of original update() method

class MappingSubclass(Mapping):

    def update(self, keys, values):
        # provides new signature for update()
        # but does not break __init__()
        for item in zip(keys, values):
            self.items_list.append(item)


list1= [12,34,34]

o1 = MappingSubclass(list1)
print(o1)
print(type(o1))
print(o1.items_list)

names= ['Suraj', 'Pawan', 'Birender']
ages = [23, 24, 26]
o1.update(names, ages)
print(o1.items_list)


obj1 = object()
print(obj1)

obj1 = o1
print(obj1)
print(obj1.__dict__)
print(obj1.__module__)
