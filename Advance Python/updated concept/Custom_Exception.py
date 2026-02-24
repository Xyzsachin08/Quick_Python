class MyError(Exception):
    pass

def check(n):
    if n<0:
        raise MyError("negative")
    return n

print(check(5))