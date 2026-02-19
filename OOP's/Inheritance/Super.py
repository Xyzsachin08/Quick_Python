class Emplyoee:
    def __init__(self):
        print("This constructor is Emplyoee")
    a = 1
    
class Manager(Emplyoee):
    def __init__(self):
        #super().__init__()
        print("This constructor is Manager")
    b = 2
    
class Programmer(Manager):
    def __init__(self):
        super().__init__()
        print("This constructor is Programmer")
    c = 3
    
#o = Emplyoee()
#print(o.a)

#s = Manager()
#print(s.a, s.b)

n = Programmer()
print(n.a, n.b, n.c)