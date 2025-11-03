file_path = "text_files/10-1_learning_pythong_txt_file.txt"

with open(file_path) as project_file:
    lines = project_file.readlines()

project_file_string = ""
for i in lines:
    project_file_string += i

print(project_file_string)
project_file_string = project_file_string.replace("Python", "C")
print(project_file_string)
