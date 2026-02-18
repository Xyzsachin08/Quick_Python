class Parent:
    def show(self):
        print("Hello from Parent")

class Child(Parent):
    def display(self):
        Parent.show(self)

c = Child()
c.display()
