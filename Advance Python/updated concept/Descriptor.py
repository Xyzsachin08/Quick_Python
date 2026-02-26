class Age:
    def __get__(self,obj,objtype):
        return obj._age
    def __set__(self,obj,value):
        obj._age=value

class Person:
    age=Age()
    def __init__(self,a):
        self.age=a

p=Person(20)
print(p.age)