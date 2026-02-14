class Demo:
    @staticmethod     #static nahi define kel tr te object sobat kam krt nahi 
    def show():
        print("Hello Static Method")

#Demo.show()   # Calling using class name
d1 = Demo()
d1.show()