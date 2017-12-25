class Employee:
    '''Special methods'''

    def __init__(self, first_name, last_name, pay):
        self.first_name = first_name
        self.last_name = last_name
        self.pay = pay
        self.email = first_name + '.' + last_name + '@gmail.com'

    def full_name(self):
        return self.first_name + ' ' + self.last_name

    def __repr__(self):
        return "Employee('{}, {}, {}')".format(self.first_name, self.last_name, self.pay)

    def __str__(self):
        return '{} - {}'.format(self.full_name(), self.email)

    def __add__(self, other):
        return self.pay + other.pay

    def __len__(self):
        return len(self.full_name())

    def __str__(self):
        pass


emp1 = Employee('Nageswara', 'Rao', 75000)

print(emp1.full_name())
# print(Employee.full_name(emp1)) # In the back ground work like this

print(repr(emp1))
print(len(emp1))

# print(1+2) # same as print(int.__add__(1,2))
# print(int.__add__(1,2))
