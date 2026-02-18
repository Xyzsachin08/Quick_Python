class Person:
    name = "Sachin"

class Student(Person):
    def display(self):
        print(self.name)

s = Student()
s.display()
