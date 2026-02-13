# Parent Class
class Animal:
    def speak(self):
        print("Animal is speaking")

# Child Class (Inheritance)
class Dog(Animal):
    def bark(self):
        print("Dog is barking")

# Create object of Dog class
d = Dog()

# Calling parent class method
d.speak()

# Calling child class method
d.bark()
