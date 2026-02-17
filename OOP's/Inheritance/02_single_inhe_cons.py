class Animal:
    def __init__(self):
        print("Animal Created")

class Dog(Animal):
    def bark(self):
        print("Dog Barking")

d = Dog()
d.bark()
