from threading import *
from time import sleep


class UsingClass:
    def display(self):
        print(current_thread().getName())
        i=0
        sleep(1)
        while i<=20:
            print(i)
            i+=1

print(current_thread().getName())
obj=UsingClass()

t=Thread(target=obj.display)
t.start()

t1=Thread(target=obj.display)
t1.start()

t2=Thread(target=obj.display)
t2.start()