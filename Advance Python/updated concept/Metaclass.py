class Meta(type):
    def __new__(m,n,b,d):
        d["id"]=1
        return super().__new__(m,n,b,d)

class A(metaclass=Meta):
    pass

a=A()
print(a.id)