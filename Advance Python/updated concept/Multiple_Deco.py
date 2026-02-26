def d1(f):
    def w(*a,**k):
        print("d1")
        return f(*a,**k)
    return w

def d2(f):
    def w(*a,**k):
        print("d2")
        return f(*a,**k)
    return w

@d1
@d2
def hello():
    print("hello")

hello()