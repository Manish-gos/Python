def dec(fun):
    def inner():
        result=fun()*2
        return result
    return inner

def fun():
    return 5
g=dec(fun)
print(g())