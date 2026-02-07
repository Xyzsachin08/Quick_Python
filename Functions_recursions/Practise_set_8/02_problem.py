#WAP using function to convert Celsius to Fahrenheit


def c_to_f(c):
    return  (c-32)*5/9

c = float(input("Enter a number: "))
print(c_to_f(c))