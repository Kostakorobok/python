# class Solution:
#     def romanToInt(self, s:str) -> int:

def roman_to_int(r_number):
    I = 1
    V = 5
    X = 10
    L = 50
    C = 100
    D = 500
    M = 1000
    int_number1 = 0
    for i in r_number:
        if i == "I":
            int_number1 += I
        elif i == "V":
            int_number1 += V
        elif i == "X":
            int_number1 += X
        elif i == "L":
            int_number1 += L
        elif i == "C":
            int_number1 += C
        elif i == "D":
            int_number1 += D
        elif i == "M":
            int_number1 += M
        else:
            print("Entry outside of roman syntax")

    return int_number1

roman_number = []
integer_number = 0
user_input = input("Enter roman number:\n")

for i in user_input:
    roman_number.append(i)

integer_number = roman_to_int(roman_number)

print(f"Roman number: {roman_number}\n"
      f"Integer equivalent: {integer_number}")