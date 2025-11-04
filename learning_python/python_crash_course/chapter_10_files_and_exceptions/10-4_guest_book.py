running = True
file_name = "text_files/10-4_guest_book.txt"
file_object_str = ""

while running:
    user_input = input("1. Enter your name\n"
                       "2. View Registry\n"
                       "3. Quit\n")
    if user_input == "1":
        with open(file_name, "a") as file_object:
            user_input_first_name = input("First name:\n")
            user_input_last_name = input("Last name:\n")
            file_object.write(f"{user_input_first_name} {user_input_last_name} logged in\n")

    elif user_input == "2":
        with open(file_name, "r") as file_object:
            lines = file_object.readlines()
            for i in lines:
                file_object_str += i

            print(file_object_str)

    elif user_input == "3":
        running = False

    else:
        input("Wrong entry, hit enter to continue...")

