import tkinter as tk
from tkinter import ttk

import linear_graphs_functions as lgf

root = tk.Tk()
root.title("Random Graph Generator")
root.geometry("600x400")
x_axis = []
y_axis = []

buttonGenerate = tk.Button(root, width = 25, height = 2, text = "Generate x and y values", command =lambda: lgf.random_xy_values(x_axis, y_axis, 10)).pack(side="top", padx = 20, pady = 20)
buttonClear = tk.Button(root,width = 25, height = 2, text = "Clear x and y data", command = lambda: lgf.clear_data(x_axis, y_axis)).pack(side="left", padx = 20, pady = 20)
buttonShow = tk.Button(root,width = 25, height = 2, text = "Show Graph", command =lambda: lgf.generate_graph(x_axis, y_axis)).pack(side="right", padx = 20, pady = 20)
buttonQuit = tk.Button(root,width = 25, height = 2, text = "Quit", command = root.destroy).pack(side="bottom", padx = 20, pady = 20)

root.mainloop()