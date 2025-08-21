import matplotlib.pyplot as plt

# Function for graph
def plot_graph (x, y_list, labels=None, title="Graph Title", x_axis_label="x-axis", y_axis_label="y-axis", grid=True, invert_y=True):

    # Screen format:
    plt.figure(figsize=(10, 6), facecolor="lightgrey")
    # Line style:

    for i, y in enumerate(y_list):
        label=labels[i] if labels and i < len(labels) else None
        plt.plot(x, y, marker='o', linestyle='-', linewidth=2, label=label)
        # for x_value, y_value in zip(x, y):
        #     plt.text(x_value, y_value,f"{y_value:.1f}", fontsize=9, ha='left', va='bottom')

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
x_axis_values = [25, 74, 125, 175, 225, 275, 325, 375, 425.00, 475.00, 525.00, 575.00, 625.00]
y_axis_values_180 = [0.87, 7.61, 21.70, 42.53, 70.31, 105.03, 146.70, 195.31,250.87, 313.37, 382.81, 459.20, 542.53]
y_axis_values_290 = [0.54, 4.72, 13.47, 26.40, 43.64, 65.19, 91.06, 121.23, 155.71, 194.50, 237.61, 285.02, 336.75]
y_axis_values_400 = [0.39, 3.42, 9.77, 19.14, 31.64, 47.27, 66.02, 87.89, 112.89, 141.02, 172.27, 206.64, 244.14]

y_axis_values = [y_axis_values_180, y_axis_values_290, y_axis_values_400]


x_axis_name = "X position"
y_axis_name = "Theoretical Y position"

plot_graph(x_axis_values, y_axis_values, labels=["180mm Water level", "290mm Water level", "400mm Water level"], title="Theoretical Jet Trajectory",
           x_axis_label="Callipers, x-axis position", y_axis_label="Stream, theoretical y-axis position")



