#Create a class "Programmer" for storing information of few programmers working at microsoft. 



class Programmer:
    company = "Microsoft"
    def __init__(self, name, salary, pin):
        self.name = name
        self.salary = salary
        self.pin = pin
        
h1 = Programmer("Harry", 12345, 12345)
print(h1.name, h1.salary, h1.pin, h1.company)

s1 = Programmer("Sachin", 75000, 413701)
print(s1.company, s1.name,s1.salary, s1.pin)

n1 = Programmer("Nisanchu", 70000, 413701)
print(n1.pin, n1.company, n1.salary, n1.name)
        
