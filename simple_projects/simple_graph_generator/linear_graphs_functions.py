import random
import matplotlib.pyplot as plt

def random_xy_values(x, y, m, c, no):
    m = 1
    c = 1
    for i in range(no):
        x_temp = random.randint(0, 100)
        y_temp = x_temp * m + c
        x.append(x_temp)
        y.append(y_temp)



def generate_graph(x, y):
    plt.plot(x, y, color="green", linestyle="solid", marker="o", linewidth=1)

    plt.suptitle("Random Linear Graph")
    plt.xlabel("x-axis values")
    plt.ylabel("y-axis values")

    plt.show()