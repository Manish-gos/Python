x=123
y=234
print(x , y)
def display():
    y=999
    x=255
    print(globals()['x'])
    print(x, y)

display()
#assign a function to a variable
z=display
z()
z()
