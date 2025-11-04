# 10-6 and 10-7
running = True

while running:
    try:
        user_choice = input("Simple addition calculator for 2 numbers.\n1. Run calculator\n2. Quit\n")
        try:
            if user_choice == "1":
                try:
                    first_number = input("First number: ")
                    if first_number == "q":
                        break
                    second_number = input("Second number: ")
                    if second_number == "q":
                        break
                    first_number_int = int(first_number)
                    second_number_int = int(second_number)
                    print(f"Result = {first_number_int + second_number_int}")
                except ValueError:
                    print("Cannot add non-integer values, try again")
                except KeyboardInterrupt:
                    print("Program incorrectly terminated")
                    break
            elif user_choice == "2":
                running = False
            else:
                print("Wrong entry try again")
        except KeyboardInterrupt:
            print("\nProgram incorrectly terminated")
            break
    except KeyboardInterrupt:
        print("\nProgram incorrectly terminated")
        break