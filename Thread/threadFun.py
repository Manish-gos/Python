from threading import *

def display():
    print(current_thread().getName())
    i=0
    while i<=20:
        print(i)
        i+=1

print(current_thread().getName())
t=Thread(target=display)
t.start()