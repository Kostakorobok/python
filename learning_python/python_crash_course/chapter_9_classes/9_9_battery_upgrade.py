class Car:
    """Simple car model"""

    def __init__ (self, make, model, year, odometer_reading):
        """Initialises attributes to describe a car"""
        self.make = make
        self.model = model
        self.year = year
        self.odometer_reading = odometer_reading

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

class PetrolCar(Car):
    """Represents aspects of a Petrol car"""
    def __init__(self, make, model, year, odometer_reading):
        """initialises atributes of parent car"""
        super().__init__(make, model, year, odometer_reading)
        self.gas_tank = GasTank()

    def refill(self):
        fuel = int(input("Enter the amount of petrol to put in the car: "))
        self.gas_tank += fuel

class ElectricCar(Car):
    """Represents aspects of a car specific to electric vehicles"""
    def __init__(self, make, model, year, odometer_reading):
        """Initialise attributes of parent car"""
        super().__init__(make, model, year, odometer_reading)
        self.battery = Battery()

    def fill_gas_tank(self):
        """notify user that EV doesn't have a gas tank"""
        print("EVs dont use gas!")

class Battery:
    """Models an EV battery"""
    def __init__(self, battery_size = 75, battery_range = 250):
        self.battery_size = battery_size
        self.battery_range = battery_range

    def describe_battery(self):
        print(f"Battery size: {self.battery_size}-kWh\n"
              f"Battery range: {self.battery_range}-km\n")

    def install_75kwh_battery(self):
        self.battery_size = 75
        self.battery_range = 250

    def install_100kwh_battery(self):
        self.battery_size = 100
        self.battery_range = 300

class GasTank:
    """Models petrol tank for combustion car"""
    def __init__ (self, tank_capacity = 65):
        self.tank_capacity = tank_capacity

    def read_gas_tank(self):
        print(f"There is {self.tank_capacity} liters of petrol in the tank")

running = True

petrol_car1 = PetrolCar("Honda", "Accord", 2012, 100000)
ev_car1 = ElectricCar("Tesla", "Model S", 2019, 1000)

while running:
    user_select = int(input(f"Car Registry:\n"
                        f"1. {petrol_car1.make}\n"
                        f"2. {ev_car1.make}\n"
                        f"3. Quit \n"))

    if user_select == 1:
        print(petrol_car1.descriptive_name())
        user_select = int(input("1. Odometer reading\n"
                            "2. Back\n"))
        if user_select == 1:
            petrol_car1.read_odometer()
        elif user_select == 2:
            continue
        else:
            print("Wrong Entry")

    elif user_select == 2:
        print(ev_car1.descriptive_name())
        user_select = int(input("1. Odometer reading\n"
                            "2. Battery settings\n"
                            "3. Back\n"))
        if user_select == 1:
            ev_car1.read_odometer()
        elif user_select == 2:
            user_select = int(input(f"1. View current battery\n"
                                f"2. Install 75kWh battery\n"
                                f"3. Install 100kWh battery\n"
                                f"4. Back\n"))
            if user_select == 1:
                ev_car1.battery.describe_battery()
            elif user_select == 2:
                ev_car1.battery.install_75kwh_battery()
            elif user_select == 3:
                ev_car1.battery.install_100kwh_battery()
            elif user_select == 4:
                continue
            else:
                print("Wrong entry, try again")
        elif user_select == 3:
            continue
        else:
            print("Wrong Entry")

    elif user_select == 3:
        running = False

    else:
        print("Wrong entry, try again")