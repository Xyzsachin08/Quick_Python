from collections import ChainMap

a={"x":1}
b={"y":2}
c=ChainMap(a,b)
print(c["x"],c["y"])