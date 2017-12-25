class Employee3:
    '''Example with alternative constructor.
    Best example is datetime module
    '''
    num_of_employees = 0
    raise_amount = 1.4

    def __init__(self, first_name, last_name, pay):
        self.first_name = first_name
        self.last_name = last_name
        self.pay = pay
        self.email = first_name + '.' + last_name + '@gmail.com'

        Employee3.num_of_employees += 1  # Increment by one for each employee object created

    def full_name(self):
        return '{} {}'.format(self.first_name, self.last_name)

    def apply_raise(self):
        return int(self.pay * self.raise_amount)

    @classmethod
    def set_raise_amount(cls, amount):
        cls.raise_amount = amount

    @classmethod
    def from_str(cls, emp_str):
        first,last,pay = emp_str.split('-')
        return cls(first, last, pay) # Return the class object # This is same as Employee3(first, last, pay)


emp1_string = 'Nag-Samayam-75000'
emp2_string = 'Satish-Samayam-10000'

emp1 = Employee3.from_str(emp1_string) # Create object from class method
emp2 = Employee3.from_str(emp2_string)
print(emp1.full_name())
print(emp2.full_name())