import matplotlib.pyplot as plt
import random as rnd

from tkinter import *
from tkinter import ttk

import linear_graphs_functions as lgf

root = Tk()
root.title("Random Graph Generator")
mainframe = ttk.Frame(root, padding = 10)
mainframe.grid()


m = 1
c = 1
a = 1
b = 1
number_of_points = 20
x_axis = []
y_axis = []

# print(x_axis, "\n", y_axis)
def generate_graph():
    plt.plot(x_axis, y_axis, color="green", linestyle="solid", marker="o", linewidth=1)

    plt.suptitle("Random Linear Graph")
    plt.xlabel("x-axis values")
    plt.ylabel("y-axis values")

    plt.show()

ttk.Button(mainframe, text = "Generate x and y values", command = lgf.random_xy_values(x_axis, y_axis, m, c, number_of_points)).grid(row = 0, column = 0)
ttk.Button(mainframe, text = "Show Graph", command = generate_graph).grid(row = 1, column = 0)
ttk.Button(mainframe, text = "Quit", command = root.destroy).grid(row = 2, column = 0)

root.mainloop()