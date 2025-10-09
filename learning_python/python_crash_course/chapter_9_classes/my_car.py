import car

car1 = car.Car("Audi", "A4", 2025)
print(car1.descriptive_name())
car1.read_odometer()
car1.update_odometer(23)
car1.read_odometer()
a = int(input("Enter odometer incrementation:\n"))
car1.increment_odometer(a)

user_input = input("Show new milage? Y/N\n").lower()
if user_input == "y":
    car1.read_odometer()

user_input = input("Increase again? Y/N\n").lower()
if user_input == "y":
    a = int(input("Enter odometer incrementation:\n"))
    car1.increment_odometer(a)

user_input = input("Show new milage? Y/N\n").lower()
if user_input == "y":
    car1.read_odometer()