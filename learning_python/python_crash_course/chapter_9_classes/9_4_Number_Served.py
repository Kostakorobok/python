class Restaurant:
    """An attempt to model a restaurant"""
    def __init__ (self, restaurant_name, cuisine_type, number_served = 0):
        self.restaurant_name = restaurant_name
        self.cuisine_type = cuisine_type
        self.number_served = number_served

    def describe_restaurant(self):
        print(f"Restaurant name: {self.restaurant_name}\n"
              f"Food type: {self.cuisine_type}\n"
              f"Number served: {self.number_served}\n")

    def set_number_served(self, a):
        self.number_served = a
        return a

    def increment_number_served(self, b):
        self.number_served += b

running = True
# user_selection = ""

restaurant_1 = Restaurant("Italianaria", "Italian food")
restaurant_1.set_number_served(0)

while running:
    user_selection = input("Increment number served?\n"
                           "1. Yes\n"
                           "2. No\n"
                           "3. Describe restaurant\n"
                           "4. View number of customers\n"
                           "5. Quit\n").lower()
    if user_selection == "1":
        c = int(input(f"Enter the incremental increase in customers:\n"))
        restaurant_1.increment_number_served(c)
    elif user_selection == "2":
        continue
    elif user_selection == "3":
        restaurant_1.describe_restaurant()
    elif user_selection == "4":
        print(f"Restaurant served {restaurant_1.number_served} people")
    elif user_selection == "5":
        running = False
    else:
        print("Wrong entry, try again")
