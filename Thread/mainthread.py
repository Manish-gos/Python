import threading

print("Current thread is: ",threading.current_thread().getName())

if threading.current_thread()==threading.main_thread():
    print("Main thread is running")
else:
    print("Some other thread is running")