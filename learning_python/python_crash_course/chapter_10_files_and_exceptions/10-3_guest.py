class User:
    def __init__(self, first_name, last_name):
        self.first_name = first_name
        self.lastname = last_name

file_name = "text_files/10-3_guest.txt"

with open(file_name, 'w') as file_object:
    user_name_first = input("Enter your first name\n")
    user_name_last = input("Enter your last name:\n")
    file_object.write(f"First name: {user_name_first}\nLast name: {user_name_last}\n")

