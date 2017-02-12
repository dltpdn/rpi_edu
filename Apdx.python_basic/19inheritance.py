class Car(object):
    engine =None

    def __init__(self, engine):
        self.engine = engine

    def drive(self):
        if self.engine ==None:
            print"can't drive caused by no engine"
        else:
            print'driving..'


class SuperCar(Car):
    def __init__(self, engine):
        super(SuperCar, self).__init__(engine)
        #Car.__init__(self, engine)
    def driveFast(self):
        print'driving fast very much...'


car = Car(2)
car.drive()

scar = SuperCar(3)
scar.drive()
scar.driveFast()