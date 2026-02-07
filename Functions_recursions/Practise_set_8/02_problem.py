#WAP using function to convert Fahreneit to Celsius


def c_to_f(c):
    return  (c-32)*5/9

c = float(input("Enter a number: "))
print(c_to_f(c))