n = int(input("Enter a number: "))

number = 1
for i in range(1, n+1):
    number = number*i
print(f"the factorial {n} is {number}")