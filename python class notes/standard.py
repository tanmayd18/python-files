class school:
    def __init__(self,name,age):
        self.name=name
        self.age=age
    def display(self):
        print(self.name,self.age)
class standard(school):
    pass
a=standard("Tanmay",18)
a.display()
