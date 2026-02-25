class File:
    def __enter__(self):
        self.f=open("demo.txt","w")
        return self.f
    def __exit__(self,a,b,c):
        self.f.close()

with File() as f:
    f.write("hello")