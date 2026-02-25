def log(func):
    def wrapper(*a, **k):
        print("start")
        r = func(*a, **k)
        print("end")
        return r
    return wrapper

@log
def add(a,b):
    return a+b

print(add(2,3))