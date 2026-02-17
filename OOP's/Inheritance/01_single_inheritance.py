class Parent:
    def show(self):
        print("Parent Class")

class Child(Parent):
    def display(self):
        print("Child Class")

obj = Child()
obj.show()
obj.display()
