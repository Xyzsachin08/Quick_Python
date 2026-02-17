class X:
    def showX(self):
        print("Class X")

class Y:
    def showY(self):
        print("Class Y")

class Z(X, Y):
    def showZ(self):
        print("Class Z")

obj = Z()
obj.showX()
obj.showY()
obj.showZ()
