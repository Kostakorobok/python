import numpy as np
import matplotlib.pyplot as plt

# Let's create 3 random linear graphs

X = np.linspace(0, 10, 10)
y0 = []
y1 = []
y2 = []

# Functions for y-axis to create 3 separate graphs
for i in X:
    y0.append(i)
    y1.append(i*6 + i*3 + 7)
    y2.append(i*4)

# Parameters
common_line_thickness = 0.5

# plt.plot plots graph on the same space

line0 = plt.plot(X, y0, color = "green", linestyle = "solid", marker = "o", linewidth = common_line_thickness)
line1 = plt.plot(X, y1, color = "red", linestyle = "dashdot", marker = "s", linewidth = common_line_thickness)
line2 = plt.plot(X, y2, color = "blue", linestyle = "dotted", marker = "x", linewidth = common_line_thickness)

# Checking generated values
# print(X,"\n", y0, "\n", y1, "\n", y2)

# Annotating
plt.suptitle("Linear Graphs")
plt.xlabel("x-axis")
plt.ylabel("y-axis")

# Displays Graph on the screen
plt.show()