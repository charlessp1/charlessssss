class Car:

    def __init__(self, make, model, year, color):
        self.make = make
        self.model = model
        self.year = year
        self.color = color

    def drive(self):
        print('Driving this', self.model, 'car now')

    def stop(self):
        print('Stopping', self.model, 'car now')

