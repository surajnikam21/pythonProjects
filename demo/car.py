class Car:

    def __init__(self, colour, miles):
        self.colour = colour
        self.miles = int(miles)


car1 = Car('Blue', 20000)
car2 = Car('Red', 30000)


def carinfo(self):
    return 'The {} car has {} miles.'.format(self.colour, self.miles)


print(carinfo(car1))
print(carinfo(car2))
