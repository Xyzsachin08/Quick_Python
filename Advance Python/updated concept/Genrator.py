def count(n):
    i=0
    while i<n:
        yield i
        i+=1

for x in count(5):
    print(x)