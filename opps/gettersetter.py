class Proggramer:

    def setName(self,n):
        self.name=n

    def getName(self):
        return self.name

    def setSalary(self,s):
        self.salary=s

    def getSlalry(self):
        return self.salary

    def setTech(self,tech):
        self.technology=tech

    def getTech(self):
        return self.technology

p1=Proggramer()
p1.setName("Manish")
p1.setSalary(500000)
p1.setTech(["java","spark","hadoop"])

print(p1.getName())
print(p1.getSlalry())
print(p1.getTech())