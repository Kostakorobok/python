from random import randint

class Dice:
    def __init__(self, sides = 6):
        self.sides = sides

    def roll_dice(self):
        # input("Roll the dice!")
        print(f"You've rolled {randint(1, self.sides)}\n")

running = True

dice6 = Dice()
dice10 = Dice(10)
dice20 = Dice(20)

while running:
    user_select = input("1. Roll 6 sided dice\n"
                   "2. Roll 10 sided dice\n"
                   "3. Roll 20 sided dice\n"
                   "4. Quit\n")
    if user_select == "1":
        dice6.roll_dice()
    elif user_select == "2":
        dice10.roll_dice()
    elif user_select == "3":
        dice20.roll_dice()
    elif user_select == "4":
        print("The end")
        running = False
    else:
        print("Wrong entry try again")