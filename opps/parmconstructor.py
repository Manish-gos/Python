class Product:
    def __init__(self,name,description,price,rating):
        self.name=name
        self.description=description
        self.price=price
        self.ratings=rating
        
    def average(self):
        length=len(self.ratings)
        av=sum(self.ratings)/length
        print("For ptoduct ",self.name," rating is ",av)

p1=Product("Iphone","is good",800,[1,3,4,5,3,2,4,5])
print(p1.name)
print(p1.description)
print(p1.price)
p1.average()

p2=Product("Iphone X","is too good",1000,[5,5,5,5,5])
print(p2.name)
print(p2.description)
print(p2.price)
p2.average()