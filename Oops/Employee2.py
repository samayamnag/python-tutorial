class Employee2:
    '''Example with instance methods, class methods
    and static methods
    class methods can be accessed with instance also
    '''
    num_of_employees = 0
    raise_amount = 1.4

    def __init__(self, first_name, last_name, pay):
        self.first_name = first_name
        self.last_name = last_name
        self.pay = pay
        self.email = first_name + '.' + last_name + '@gmail.com'

        Employee2.num_of_employees += 1  # Increment by one for each employee object created

    def full_name(self):
        return '{}  {}'.format(self.first_name, self.last_name)

    def apply_raise(self):
        return int(self.pay * self.raise_amount)

    @classmethod
    def set_raise_amount(cls, amount):
        cls.raise_amount = amount


emp1 = Employee2('Nageswara', 'Rao', 75000)
emp2 = Employee2('Nageswara', 'Rao', 75000)

print(Employee2.raise_amount)
Employee2.set_raise_amount(1.5) # same as Emplyee2.raise_amount = 1.5
print(Employee2.raise_amount)
emp1.set_raise_amount(1.6)
print(Employee2.raise_amount)