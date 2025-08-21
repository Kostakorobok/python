import matplotlib.pyplot as plt
import numpy as np

# Data for the Freundlich isotherm
log_P = np.linspace(0, 1.2, 100)
log_k = 0.2
slope = 0.6
log_x_m = slope * log_P + log_k

# Colors and styles
line_color = '#FF6F61'       # Coral pink
triangle_color = '#4B0082'   # Indigo
text_color = '#008080'       # Teal
bg_color = '#fdf6e3'         # Soft background

# Setup plot
fig, ax = plt.subplots(figsize=(10, 6))
fig.patch.set_facecolor(bg_color)
ax.set_facecolor(bg_color)

# Freundlich curve
ax.plot(log_P, log_x_m, color=line_color, linewidth=3)

# Triangle (touches the curve)
x_triangle = 0.7
y_triangle = slope * x_triangle + log_k
dx = 0.25
dy = dx * slope
ax.plot([x_triangle - dx, x_triangle], [y_triangle - dy, y_triangle], color=triangle_color)
ax.plot([x_triangle, x_triangle], [y_triangle - dy, y_triangle], color=triangle_color)
ax.plot([x_triangle - dx, x_triangle], [y_triangle - dy, y_triangle - dy], color=triangle_color)

# Slope label
ax.text(x_triangle + 0.02, y_triangle - dy / 2, 'slope = 1/n',
        fontsize=16, color=text_color, va='center')

# Intercept marker and label
ax.plot([0, 0], [0, log_k], color='black')
ax.plot([-0.02, 0.02], [0, 0], color='black')
ax.plot([-0.02, 0.02], [log_k, log_k], color='black')
ax.text(0.05, log_k - 0.05, 'Intercept = log k',
        fontsize=14, color=text_color, ha='left', va='top')

# Axis arrowheads
arrowprops = dict(facecolor='black', arrowstyle='->', linewidth=1.5)
ax.annotate('', xy=(2.5, 0), xytext=(0, 0), arrowprops=arrowprops)  # x-axis
ax.annotate('', xy=(0, 1.2), xytext=(0, 0), arrowprops=arrowprops)  # y-axis

# Remove default spines
for spine in ['bottom', 'left', 'top', 'right']:
    ax.spines[spine].set_visible(False)

# Labels
ax.set_xlabel("Log P", fontsize=16, color='black', labelpad=15)
ax.set_ylabel(r"Log $\frac{x}{m}$", fontsize=16, color='black', labelpad=15)

# LaTeX equation
latex_eq = r"$\log\left(\frac{x}{m}\right) = \log(K) + \frac{1}{n} \log(C)$"
ax.text(1.25, 1.1, latex_eq, fontsize=18, color='black')

# Explanation block (your real-world terms)
description = (
    r"$x$ = copper mass absorbed by soil" + "\n"
    r"$m$ = mass of soil sample" + "\n"
    r"$C$ = equilibrium copper concentration in water" + "\n"
    r"$K$ = partition coefficient (y-intercept)" + "\n"
    r"$\frac{1}{n}$ = slope"
)
ax.text(1.25, 0.5, description, fontsize=14, color='black', va='top')

# Clean up plot
ax.set_xticks([])
ax.set_yticks([])
ax.set_xlim(0, 2.5)
ax.set_ylim(0, 1.2)

# Final layout and show
plt.tight_layout()
plt.show()
