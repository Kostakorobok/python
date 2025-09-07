import random
import matplotlib.pyplot as plt

def random_xy_values(x, y, no):
    for i in range(no):
        x_temp = random.randint(0, 100)
        y_temp = x_temp + 1
        x.append(x_temp)
        y.append(y_temp)

def generate_graph(x, y):
    plt.clf()

    plt.plot(x, y, color="green", linestyle="solid", marker="o", linewidth=1)
    plt.suptitle("Random Linear Graph")
    plt.xlabel("x-axis values")
    plt.ylabel("y-axis values")

    plt.show()

def clear_data(x, y):
    x.clear()
    y.clear()