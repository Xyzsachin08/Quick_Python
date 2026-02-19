class Employee:
    a =1
    @classmethod
    def show(cls): #Don't use the self use cls
        print(f"The class attribute of a is{cls.a}")
        
e = Employee()
e.a=45

e.show()