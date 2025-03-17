class Car:


    def __init__(self,make,model,year):
        self.model = model
        self.make = make
        self.year = year


    def start(self):
        print(f"{self.make} {self.model} {self.year} is starting")


car = Car("ford","mustang","1969")

car.start()
