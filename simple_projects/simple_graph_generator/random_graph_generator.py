import matplotlib.pyplot as mt
import random as rnd

from tkinter import *
from tkinter import ttk

import linear_graphs_functionsÍ

m = 1
c = 1
a = 1
b = 1
number_of_points = 20
x_axis = []
y_axis = []

for i in range(number_of_points):
    x = rnd.randint(0, 100)
    y_linear = x * m + c
    x_axis.append(x)
    y_axis.append(y_linear)

print(x_axis, "\n", y_axis)