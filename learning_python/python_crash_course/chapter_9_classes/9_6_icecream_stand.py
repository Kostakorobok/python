class Restaurant:
    """An attempt to model a restaurant"""
    def __init__ (self, restaurant_name, cuisine_type, menu):
        self.restaurant_name = restaurant_name
        self.cuisine_type = cuisine_type
        self.menu = menu

    def describe_restaurant(self):
        print(f"Restaurant name: {self.restaurant_name}")
        print(f"Restaurant type: {self.cuisine_type}")

class IceCreamStand(Restaurant):
    """Modeling an icecream stand of Restaurant class"""
    def __init__(self, restaurant_name, cuisine_type, menu):
        super().__init__(restaurant_name, cuisine_type, menu)
        self.cuisine_type = "Icecream shop"

class IceCream:
    def __init__ (self, flavour, cost):
        self.flavour = flavour
        self.cost = cost

    def describe_icecream(self):
        print(f"{self.flavour}, ${self.cost}")


vanilla = IceCream("Vanilla", 2)
chocolate = IceCream("Chocolate", 3.45)
strawberry = IceCream("Strawberry", 2.35)
icecream_list = [vanilla, chocolate, strawberry]

icecreamstand1 = IceCreamStand("Chef's Creamy Treats", cuisine_type = "icecream shop", menu = icecream_list)
icecreamstand1.describe_restaurant()
print(f"\n{icecreamstand1.restaurant_name} has following flavours:")
for i in icecreamstand1.menu:
    i.describe_icecream()
