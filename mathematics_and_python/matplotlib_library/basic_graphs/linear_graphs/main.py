import matplotlib.pyplot as plt

# Let's create 3 random linear graphs

x = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
y1 = []
y2 = []
y3 = []

# Functions for y-axis to create 3 separate graphs
for i in x:
    y1.append(i)
    y2.append(i*6 + i*3 + 7)
    y3.append(i*4)

# plt.plot plots graph on the same space

plt.plot(x, y1, color = "green")
plt.plot(x, y2, color = "red")
plt.plot(x, y3, color = "blue")

# Checking generated values
print(x,"\n", y1, "\n", y2, "\n", y3)

# Annotating
plt.suptitle("Linear Graphs")
plt.xlabel("x-axis")
plt.ylabel("y-axis")

# Displays Graph on the screen
plt.show()
