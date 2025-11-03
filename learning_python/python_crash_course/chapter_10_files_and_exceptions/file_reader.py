file_name = 'text_files/pi_million_digits.txt'

with open(file_name) as file_object:
    lines = file_object.readlines()

pi_string = ''
for i in lines:
    pi_string += i.strip()

my_birthday = input("Enter your birthday in format ddmmyy:\n")
if my_birthday in pi_string:
    print("Your birthday appears in the first million digits of Pi")
else:
    print("Your birthday doesn't appear in the first million digits of Pi")
