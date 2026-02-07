#WAP convert the celsius to fharenheit


def c_to_f(f):
    return (f*9/5)+32

f = float(input("Enter a number : "))
print(f"The Fharenheit = {c_to_f(f)} f")