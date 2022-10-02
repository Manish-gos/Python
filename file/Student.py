class Student:
    def __init__(self,rollNo,name,testScore):
        self.rollNo=rollNo
        self.name=name
        self.testScore=testScore

    def display(self):
        print(self.rollNo,self.name,self.testScore)
