# oops

# class Employee:
#     pass
#     # class members variables
#     # methods
#
# emp1 = Employee()
# emp2 = Employee()
# print(emp1)
# print(emp2)


class Employee:

    raise_amt = 1.04  #class variable
    num_of_emps = 0   #static variables

    # constructor : initializes class instance var
    def __init__(self, first, last, pay):
        self.first = first
        self.last = last
        self.pay = pay

        self.email = self.first + '.' + self.last + '@mail.com'
        Employee.num_of_emps += 1

    # Instance method
    def fullname(self):
       # return '{} {}'.format(self.first, self.last)
        return self.first + ' ' + self.last

    def raise_apply(self):
        self.pay = int(self.pay * self.raise_amt)


emp1 = Employee('Suraj', 'Singh', 30000)
emp2 = Employee('Pankaj', 'Sharma', 20000)
emp3 = Employee('Kiran', 'Suraj', 20000)
print(Employee.num_of_emps)


# print(emp1.first)
# print(emp1.email)
print(emp1.fullname())
# print(Employee.fullname(emp1))
print(emp1.pay)
emp1.raise_apply()
print(emp1.pay)


# print(emp2.first)
# print(emp2.email)
print(emp2.fullname())
print(emp2.pay)
emp2.raise_apply()
print(emp2.pay)



