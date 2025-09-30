class User:
    def __init__ (self, first_name, last_name, age, gender):
        self.first_name = first_name
        self.last_name = last_name
        self.age = age
        self.gender = gender

    def describe_user(self):
        print(f"First name: {self.first_name}\n"
              f"Last name: {self.last_name}\n"
              f"Age: {self.age}\n"
              f"Gender: {self.gender}\n")

    def greet_user(self):
        print(f"Welcome {self.first_name} {self.last_name}")

user1 = User("Anna", "Vichitra", "30", "female")
user2 = User("Costa", "Mathew", 34, "male")
user3 = User("Jeffrey", "Epstein", 50, "male")

user1.describe_user()
user2.describe_user()
user3.describe_user()

user1.greet_user()
