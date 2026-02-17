class Father:
    def show(self):
        print("Father Method")

class Son(Father):
    def show(self):
        print("Son Method")

s = Son()
s.show()
