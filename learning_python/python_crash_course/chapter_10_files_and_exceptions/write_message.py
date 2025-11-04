file_name = "text_files/programming.txt"

with open(file_name, "w") as file_object:
    file_object.write("I love programming.\n")
    file_object.write("I love creating new games.\n")

with open(file_name, "a") as file_object:
    file_object.write("I also love finding meaning in large databases.\n")
    file_object.write("I also love creating apps that can run in a browser.\n")

