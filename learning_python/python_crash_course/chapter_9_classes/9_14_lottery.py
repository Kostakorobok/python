from random import choice

lottery_choice = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, "a", "h", "e", "m", "u"]
a = 4
winning_ticket = []
my_ticket = []
tries = 0

running = True

for i in range(a):
    winning_ticket.append(choice(lottery_choice))

while running:
    my_ticket = []
    for i in range(a):
        my_ticket.append(choice(lottery_choice))

    if my_ticket == winning_ticket:
        tries += 1
        print(f"You win after {tries} tickets\n"
              f"winning ticket: {winning_ticket}\n"
              f"my ticket: {my_ticket}")

        running = False
    elif tries == 100000:
        print(f"You've won nothing after buying {tries} tickets")
        running = False
    else:
        tries += 1
        print(tries)