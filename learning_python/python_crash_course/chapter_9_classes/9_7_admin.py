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

class Privileges:
    def __init__(self, privileges):
        self.privileges = privileges

    def describe_privileges(self, firstName, priv):
        print(f"{firstName}:")
        for i in priv:
            print(f"- {i}")

running = True
admin_priv = ["can add post", "can edit post", "can delete post"]
admin1_privileges = Privileges(admin_priv)

user1 = User("Anna", "Vichitra", "30", "female")
user2 = User("Costa", "Mathew", 34, "male")
user3 = User("Jeffrey", "Epstein", 50, "male")

admin1 = Admin("Elon", "Musk", 50, "male")

while running:
    user_select = input(f"Select user:\n"
                        f"1. {user1.first_name} {user1.last_name}\n"
                        f"2. {user2.first_name} {user2.last_name}\n"
                        f"3. {user3.first_name} {user3.last_name}\n"
                        f"4. {admin1.first_name} {admin1.last_name}\n"
                        f"5. Reset all logins\n"
                        f"6. Quit\n")
    if user_select == "1":
        user1.greet_user()
        user1.describe_user()
        user1.increment_login_attempts()
    elif user_select == "2":
        user2.greet_user()
        user2.describe_user()
        user2.increment_login_attempts()
    elif user_select == "3":
        user3.greet_user()
        user3.describe_user()
        user3.increment_login_attempts()
    elif user_select == "4":
        admin1.greet_user()
        admin1.describe_user()
        admin1_privileges.describe_privileges(admin1.first_name, admin_priv)
        admin1.increment_login_attempts()
    elif user_select == "5":
        for i in (user1, user2, user3, admin1):
            i.reset_login_attempts()
    elif user_select == "6":
        running = False
    else:
        print("Wrong entry, try again")
