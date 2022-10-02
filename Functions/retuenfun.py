def display(name):
    def message():
        return "Hello "+name
    return message
fun=display("manish")
print(fun())