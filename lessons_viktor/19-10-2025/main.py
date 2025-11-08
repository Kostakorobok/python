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
        self.direction = ""

        self.load_assets()
        self.create_images()
        self.pack()
        self.start_game()

    def start_game(self):
        self.direction = "Right"
        self.move_snake()
        self.bind_all("<Key>", self.change_direction(self.direction))
        # set positions

    def move_snake(self):
        # self.snake_positions = [(100, 100), (80, 100), (60, 100)
        head_x, head_y = self.snake_positions[0]
        new_head = 0
        if self.direction == "Up":
            new_head = (head_x, head_y - 20)  # down, left, right
        if self.direction == "Down":
            new_head = (head_x, head_y + 20)
        if self.direction == "Right":
            new_head = (head_x + 20, head_y)
        if self.direction == "Left":
            new_head = (head_x - 20, head_y)

        # self.snake_positions = [(80, 100), (100, 100), (80, 100), (60, 100)]
        self.snake_positions = [new_head] + self.snake_positions[:-1]
        self.snake_positions.pop()

    def change_direction(self, event):
        self.move_snake()

    def update_graphics(self):
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

    def create_images(self):
        for x_snake, y_snake in self.snake_positions:
            self.create_image(x_snake, y_snake, image=self.photo_snake, tag="snake")
        x_food, y_food = self.food_positions  # !!!!!
        self.create_image(x_food, y_food, image=self.food_photo, tag="food")

    def set_food_positions(self):
        return (random.randint(0, 300), random.randint(0, 300))  # experiment

    def test(self):
        # asset_food = tk.Label(self.root, image=self.food_photo).pack()
        # asset_snake = tk.Label(self.root, image=self.photo_snake).pack()
        pass
        # asset_food = self.create_image(100, 100, image=self.food_photo, tag="food")
        # asset_snake = self.create_image(290, 290, image=self.photo_snake, tag="snake")

root = tk.Tk()
root.title("Show assets!")
root.resizable(False, False)
root.geometry("600x620")

# bind
board = Snake(root)
board.test()

root.mainloop()

root.bind('<Left>', board.change_direction('Left'))
root.bind('<Right>', board.change_direction('Right'))
root.bind('<Up>', board.change_direction('Up'))
root.bind('<Down>', board.change_direction('Down'))

# graphics :
# Choice 1 : clear screen -> draw everything again with aonther positions -> blinking problem
# Choice 2: delete only 1 elem -> remove/ pop doesn't work
# update_graphics function -> do that
# reaction on buttons problem.
