#Vector n dimension + and *

class Vector:
    def __init__(self, data):
        self.data = data

    def __add__(self, o):
        return Vector([a+b for a,b in zip(self.data,o.data)])

    def __mul__(self, o):
        return sum(a*b for a,b in zip(self.data,o.data))

v1 = Vector([1,2,3])
v2 = Vector([4,5,6])
print((v1+v2).data)
print(v1*v2)