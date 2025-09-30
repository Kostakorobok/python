class Car:
    """Simple car model"""

    def __init__ (self, make, model, year):
        """Initialises attributes to describe a car"""
        self.make = make
        self.model = model
        self.year = year
        self.odometer_reading = 0

    def descriptive_name(self):
        """Return neatly formatted descriptive name"""
        long_name = f"{self.make} {self.model} {self.year}"
        return long_name

    def read_odometer(self):
        """Shows car's mileage"""
        print(f"This car has {self.odometer_reading} miles on it")

car1 = Car("Audi", "A4", 2025)
print(car1.descriptive_name())

