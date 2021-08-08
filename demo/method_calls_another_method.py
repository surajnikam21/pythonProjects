class Bag:
    def __init__(self):
        self.data = []   #empty list

    def add(self, x):
        self.data.append(x)

    def addtwice(self, x):
        self.add(x)
        self.add(x)



b1 = Bag()
b1.addtwice(5)
print(b1.data)

b1.addtwice('suraj')
print(b1.data)

b1.add('roshan')
print(b1.data)


