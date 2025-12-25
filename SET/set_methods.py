s = {1,2,3,4,"sachin"}
print(s,type(s))

s.add(344)
print(s)

s.add("bhushan")
print(s)

s.add(0)
print(s)

#update
s.update([5,6,9])
print(s)


#remove   (at a time only one elements delete)
s.remove(5)
print(s)

#discard
s.discard(0) 
print(s)


#union
a= {1,2,3}
b= {2,1,4,5,6}
print(a.union(b))

#intersection
print(a.intersection(b))

#difference   (only on first set)
print(a.difference(b))

#issubset  (check if one set is part of another)
print(a.issubset(b))