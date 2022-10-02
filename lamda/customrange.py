def range(x,y):
    while x<y:
        yield x
        x+=1

y=range(10,30)
for i in y:print(i)