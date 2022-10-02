from threading import *

class MyBus:
    def __init__(self,availableseats):
        self.availableseats=availableseats
        #self.l=Lock()
        self.l = Semaphore()

    def bookseats(self,requestedseats):
        self.l.acquire()
        print("Total available seats ",self.availableseats)
        if self.availableseats>=requestedseats:
            print("Booking ticket")
            print("Processing the payment")
            print("Tickit booked successfully")
            self.availableseats-=requestedseats
        else:print("Sorry ! No ticket available")
        self.l.release()

obj=MyBus(10)
t=Thread(target=obj.bookseats,args=(3,))
t1=Thread(target=obj.bookseats,args=(3,))
t2=Thread(target=obj.bookseats,args=(4,))
t3=Thread(target=obj.bookseats,args=(3,))

t.start()
t1.start()
t2.start()
t3.start()
