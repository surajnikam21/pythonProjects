class Car:

    def __init__(self, colour, miles):
        self.colour = colour
        self.miles = int(miles)


    def carinfo(self):
        return 'The {} car has {} miles.'.format(self.colour, self.miles)


#Take the input from user

print("Please enter the car color and its mileage")
color = input("Enter Color.")
miles = input("Enter car miles")


car = Car(color, miles)

print(car.carinfo())



