class BMW:
    def __init__(self,make,model,year):
        self.make=make
        self.model=model
        self.year=year

    def start(self):
        print("Car is starting")

    def stop(self):
        print("Car is stopping")

class ThreeSeries(BMW):
    def __init__(self,threeSeries,make,model,year):
        BMW.__init__(self,make,model,year)
        self.threeseries=threeSeries

    def start(self):
        super().start()
        print("Button start")

class FiveSeries(BMW):
    def __init__(self,fiveSeries,make,model,year):
        super().__init__(make,model,year)
        self.fiveseries=fiveSeries

t=ThreeSeries(True,"BMW","320i","2022")
print(t.year)
print(t.model)
print(t.make)
print(t.threeseries)
t.start()
t.stop()