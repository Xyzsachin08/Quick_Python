class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def display_person(self):
        print("Name:", self.name)
        print("Age:", self.age)


class Student(Person):
    def __init__(self, name, age, roll_no, branch):
        super().__init__(name, age)
        self.roll_no = roll_no
        self.branch = branch

    def display_student(self):
        self.display_person()
        print("Roll No:", self.roll_no)
        print("Branch:", self.branch)


s1 = Student("Sachin", 19, 101, "Computer Engineering")

s1.display_student()

s2 = Student("Rahul", 20, 102, "Mechanical Engineering")

print()
s2.display_student()
