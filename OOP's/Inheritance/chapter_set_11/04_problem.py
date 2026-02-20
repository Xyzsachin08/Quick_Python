# Complex + and *

class Complex:
    def __init__(self, r, i):
        self.r = r
        self.i = i

    def __add__(self, o):
        return Complex(self.r + o.r, self.i + o.i)

    def __mul__(self, o):
        return Complex(self.r*o.r - self.i*o.i, self.r*o.i + self.i*o.r)

    def show(self):
        print(self.r, "+", self.i, "i")

a = Complex(1,2)
b = Complex(3,4)
(a+b).show()
(a*b).show()