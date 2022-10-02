class Student:
    major="CSE"

    def __init__(self,name,rollno):
        self.name=name
        self.rollno=rollno

    def display(self):
        print(self.name)
        print(self.rollno)
        print(self.major)

s1=Student("Manish",21)
s1.display()
s2=Student("Akash",24)
s2.display()