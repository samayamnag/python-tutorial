class Employee:
    def __init__(self, first_name, last_name, pay):
        self.first_name = first_name
        self.last_name = last_name
        self.pay = pay
        self.email = first_name + '.' + last_name + '@gmail.com'

    def full_name(self):
        return self.first_name + ' ' + self.last_name


emp1 = Employee('Nageswara', 'Rao', 75000)

print(emp1.full_name())
# print(Employee.full_name(emp1)) # In the back ground work like this
