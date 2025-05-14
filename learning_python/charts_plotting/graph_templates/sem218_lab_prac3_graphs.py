import matplotlib.pyplot as plt

# Function for graph
def plot_graph (x, y_list, labels=None, title="Graph Title", x_axis_label="x-axis", y_axis_label="y-axis", grid=True, invert_y=True):

    # Screen format:
    plt.figure(figsize=(10, 6), facecolor="lightgrey")
    # Line style:

    for i, y in enumerate(y_list):
        label=labels[i] if labels and i < len(labels) else None
        plt.plot(x, y, marker='o', linestyle='-', linewidth=2, label=label)

    #labels:
    plt.title(title, fontsize=16)
    plt.xlabel(x_axis_label, fontsize=12)
    plt.ylabel(y_axis_label, fontsize=12)

    # background grid, transparent:
    if grid:
        plt.grid(True, linestyle="--", alpha=0.7)

    if labels:
        plt.legend()

    if invert_y:
        plt.gca().invert_yaxis()
    # Generating part name:

    plt.show()

# Values for 4mm Sharp Nozzle
x_axis_values_4S_180 = [25, 74, 125, 175, 225]
x_axis_values_4S_290 = [25, 74, 125, 175, 225, 275, 325]
x_axis_values_4S_400 = [25, 74, 125, 175, 225, 275, 325, 375]
y_axis_values_4S_180 = [0, 12.86, 38.06, 72.81, 117.48]
y_axis_values_4S_290 = [0, 8.01, 22.54, 44.21, 74.51, 114.41, 158.77]
y_axis_values_4S_400 = [0, 4.59, 15.16, 31.14, 52.51, 78.51, 110.45, 152.04]

# Values for 8mm Sharp Nozzle
x_axis_values_8S_180 = [25, 74, 125, 175, 225]
x_axis_values_8S_290 = [25, 74, 125, 175, 225, 275, 325]
x_axis_values_8S_400 = [25, 74, 125, 175, 225, 275, 325, 375]
y_axis_values_8S_180 = [0, 11.63, 34.9, 70.25, 114.29]
y_axis_values_8S_290 = [0, 7.51, 24.23, 43.78, 73.08, 104.44, 158.32]
y_axis_values_8S_400 = [0, 3.63, 13.75, 29.83, 50.85, 81.68, 107.8, 142.15]

# Values for 4mm Round Nozzle
x_axis_values_4R_180 = [25, 74, 125, 175, 225, 275]
x_axis_values_4R_290 = [25, 74, 125, 175, 225, 275, 325, 375]
x_axis_values_4R_400 = [25, 74, 125, 175, 225, 275, 325, 375]
y_axis_values_4R_180 = [0, 9.23, 29.4, 55.32, 92.06, 137.76]
y_axis_values_4R_290 = [0, 4.79, 15.91, 32.82, 54.09, 80.09, 116.63, 154.76]
y_axis_values_4R_400 = [0, 3.43, 10.67, 22.46, 38.04, 57.04, 78.44, 106.49]

# Values for 8mm Round Nozzle
x_axis_values_8R_180 = [25, 74, 125, 175, 225, 275]
x_axis_values_8R_290 = [25, 74, 125, 175, 225, 275, 325, 375]
x_axis_values_8R_400 = [25, 74, 125, 175, 225, 275, 325, 375]
y_axis_values_8R_180 = [0, 5.27, 22.22, 45.47, 78.14, 116.28]
y_axis_values_8R_290 = [0, 5.77, 14.87, 28.7, 45.84, 74.22, 106.36, 140.8]
y_axis_values_8R_400 = [0, 0.41, 7.7, 18.73, 32.62, 50.89, 69.85, 97.97]

list_y_axes_S180mm = [y_axis_values_4S_180, y_axis_values_8S_180]
list_y_axes_S290mm = [y_axis_values_4S_290, y_axis_values_8S_290]
list_y_axes_S400mm = [y_axis_values_4S_400, y_axis_values_8S_400]

list_y_axes_R180mm = [y_axis_values_4R_180, y_axis_values_8R_180]
list_y_axes_R290mm = [y_axis_values_4R_290, y_axis_values_8R_290]
list_y_axes_R400mm = [y_axis_values_4R_400, y_axis_values_8R_400]

x_axis_name = "Callipers X position"
y_axis_name = "Stream Y position"

plot_graph(x_axis_values_4S_180, list_y_axes_S180mm, labels=["4mm-Sharp", "8mm-Sharp"], title="Jet Trajectory, Sharp Nozzle | 180mm Water Level",
           x_axis_label="Callipers, x-axis position", y_axis_label="Stream, y-axis position")
plot_graph(x_axis_values_4S_290, list_y_axes_S290mm, labels=["4mm-Sharp", "8mm-Sharp"], title="Jet Trajectory, Sharp Nozzle | 290mm Water Level",
           x_axis_label="Callipers, x-axis position", y_axis_label="Stream, y-axis position")
plot_graph(x_axis_values_4S_400, list_y_axes_S400mm, labels=["4mm-Sharp", "8mm-Sharp"], title="Jet Trajectory, Sharp Nozzle | 400mm Water Level",
           x_axis_label="Callipers, x-axis position", y_axis_label="Stream, y-axis position")

plot_graph(x_axis_values_4R_180, list_y_axes_R180mm, labels=["4mm-Round", "8mm-Round"], title="Jet Trajectory, Round Nozzle | 180mm Water Level",
           x_axis_label="Callipers, x-axis position", y_axis_label="Stream, y-axis position")
plot_graph(x_axis_values_4R_290, list_y_axes_R290mm, labels=["4mm-Round", "8mm-Round"], title="Jet Trajectory, Round Nozzle | 290mm Water Level",
           x_axis_label="Callipers, x-axis position", y_axis_label="Stream, y-axis position")
plot_graph(x_axis_values_4R_400, list_y_axes_R400mm, labels=["4mm-Round", "8mm-Round"], title="Jet Trajectory, Round Nozzle | 400mm Water Level",
           x_axis_label="Callipers, x-axis position", y_axis_label="Stream, y-axis position")


