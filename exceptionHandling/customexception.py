class ovrthelimit(Exception):
    def __init__(self,msg):
        self.msg=msg

def withdraw(ammount):
    if(ammount>500):
        raise ovrthelimit("you can not withdarw more then 500$ in a day")

withdraw(600)