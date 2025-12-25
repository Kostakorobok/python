import tkinter as tk
from PIL import Image, ImageTk
import random

WALL_MARGIN_PX = 10
STEP = 20


class Snake(tk.Canvas):

    def __init__(self, root, width=600, length=620, colour="black", line_thickness=0):
        super().__init__(
            root,
            width=width,
            height=length,
            bg=colour,
            highlightthickness=line_thickness
        )

        # -------- REQUIRED FIRST --------
        self.root = root
        self.width = width
        self.length = length
        self.colour = colour
        self.line_thickness = line_thickness

        # -------- GAME STATE --------
        self.snake_positions = [(100, 100), (80, 100), (60, 100)]
        self.direction = "Right"
        self.is_game_on = True

        self.food_positions = self.set_food_positions()

        # -------- ASSETS --------
        self.food_photo = None
        self.photo_snake = None

        self.load_assets()
        self.pack()
        self.start_game()

    def start_game(self):
        self.bind_all("<Key>", self.change_direction)
        self.game_loop()

    def game_loop(self):
        self.move_snake()
        self.check_boundaries()
        self.check_food_collisions()
        self.check_snake_collisions()

        if not self.is_game_on:
            return

        self.update_graphics()
        self.root.after(200, self.game_loop)

    def move_snake(self):
        head_x, head_y = self.snake_positions[0]

        if self.direction == "Up":
            new_head = (head_x, head_y - STEP)
        elif self.direction == "Down":
            new_head = (head_x, head_y + STEP)
        elif self.direction == "Left":
            new_head = (head_x - STEP, head_y)
        else:  # Right
            new_head = (head_x + STEP, head_y)

        self.snake_positions.insert(0, new_head)

        if (new_head == self.snake_positions[-1]):
            self.end_game()
            return

        if new_head != self.food_positions:
            self.snake_positions.pop()

    def update_graphics(self):
        self.delete("all")

        for x, y in self.snake_positions:
            self.create_image(x, y, image=self.photo_snake)

        fx, fy = self.food_positions
        self.create_image(fx, fy, image=self.food_photo)

    def change_direction(self, event):
        key = event.keysym

        if key == "Up" and self.direction != "Down":
            self.direction = "Up"
        elif key == "Down" and self.direction != "Up":
            self.direction = "Down"
        elif key == "Left" and self.direction != "Right":
            self.direction = "Left"
        elif key == "Right" and self.direction != "Left":
            self.direction = "Right"

    def check_food_collisions(self):  # for head
        if self.snake_positions[0] == self.food_positions:
            self.food_positions = self.set_food_positions()

    def check_snake_collisions(self):
        if (self.snake_positions[0] in self.snake_positions[1:]):
            self.end_game()

    def check_boundaries(self):
        x, y = self.snake_positions[0]

        if (
                x < WALL_MARGIN_PX or
                y < WALL_MARGIN_PX or
                x > self.width - WALL_MARGIN_PX or
                y > self.length - WALL_MARGIN_PX
        ):
            self.end_game()

    def end_game(self):
        self.is_game_on = False
        self.delete("all")
        self.create_text(
            self.width / 2,
            self.length / 2,
            text="GAME OVER",
            fill="#00cc00",
            font=("Arial", 28, "bold")
        )

    def set_food_positions(self):
        while True:
            x = random.randrange(0, self.width, STEP)
            y = random.randrange(0, self.length, STEP)
            if (x, y) not in self.snake_positions:
                return (x, y)

    def load_assets(self):
        try:
            self.food_image = Image.open("assets/food.png").resize((STEP, STEP))
            self.snake_image = Image.open("assets/snake.png").resize((STEP, STEP))

            self.food_photo = ImageTk.PhotoImage(self.food_image)
            self.photo_snake = ImageTk.PhotoImage(self.snake_image)

        except IOError as error:
            print(error)
            self.root.destroy()


# -------- MAIN --------

root = tk.Tk()
root.title("Snake Game")
root.resizable(False, False)

board = Snake(root)

root.mainloop()
