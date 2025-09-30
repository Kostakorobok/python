
class Dog:
    """A simple attempt to model a dog."""

    def __init__(self, name, age):
        """Initialise name and age attributes"""
        self.name = name
        self.age = age

    def sit(self):
        """Simulate a dog sitting in response to a command."""
        print(f"{self.name} is now sitting.")

    def roll_over(self):
        """Simulate rolling over in response to a command"""
        print(f"{self.name} rolled over!")

my_dog_1 = Dog("Huxley", 3)
my_dog_2 = Dog("Boofy", 1)

print(f"First dog: {my_dog_1.name}, {my_dog_1.age} years old\nSecond dog: {my_dog_2.name}, {my_dog_2.age} years old")

my_dog_2.roll_over()
