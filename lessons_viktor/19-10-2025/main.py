import tkinter as tk
from PIL import Image, ImageTk

# class Snake -> __init__ -> load_assets(self)

class Snake:
  def __init__(self, root, width = 600, length = 620, colour = "black", line_thickness = 0):
    self.root = root
    self.width = width
    self.length = length
    self.colour = colour
    self.line_thickness = line_thickness
    self.food_photo = None
    self.photo_snake = None

  def load_assets(self):
    try:
      self.food_image = Image.open("assets/food.png")
      self.snake_image = Image.open("assets/snake.png")
      self.food_photo = ImageTk.PhotoImage(self.food_image)
      self.photo_snake = ImageTk.PhotoImage(self.snake_image)
    except IOError as error:
      print(f"{error}")
      root.destroy()

  def test(self):
    asset_food = tk.Label(self.root, image=self.food_photo).pack()
    asset_snake = tk.Label(self.root, image=self.photo_snake).pack()


root = tk.Tk()
root.title("Show assets!")
root.resizable(False, False)
root.geometry("600x620")

board = Snake(root)
board.load_assets()
board.test()

root.mainloop()