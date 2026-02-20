# len vector

class Vector:
    def __init__(self,data):
        self.data=data

    def __len__(self):
        return len(self.data)

v = Vector([1,2,3])
print(len(v))