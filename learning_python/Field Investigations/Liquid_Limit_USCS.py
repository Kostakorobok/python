import matplotlib.pyplot as plt
import numpy as np

# Define Liquid Limit (LL) range
LL = np.linspace(0, 100, 500)

# A-line and U-line formulas
A_line = 0.73 * (LL - 20)
U_line = 0.9 * (LL - 8)

# Compute LL values for PI = 4 and 7 on A-line and U-line
LL_Aline_4 = (4 / 0.73) + 20
LL_Aline_7 = (7 / 0.73) + 20
LL_Uline_4 = (4 / 0.9) + 8
LL_Uline_7 = (7 / 0.9) + 8

# Silty clay polygon coordinates
silty_clay_LL = [LL_Uline_4, LL_Uline_7, LL_Aline_7, LL_Aline_4]
silty_clay_PI = [4, 7, 7, 4]

# Create plot
plt.figure(figsize=(10, 6))
plt.plot(LL, A_line, label="A-line: PI = 0.73(LL - 20)", color='black')
plt.plot(LL, U_line, label="U-line: PI = 0.9(LL - 8)", color='black')

# Fill zones
plt.fill_between(LL, A_line, U_line, where=(U_line > A_line), color='lightcoral', label='Clay')
plt.fill_between(LL, 0, A_line, color='lightgreen', label='Silt')
plt.fill(silty_clay_LL, silty_clay_PI, color='gray', label='Silty clay')

# Horizontal PI reference lines
plt.axhline(y=4, color='black', linestyle='--', linewidth=0.8)
plt.axhline(y=7, color='black', linestyle='--', linewidth=0.8)

# Label for Silty clay
plt.annotate('Silty clay', xy=(18, 6.2), xytext=(4, 10),
             arrowprops=dict(facecolor='black', arrowstyle='-'),
             fontsize=12)

# Inline labels for A-line and U-line
plt.text(60, 0.73 * (60 - 20) - 3, 'A-line', fontsize=12, rotation=31, color='black')
plt.text(55, 0.9 * (55 - 8) + 2, 'U-line', fontsize=12, rotation=40, color='black')

# Axis settings
plt.xlabel("Liquid Limit")
plt.ylabel("Plasticity Index")
plt.xlim(0, 100)
plt.ylim(0, 65)
plt.xticks(np.arange(0, 101, 10))
plt.yticks(np.arange(0, 70, 10))

# Grid, legend, and title
plt.legend()
plt.grid(True, which='both', linestyle='--', linewidth=0.5)
plt.title("Plasticity Chart for the Field Investigations")

# Save to file
plt.tight_layout()
plt.savefig("plasticity_chart.png", dpi=300)
plt.show()
