import random

def random_xy_values(x_axis_value, y_axis_value, constant_m, constant_c, number_of_points):
    for i in range(number_of_points):
        x = random.randint(0, 100)
        y_linear = x * constant_m + constant_c
        x_axis_value.append(x)
        y_axis_value.append(y_linear)