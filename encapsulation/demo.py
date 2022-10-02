class Demo:
    def __init__(self):
        self.__name="Manish"
        self.__age=24

    def display(self):
        print(self.__name)
        print(self.__age)

d=Demo()
d.display()
print(d._Demo__name) #nameMangling