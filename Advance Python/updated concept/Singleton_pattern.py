class Singleton:
    _i=None
    def __new__(c,*a,**k):
        if not c._i:
            c._i=super().__new__(c)
        return c._i

a=Singleton()
b=Singleton()
print(a is b)