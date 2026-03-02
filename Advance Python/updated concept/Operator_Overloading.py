class Point:
    def __init__(self,x,y):
        self.x=x
        self.y=y
    def __add__(self,o):
        return Point(self.x+o.x,self.y+o.y)

p1=Point(1,2)
p2=Point(3,4)
p3=p1+p2
print(p3.x,p3.y)