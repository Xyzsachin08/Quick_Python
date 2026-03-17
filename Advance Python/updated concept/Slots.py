class User:
    __slots__=("name","age")
    def __init__(self,n,a):
        self.name=n
        self.age=a

u=User("Sachin",19)
print(u.name)