class Car:
    pass

myCar = Car() 
print type(myCar) 


class Car:
    name = 'Sonanta'

    def drive(self):
        print 'run :', self.name

myCar = Car()
print type(myCar)
print myCar 
myCar.drive()
