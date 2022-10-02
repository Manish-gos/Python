class Flight:
    def __init__(self,engin):
        self.engin=engin

    def startEngin(self):
        self.engin.start()

class AirbunEngin:
    def start(self):
        print("Starting Airban Engin")

class BoingEngin:
    def start(self):
        print("Starting Boing Engin")

ae=AirbunEngin()
f=Flight(ae)
f.startEngin()

be=BoingEngin()
f1=Flight(be)
f1.startEngin()