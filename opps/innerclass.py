class Car:

    def __init__(self,name,model):
        self.name=name
        self.model=model

    def display(self):
        print(self.name)
        print(self.model)

    class Engine:
        def __init__(self,num):
            self.number=num

        def start(self):
            print("Car is started")
            print(self.number)

c=Car("Verna","CSI")
c.display()
e=c.Engine(1234)
e.start()