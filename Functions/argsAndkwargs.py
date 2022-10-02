def display(x,*args,**kwargs):
    print(x)
    for i in args:
        print(i)
    for key,value in kwargs.items():
        print(key , value)

display(10,20,30,40,name="Manish", salary="50000")