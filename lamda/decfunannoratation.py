def dec(fun):
    def inner():
        result=fun()*2
        return result
    return inner
@dec
def fun():
    return 5

print(fun())