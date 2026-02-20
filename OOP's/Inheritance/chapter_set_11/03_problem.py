#Employee salaryAfterIncrement property



class Employee:
    def __init__(self, salary, increment):
        self.salary = salary
        self.increment = increment

    @property
    def salaryAfterIncrement(self):
        return self.salary + self.increment

    @salaryAfterIncrement.setter
    def salaryAfterIncrement(self, value):
        self.increment = value - self.salary

e = Employee(50000, 5000)
print(e.salaryAfterIncrement)
e.salaryAfterIncrement = 60000
print(e.increment)