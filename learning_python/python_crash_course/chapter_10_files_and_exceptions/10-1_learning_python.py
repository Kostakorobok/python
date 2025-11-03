file_path = "text_files/10-1_learning_pythong_txt_file.txt"

with open(file_path) as project_file:
    lines = project_file.readlines()

print(f"{lines}\n")

for i in lines:
    print(i)

project_file_string = ""
for i in lines:
    project_file_string += i

print(project_file_string)