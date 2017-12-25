class Employee3:
    '''Example with inheritance
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
        first, last, pay = emp_str.split('-')
        return cls(first, last, pay)  # Return the class object # This is same as Employee3(first, last, pay)


class Developer(Employee3):
    def __init__(self, first, last, pay, prog_lang):
        super().__init__(first, last, pay)
        # Employee3.__init__(self, first, last, pay)
        self.prog_lang = prog_lang


class Manager(Employee3):
    def __init__(self, first, last, pay, employees=None):
        super().__init__(first, last, pay)
        if employees is None:
            self.employees = []
        else:
            self.employees = employees

    def add_employee(self, emp):
        if emp not in self.employees:
            self.employees.append(emp)

    def remove_employee(self, employee):
        if employee in self.employees:
            self.employees.remove(employee)

    def print_employees(self):
        for emp in self.employees:
            print(emp.full_name())


dev1 = Developer('Nageswara', 'Rao', 75000, 'PHP')
dev2 = Developer('Satish', 'Samayam', 105000, 'Python')

manager1 = Manager('Manager1', 'Rao', 75000)
# manager2 = Manager('Manager2', 'Samayam', 105000)

manager1.add_employee(dev2)
manager1.add_employee(dev1)

manager1.print_employees()
print(isinstance(manager1, Manager))
print(issubclass(Manager, Employee3))
