from functools import partial

def power(a,b):
    return a**b

square=partial(power,b=2)
print(square(5))