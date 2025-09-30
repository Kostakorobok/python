class Restaurant:
    """An attempt to model a restaurant"""
    def __init__ (self, restaurant_name, cuisine_type):
        self.restaurant_name = restaurant_name
        self.cuisine_type = cuisine_type

    def describe_restaurant(self):
        print(f"Restaurant name: {self.restaurant_name}")
        print(f"Restaurant type: {self.cuisine_type}")

restaurant_1 = Restaurant("Italianaria", "Italian food")
restaurant_2 = Restaurant("Drinkaira", "Wine bar")
restaurant_3 = Restaurant("Chineseria", "Chinese food")

restaurant_1.describe_restaurant()
restaurant_2.describe_restaurant()
restaurant_3.describe_restaurant()
