class ToYoung:
    def __init__(self,msg):
        self.msg=msg

class ToOld:
    def __init__(self,msg):
        self.msg=msg

age=int(input("Enter your age"))

if age>90:
    raise ToOld("You are to old for a licence max age is 90")

if age<18:
    raise ToOld("You are to young for a licence min age is 18")

else:
    print("You are eligible")