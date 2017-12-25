import datetime;


class Employee4:
    '''Example with static methods
     Static methods won't take self or cls as their first argument.
     In simple words static methods are those are not using self or cls variable/methods.
     These are very plain methods.
     Static methods can be access by class as well as instance ======
    '''
    num_of_employees = 0
    raise_amount = 1.4

    def __init__(self, first_name, last_name, pay):
        self.first_name = first_name
        self.last_name = last_name
        self.pay = pay
        self.email = first_name + '.' + last_name + '@gmail.com'

        Employee4.num_of_employees += 1  # Increment by one for each employee object created

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
        return cls(first, last, pay)  # Return the class object # This is same as Employee4(first, last, pay)

    @staticmethod
    def is_workday(day):
        if day.weekday() == 5 or day.weekday() == 6:
            return False
        return True


emp1 = Employee4('Nageswara', 'Rao', 75000)
emp2 = Employee4('Nageswara', 'Rao', 75000)

my_date = datetime.date(2017, 12, 24)
print(Employee4.is_workday(my_date))
print(emp1.is_workday(my_date))
