class Duck:
    def talk(self):
        print("Quake Quake")

class Human:
    def talk(self):
        print("Hello")


def callTalk(obj):
    obj.talk()

d=Duck()
callTalk(d)

h=Human()
callTalk(h)
