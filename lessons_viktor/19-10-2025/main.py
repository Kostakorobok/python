import tkinter as tk
from PIL import Image, ImageTk
import random


#
# class Snake -> __init__ -> load_assets(self)
# turtle
class Snake(tk.Canvas):

  def __init__(self,
               root,
               width=600,
               length=620,
               colour="black",
               line_thickness=0):
    super().__init__(root,
                     width=width,
                     height=length,
                     bg=colour,
                     highlightthickness=line_thickness)
    self.snake_positions = [(100, 100), (80, 100), (60, 100)]
    self.food_positions = self.set_food_positions()
    self.root = root
    self.width = width
    self.length = length
    self.colour = colour
    self.line_thickness = line_thickness
    self.food_photo = None
    self.photo_snake = None

    self.load_assets()
    self.create_images()
    self.pack()

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
    #self.snake_positions = [(100, 100), (80, 100), (60, 100)]
    for x_snake, y_snake in self.snake_positions:
      self.create_image(x_snake, y_snake, image=self.photo_snake, tag="snake")
    x_food, y_food = self.food_positions  # !!!!!
    self.create_image(x_food, y_food, image=self.food_photo, tag="food")

  def set_food_positions(self):
    return (random.randint(120, 300), random.randint(120, 300))  # experiment

  def test(self):
    # asset_food = tk.Label(self.root, image=self.food_photo).pack()
    # asset_snake = tk.Label(self.root, image=self.photo_snake).pack()
    pass
    #asset_food = self.create_image(100, 100, image=self.food_photo, tag="food")
    #asset_snake = self.create_image(290, 290, image=self.photo_snake, tag="snake")
  #def move_snake():

root = tk.Tk()
root.title("Show assets!")
root.resizable(False, False)
root.geometry("600x620")

board = Snake(root)
board.test()

root.mainloop()
# 010101010
# Homework:
# - How to make sneak move: tkinter
# -
# bind_all
# https://www.geeksforgeeks.org/python/how-to-bind-the-enter-key-to-a-tkinter-window/
# try to  move a snake
# https://www.youtube.com/watch?v=bfRwxS5d0SI