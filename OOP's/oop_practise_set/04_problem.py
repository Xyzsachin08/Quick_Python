# add a static method in problem 2, to greet the user with hello.
class Calculator:
    def __init__(self, n):
        self.n = n
        
    def square(self):
        print(f"The square is{self.n*self.n}")
        
    def cube(self):
        print(f"The cube is{self.n*self.n*self.n}")
        
    def squareroot(self):
        print(f"The square root is{self.n**1/2}")
       
    @staticmethod
    def hello():
        print("Hello There!")
        
c1 = Calculator(4)
c1.square()
c1.squareroot()
c1.cube()