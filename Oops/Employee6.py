class Employee:
    '''Property decorators - getter and setters'''

    def __init__(self, first_name, last_name, pay):
        self.first_name = first_name
        self.last_name = last_name
        self.pay = pay

    @property
    def email(self):
        return '{}.{}@gmail.com'.format(self.first_name, self.last_name)

    @property
    def full_name(self):
        return self.first_name + ' ' + self.last_name

    @full_name.setter
    def full_name(self, name):
        first, last = name.split(' ')
        self.first_name = first
        self.last_name = last

    @full_name.deleter
    def full_name(self):
        self.first_name = None
        self.last_name = None


emp1 = Employee('Nageswara', 'Rao', 75000)

print(emp1.email)
print(emp1.full_name)

emp1.full_name = 'Lord Siva'

print(emp1.full_name)

del emp1.full_name
print(emp1.first_name)