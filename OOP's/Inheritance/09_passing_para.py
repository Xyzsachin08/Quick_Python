class Person:
    def __init__(self, name):
        self.name = name

class Student(Person):
    def show(self):
        print(self.name)

s = Student("Rahul")
s.show()
