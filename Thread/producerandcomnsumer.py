from threading import Thread, Condition
from time import sleep


class Producer:
    def __init__(self):
        self.product=[]
        #self.remflag=False
        self.c=Condition()

    def addProduct(self):
        self.c.acquire()
        for i in range(1,5):
            self.product.append("Product"+str(i))
            sleep(1)
            print("item added- Product",str(i))
           # self.remflag=True
        self.c.notifyAll()
        self.c.release()

class Consumer:
    def __init__(self,prod):
        self.prod=prod

    def checkConsume(self):
        self.prod.c.acquire
        self.prod.c.wait(timeout=0)
        self.prod.c.release
        #while self.prod.remflag == False:
           # sleep(0.2)
          #  print("Order is preparing")

        print("Order is processed")

p=Producer()
c=Consumer(p)

t=Thread(target=p.addProduct)
t1=Thread(target=c.checkConsume)

t.start()
t1.start()
