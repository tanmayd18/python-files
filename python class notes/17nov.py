'''class name:
    def __init__(self,name,age):
        self.age=age
        self.name=name
    def __str__(self):
        return f"{self.name}{self.age}"
a=name("Hena",8)
print(a)'''
class school:
    def __init__(self,name):
        self.name=name
    def add(self):
        print("My Name is "+self.name)
a=school("Tanmay")
a.add()
