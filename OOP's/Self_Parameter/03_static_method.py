class Student:
    age = 85
    std = 96
    roll_no = 45
    clg_name = "trinity"
    
    def raj(self):
        print(f"The age of student is {self.age} and roll no is {self.roll_no} and clg name is{self.clg_name} the standard is {self.std}")
    @staticmethod      
    def mahesh():
        print("Good Morning")
        
s1 =  Student()
s1.raj()
s1.mahesh()
print(s1)
