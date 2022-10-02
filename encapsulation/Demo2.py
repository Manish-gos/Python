class Demo2:
    def setName(self,name):
        self.name=name

    def getName(self):
        return self.name

    def setAge(self,age):
        self.age=age

    def getAge(self):
        return  self.age

d=Demo2()
d.setAge(22)
d.setName("Manish")
print(d.getName())
print(d.getAge())

