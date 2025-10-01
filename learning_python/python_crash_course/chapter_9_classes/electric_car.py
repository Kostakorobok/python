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

    def update_odometer(self, mileage):
        """Simple method to update car's odometer
        Reject if attempting to roll back the odometer"""
        if mileage > self.odometer_reading:
            self.odometer_reading = mileage
        else:
            print("You cannot roll back the odometer!")

    def increment_odometer(self, miles):
        """Add an increment amount to odometer reading"""
        self.odometer_reading += miles

class ElectricCar(Car):
    """Represents aspects of a car specific to electric vehicles"""
    def __init__(self, make, model, year):
        """Initialise attributes of parent car"""
        super().__init__(make, model, year)
        self.battery_size = 75

    def describe_battery(self):
        """Prints a statement describing battery size"""
        a = f"{self.make} has {self.battery_size}-kWh battery"
        return a

my_tesla = ElectricCar("Tesla", "Model S", 2025)
print(f"{my_tesla.descriptive_name()}\n"
      f"{my_tesla.describe_battery()}\n")
