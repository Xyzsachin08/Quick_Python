class Sachin:
    name = "default name"
    company = "Tudip Tech"
    def sachin(self):
        print(f"The name of the sachin class is{self.name} and company is {self.company}")
        
class Bhushan:
    roll_no = 3011
    company = "proazure"
    def bhushan(self):
        print(f"The name of the bhushan is {self.roll_no} and company is {self.company}")
        
class Raj(Sachin, Bhushan):
    def raj(self):
        print("Hi i am a raj")
        
        
a = Raj()
a.sachin()
a.bhushan()
a.raj()