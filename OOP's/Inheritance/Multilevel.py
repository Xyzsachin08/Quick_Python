class Emplyoee:
    a = 1
    
class Manager(Emplyoee):
    b = 2
    
class Programmer(Manager):
    c = 3
    
o = Emplyoee()
print(o.a)

s = Manager()
print(s.a, s.b)

n = Programmer()
print(n.a, n.b, n.c)