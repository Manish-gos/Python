class ObjectCounter:
    noOfObject=0
    def __init__(self):
        ObjectCounter.noOfObject+=1
    @staticmethod
    def display():
        print(ObjectCounter.noOfObject)

o1=ObjectCounter()
o2=ObjectCounter()
ObjectCounter.display()