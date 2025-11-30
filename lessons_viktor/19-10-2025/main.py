import tkinter as tk
from PIL import Image, ImageTk
import random

class Snake(tk.Canvas):
    def __init__(self, root, width=600, length=620, colour="black", line_thickness=0):
        super().__init__(root,
                         width=width,
                         height=length,
                         bg=colour,
                         highlightthickness=line_thickness
                         )
        self.snake_positions = [(100, 100), (80, 100), (60, 100)]
        self.food_positions = self.set_food_positions()
        self.root = root
        self.width = width
        self.length = length
        self.colour = colour
        self.line_thickness = line_thickness
        self.food_photo = None
        self.photo_snake = None
        self.direction = "Right"
        # from func create_images

        self.load_assets()
        self.pack()
        self.start_game()

    def start_game(self):
        self.bind_all("<Key>", self.change_direction)
        self.game_loop()
        # set positions

    def update_graphics(self):
        self.delete("snake")
        for x_snake, y_snake in self.snake_positions:
            self.create_image(x_snake, y_snake, image=self.photo_snake, tag="snake")
        x_food, y_food = self.food_positions  # !!!!!
        self.create_image(x_food, y_food, image=self.food_photo, tag="food")

    def game_loop(self):
        self.move_snake()
        self.update_graphics()
        root.after(200, self.game_loop)

    def move_snake(self):

        # Get the current head position (first element in the list)
        sneak_head_x, sneak_head_y = self.snake_positions[0]
        new_head = 0

        if self.direction == "Right":
            new_head = (sneak_head_x + 20, sneak_head_y)
        elif self.direction == "Left":
            new_head = (sneak_head_x - 20, sneak_head_y)
        elif self.direction == "Up":
            new_head = (sneak_head_x, sneak_head_y - 20)
        elif self.direction == "Down":
            new_head = (sneak_head_x, sneak_head_y + 20)

        # Add the new head at the front, remove the last segment
        # This creates the illusion of movement :-1
        self.snake_positions = [new_head] + self.snake_positions[:-1]
        # 120, 100, [(100, 100), (80, 100) -> move right

        # https://www.youtube.com/watch?v=ajrtAuDg3yw

    def change_direction(self, event):  # no turn on 180
        key = event.keysym
        if key == "Up" and self.direction != "Down":
            self.direction = "Up"
        if key == "Down" and self.direction != "Up":
            self.direction = "Down"
        if key == "Left" and self.direction != "Right":
            self.direction = "Left"
        if key == "Right" and self.direction != "Left":
            self.direction = "Right"

    def check_boundaries(self):
        pass

    def load_assets(self):
        try:
            self.food_image = Image.open("assets/food.png")
            self.snake_image = Image.open("assets/snake.png")
            self.food_photo = ImageTk.PhotoImage(self.food_image)
            self.photo_snake = ImageTk.PhotoImage(self.snake_image)
        except IOError as error:
            print(f"{error}")
            root.destroy()

    def set_food_positions(self):
        return (random.randint(0, 300), random.randint(0, 300))  # experiment


root = tk.Tk()  # This is window
# tk.Tk() is the command in Python's tkinter library to create the main application window
root.title("Show assets!")
root.resizable(False, False)
board = Snake(root)

root.bind('<Left>', board.change_direction)
root.bind('<Right>', board.change_direction)
root.bind('<Up>', board.change_direction)
root.bind('<Down>', board.change_direction)

root.mainloop()