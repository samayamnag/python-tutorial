class Employee1:
    '''Example with class variables'''
    num_of_employees = 0
    raise_amount = 1.4

    def __init__(self, first_name, last_name, pay):
        self.first_name = first_name
        self.last_name = last_name
        self.pay = pay
        self.email = first_name + '.' + last_name + '@gmail.com'

        Employee1.num_of_employees += 1  # Increment by one for each employee object created

    def full_name(self):
        return '{}  {}'.format(self.first_name, self.last_name)

    def apply_raise(self):
        return int(self.pay * self.raise_amount)
        # return int(self.pay * Employee1.raise_amount) # Accessing with class


print(Employee1.num_of_employees)
print(Employee1.raise_amount)
emp1 = Employee1('Nageswara', 'Rao', 75000)
emp2 = Employee1('Nageswara', 'Rao', 75000)

print(Employee1.num_of_employees)
print(emp1.apply_raise())
emp1.raise_amount = 2.2 # Set raise amount specific to emp1
print(emp1.apply_raise())
print(emp2.apply_raise())
# print(Employee.full_name(emp1)) # In the back ground work like this
