import matplotlib.pyplot as plt

# Function for graph
def plot_graph (x_list, y_list, labels=None, title="Graph Title", x_axis_label="x-axis", y_axis_label="y-axis", grid=True, invert_y=True, invert_x=False, show_reynolds_threshold=False):

    # Screen format:
    plt.figure(figsize=(10, 6), facecolor="lightgrey")
    # Line style:

    for i, y in enumerate(y_list):
        x = x_list[i] if isinstance(x_list[0], list) else x_list
        label=labels[i] if labels and i < len(labels) else None
        plt.plot(x, y, marker='o', linestyle='-', linewidth=2, label=label)

    if show_reynolds_threshold:
        plt.axhline(y=2300, color='gray', linestyle='--', linewidth=1.5, label='Re = 2300')

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

    if invert_x:
        plt.gca().invert_xaxis()

    plt.show()

"""Prac 2"""

# Values for 4mm Sharp Nozzle
# x_axis_values_4S_180 = [25, 74, 125, 175, 225]
# x_axis_values_4S_290 = [25, 74, 125, 175, 225, 275, 325]
# x_axis_values_4S_400 = [25, 74, 125, 175, 225, 275, 325, 375]
# y_axis_values_4S_180 = [0, 12.86, 38.06, 72.81, 117.48]
# y_axis_values_4S_290 = [0, 8.01, 22.54, 44.21, 74.51, 114.41, 158.77]
# y_axis_values_4S_400 = [0, 4.59, 15.16, 31.14, 52.51, 78.51, 110.45, 152.04]
#
# # Values for 8mm Sharp Nozzle
# x_axis_values_8S_180 = [25, 74, 125, 175, 225]
# x_axis_values_8S_290 = [25, 74, 125, 175, 225, 275, 325]
# x_axis_values_8S_400 = [25, 74, 125, 175, 225, 275, 325, 375]
# y_axis_values_8S_180 = [0, 11.63, 34.9, 70.25, 114.29]
# y_axis_values_8S_290 = [0, 7.51, 24.23, 43.78, 73.08, 104.44, 158.32]
# y_axis_values_8S_400 = [0, 3.63, 13.75, 29.83, 50.85, 81.68, 107.8, 142.15]
#
# # Values for 4mm Round Nozzle
# x_axis_values_4R_180 = [25, 74, 125, 175, 225, 275]
# x_axis_values_4R_290 = [25, 74, 125, 175, 225, 275, 325, 375]
# x_axis_values_4R_400 = [25, 74, 125, 175, 225, 275, 325, 375]
# y_axis_values_4R_180 = [0, 9.23, 29.4, 55.32, 92.06, 137.76]
# y_axis_values_4R_290 = [0, 4.79, 15.91, 32.82, 54.09, 80.09, 116.63, 154.76]
# y_axis_values_4R_400 = [0, 3.43, 10.67, 22.46, 38.04, 57.04, 78.44, 106.49]
#
# # Values for 8mm Round Nozzle
# x_axis_values_8R_180 = [25, 74, 125, 175, 225, 275]
# x_axis_values_8R_290 = [25, 74, 125, 175, 225, 275, 325, 375]
# x_axis_values_8R_400 = [25, 74, 125, 175, 225, 275, 325, 375]
# y_axis_values_8R_180 = [0, 5.27, 22.22, 45.47, 78.14, 116.28]
# y_axis_values_8R_290 = [0, 5.77, 14.87, 28.7, 45.84, 74.22, 106.36, 140.8]
# y_axis_values_8R_400 = [0, 0.41, 7.7, 18.73, 32.62, 50.89, 69.85, 97.97]
#
# list_y_axes_S180mm = [y_axis_values_4S_180, y_axis_values_8S_180]
# list_y_axes_S290mm = [y_axis_values_4S_290, y_axis_values_8S_290]
# list_y_axes_S400mm = [y_axis_values_4S_400, y_axis_values_8S_400]
#
# list_y_axes_R180mm = [y_axis_values_4R_180, y_axis_values_8R_180]
# list_y_axes_R290mm = [y_axis_values_4R_290, y_axis_values_8R_290]
# list_y_axes_R400mm = [y_axis_values_4R_400, y_axis_values_8R_400]
#
# x_axis_name = "Callipers X position"
# y_axis_name = "Stream Y position"

# plot_graph(x_axis_values_4S_180, list_y_axes_S180mm, labels=["4mm-Sharp", "8mm-Sharp"], title="Jet Trajectory, Sharp Nozzle | 180mm Water Level",
#            x_axis_label="Callipers, x-axis position", y_axis_label="Stream, y-axis position")
# plot_graph(x_axis_values_4S_290, list_y_axes_S290mm, labels=["4mm-Sharp", "8mm-Sharp"], title="Jet Trajectory, Sharp Nozzle | 290mm Water Level",
#            x_axis_label="Callipers, x-axis position", y_axis_label="Stream, y-axis position")
# plot_graph(x_axis_values_4S_400, list_y_axes_S400mm, labels=["4mm-Sharp", "8mm-Sharp"], title="Jet Trajectory, Sharp Nozzle | 400mm Water Level",
#            x_axis_label="Callipers, x-axis position", y_axis_label="Stream, y-axis position")
#
# plot_graph(x_axis_values_4R_180, list_y_axes_R180mm, labels=["4mm-Round", "8mm-Round"], title="Jet Trajectory, Round Nozzle | 180mm Water Level",
#            x_axis_label="Callipers, x-axis position", y_axis_label="Stream, y-axis position")
# plot_graph(x_axis_values_4R_290, list_y_axes_R290mm, labels=["4mm-Round", "8mm-Round"], title="Jet Trajectory, Round Nozzle | 290mm Water Level",
#            x_axis_label="Callipers, x-axis position", y_axis_label="Stream, y-axis position")
# plot_graph(x_axis_values_4R_400, list_y_axes_R400mm, labels=["4mm-Round", "8mm-Round"], title="Jet Trajectory, Round Nozzle | 400mm Water Level",
#            x_axis_label="Callipers, x-axis position", y_axis_label="Stream, y-axis position")

# Round nozzles
# 4mm round nozzles:
# x_common = [25, 74, 125, 175, 225, 275, 325, 375]
# list_y_4mmR_nozzle = [y_axis_values_4R_180+[None, None], y_axis_values_4R_290, y_axis_values_4R_400]
# plot_graph(x_common, list_y_4mmR_nozzle)

dia1mm_measured_deltaP = [11260, 8580, 6290, 4640, 3290, 2470, 1620, 930]
dia1mm_theoretical_deltaP = [433596.30, 339764.16, 256843.40, 184923.97, 124135.42, 74675.00, 36869.65, 11348.80]
dia2mm_measured_deltaP = [17450, 17420, 13310, 9530, 6350, 4090, 2000, 530]
dia2mm_theoretical_deltaP = [1001163.81, 776908.52, 580229.11, 411779.91, 271556.09, 159573.77, 76025.52, 22040.06]
dia3mm_measured_deltaP = [9450, 7410, 5510, 4030, 2620, 1490, 600, 110]
dia3mm_theoretical_deltaP = [991726.20, 751640.88, 544748.99, 370705.50, 229734.00, 121824.70, 47189.88, 6515.80]
dia4mm_measured_deltaP = [8140, 7140, 5400, 4090, 2820, 1720, 860, 240]
dia4mm_theoretical_deltaP = [423698.17, 328564.25, 245298.82, 173882.29, 114473.18, 67062.11, 31852.02, 9122.57]

dia1mm_average_velocity = [16.985, 14.862, 12.739, 10.616, 8.493, 6.369, 4.246, 2.123]
dia2mm_average_velocity = [42.463, 37.155, 31.847, 26.539, 21.231, 15.924, 10.616, 5.308]
dia3mm_average_velocity = [53.079, 46.001, 38.924, 31.847, 24.770, 17.693, 10.616, 3.539]
dia4mm_average_velocity = [42.463, 37.155, 31.847, 26.539, 21.231, 15.924, 10.616, 5.308]

x_axis_combined = [dia1mm_average_velocity, dia1mm_average_velocity, dia2mm_average_velocity, dia2mm_average_velocity, dia3mm_average_velocity, dia3mm_average_velocity, dia4mm_average_velocity, dia4mm_average_velocity]
y_axis_combined = [dia1mm_measured_deltaP, dia1mm_theoretical_deltaP, dia2mm_measured_deltaP, dia2mm_theoretical_deltaP, dia3mm_measured_deltaP, dia3mm_theoretical_deltaP,
          dia4mm_measured_deltaP, dia4mm_theoretical_deltaP]

x_axis_1mm = [dia1mm_average_velocity, dia1mm_average_velocity]
x_axis_2mm = [dia2mm_average_velocity, dia2mm_average_velocity]
x_axis_3mm = [dia3mm_average_velocity, dia3mm_average_velocity]
x_axis_4mm = [dia4mm_average_velocity, dia4mm_average_velocity]

y_axis_1mm = [dia1mm_measured_deltaP, dia1mm_theoretical_deltaP]
y_axis_2mm = [dia2mm_measured_deltaP, dia2mm_theoretical_deltaP]
y_axis_3mm = [dia3mm_measured_deltaP, dia3mm_theoretical_deltaP]
y_axis_4mm = [dia4mm_measured_deltaP, dia4mm_theoretical_deltaP]

y_axis_Re_1mm = [17765.440, 15544.760, 13324.080, 11103.400, 8882.720, 6662.040, 4441.360, 2220.680]
y_axis_Re_2mm = [88827.199, 77723.800, 66943.006, 55920.315, 44736.252, 33552.189, 22583.430, 11237.875]
y_axis_Re_3mm = [168568.130, 146792.295, 124208.865, 101867.799, 79230.510, 56593.222, 33955.933, 11345.580]
y_axis_Re_4mm = [181529.276, 158838.116, 136146.957, 113725.210, 90980.168, 68396.806, 45597.871, 22798.935]

Re_x_axis = [dia1mm_average_velocity, dia2mm_average_velocity, dia3mm_average_velocity, dia4mm_average_velocity]
Re_y_axis_1mm = [y_axis_Re_1mm, y_axis_Re_2mm, y_axis_Re_3mm, y_axis_Re_4mm]

# plot_graph(x_axis_combined, y_axis_combined, labels=["1mm Dia | Measured Pressure Drop, Pa", "1mm Dia | Theoretical Pressure Drop, Pa",
#                                                     "2mm Dia | Measured Pressure Drop, Pa", "2mm Dia | Theoretical Pressure Drop, Pa",
#                                                     "3mm Dia | Measured Pressure Drop, Pa", "3mm Dia | Theoretical Pressure Drop, Pa",
#                                                     "4mm Dia | Measured Pressure Drop, Pa", "4mm Dia | Theoretical Pressure Drop, Pa"], title="Measured vs Theoretical Pressure Drop",
#            x_axis_label="Average Velocity m/s", y_axis_label="Pressure Drop, Pa")

# plot_graph(x_axis_1mm, y_axis_1mm, labels=["1mm Dia | Measured Pressure Drop, Pa", "1mm Dia | Theoretical Pressure Drop, Pa"], title="Pipe 1mm Dia | Measured vs Theoretical Pressure Drop", x_axis_label="Average Velocity m/s", y_axis_label="Pressure Drop, Pa", invert_y=False, invert_x=True)
# plot_graph(x_axis_2mm, y_axis_2mm, labels=["2mm Dia | Measured Pressure Drop, Pa", "2mm Dia | Theoretical Pressure Drop, Pa"], title="Pipe 2mm Dia | Measured vs Theoretical Pressure Drop", x_axis_label="Average Velocity m/s", y_axis_label="Pressure Drop, Pa", invert_y=False, invert_x=True)
# plot_graph(x_axis_3mm, y_axis_3mm, labels=["3mm Dia | Measured Pressure Drop, Pa", "3mm Dia | Theoretical Pressure Drop, Pa"], title="Pipe 3mm Dia | Measured vs Theoretical Pressure Drop", x_axis_label="Average Velocity m/s", y_axis_label="Pressure Drop, Pa", invert_y=False, invert_x=True)
# plot_graph(x_axis_4mm, y_axis_4mm, labels=["4mm Dia | Measured Pressure Drop, Pa", "4mm Dia | Theoretical Pressure Drop, Pa"], title="Pipe 4mm Dia | Measured vs Theoretical Pressure Drop", x_axis_label="Average Velocity m/s", y_axis_label="Pressure Drop, Pa", invert_y=False, invert_x=True)

# plot_graph(x_axis_1mm, y_axis_Re_1mm, title="Pipe 1mm Dia | Reynold's Number vs Average Velocity", x_axis_label="Average Velocity m/s", y_axis_label="Reynold's Number", invert_y=False, invert_x=True)
# plot_graph(x_axis_2mm, y_axis_Re_2mm, title="Pipe 2mm Dia | Reynold's Number vs Average Velocity", x_axis_label="Average Velocity m/s", y_axis_label="Reynold's Number", invert_y=False, invert_x=True)
# plot_graph(x_axis_3mm, y_axis_Re_3mm, title="Pipe 3mm Dia | Reynold's Number vs Average Velocity", x_axis_label="Average Velocity m/s", y_axis_label="Reynold's Number", invert_y=False, invert_x=True)
# plot_graph(x_axis_4mm, y_axis_Re_4mm, title="Pipe 4mm Dia | Reynold's Number vs Average Velocity", x_axis_label="Average Velocity m/s", y_axis_label="Reynold's Number", invert_y=False, invert_x=True)

plot_graph(Re_x_axis, Re_y_axis_1mm, title="Velocity VS Reynold's number", labels=["1mm Diameter Pipe", "2mm Diameter Pipe", "3mm Diameter Pipe", "4mm Diameter Pipe"], x_axis_label="Average Velocity m/s", y_axis_label="Reynold's Number", invert_y=False, invert_x=False, show_reynolds_threshold=True)
