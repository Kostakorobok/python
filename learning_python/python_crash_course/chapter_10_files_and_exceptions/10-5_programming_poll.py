file_name = "text_files/10-5_programming_poll.txt"
running = True

while running:
    user_input = input("1. Reason you like programming\n"
                       "2. View File\n"
                       "3. Quit\n")
    if user_input == "1":
        with open(file_name, "a") as file_object:
            user_name = input(f"Enter your name:\n")
            user_reasons = input(f"Why do you like programming?\n")
            file_object.write(f"{user_name}:\n{user_reasons}\n")
    elif user_input == "2":
        with open(file_name, "r") as file_object:
            lines_string = ""
            lines = file_object.readlines()
            for i in lines:
                lines_string += i
            print(lines_string)
    elif user_input == "3":
        running = False
    else:
        input("Wrong entry, hit Enter to continue...")
