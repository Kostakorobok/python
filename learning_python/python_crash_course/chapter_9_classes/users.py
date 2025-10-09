class User:
    def __init__ (self, first_name, last_name, age, gender):
        self.first_name = first_name
        self.last_name = last_name
        self.age = age
        self.gender = gender
        self.login_attempts = 0

    def describe_user(self):
        print(f"First name: {self.first_name}\n"
              f"Last name: {self.last_name}\n"
              f"Age: {self.age}\n"
              f"Gender: {self.gender}\n"
              f"Login attempts: {self.login_attempts}")

    def greet_user(self):
        print(f"Welcome {self.first_name}\n")

    def increment_login_attempts(self):
        user_selection = input("Login? Y/N").lower()
        if user_selection == "y":
            self.login_attempts += 1

    def reset_login_attempts(self):
        self.login_attempts = 0

class Admin(User):
    def __init__(self, first_name, last_name, age, gender):
        super().__init__(first_name, last_name, age, gender)
        self.privileges = Privileges

    def describe_user(self):
        print(f"First name: {self.first_name}\n"
              f"Last name: {self.last_name}\n"
              f"Age: {self.age}\n"
              f"Gender: {self.gender}\n"
              f"Login attempts: {self.login_attempts}\n")

    def describe_privileges(self, firstName, priv):
        print(f"{firstName}:")
        for i in priv:
            print(f"- {i}")

class Privileges:
    def __init__(self, privileges):
        self.privileges = privileges

    def describe_privileges(self, firstName, priv):
        print(f"{firstName}:")
        for i in priv:
            print(f"- {i}")

admin_privileges = ["Can add", "Can delete", "Can edit", "Can Ban"]