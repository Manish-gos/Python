def calc(a,b):
    w=a+b
    x=a-b
    y=a*b
    z=a/b
    return w,x,y,z

res=calc(20,10)
for i in res:
    print(i)