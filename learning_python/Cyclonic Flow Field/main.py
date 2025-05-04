import sympy as sp
import numpy as np
import matplotlib.pyplot as plt

# Symbols
x, y = sp.symbols('x y')

# Constants
XX = 22   # From student ID
YY = 93   # From student ID
b = 2.31
K = 4.55

# Velocity components
u = XX + b * y - K * x
v = YY - b * x - K * y

# 1. Velocity vector at (1,1)
ux_val = u_val = u.subs({x: 1, y: 1})
vy_val = v_val = v.subs({x: 1, y: 1})

velocity_vector = sp.Matrix([u_val, v_val])
velocity_magnitude = sp.sqrt(u_val**2 + v_val**2)
velocity_direction = sp.atan2(v_val, u_val)

# 2. Acceleration vector using material derivative (2D only)
du_dx = sp.diff(u, x)
du_dy = sp.diff(u, y)
dv_dx = sp.diff(v, x)
dv_dy = sp.diff(v, y)

ax = u * du_dx + v * du_dy
ay = u * dv_dx + v * dv_dy

ax_val = ax.subs({x: 1, y: 1})
ay_val = ay.subs({x: 1, y: 1})

acceleration_vector = sp.Matrix([ax_val, ay_val])
acceleration_magnitude = sp.sqrt(ax_val**2 + ay_val**2)
acceleration_direction = sp.atan2(ay_val, ax_val)

# 3. Stagnation point: solve u=0, v=0
stagnation_point = sp.solve([u, v], (x, y))

# 4. Incompressibility check: divergence
div = sp.diff(u, x) + sp.diff(v, y)

# 5. Optional: Plot vector field around origin
X_vals, Y_vals = np.meshgrid(np.linspace(-5, 5, 20), np.linspace(-5, 5, 20))
U_func = sp.lambdify((x, y), u, 'numpy')
V_func = sp.lambdify((x, y), v, 'numpy')
U_vals = U_func(X_vals, Y_vals)
V_vals = V_func(X_vals, Y_vals)

plt.figure(figsize=(6, 6))
plt.quiver(X_vals, Y_vals, U_vals, V_vals, color='blue')
plt.title('Cyclonic Velocity Field')
plt.xlabel('x')
plt.ylabel('y')
plt.grid(True)
plt.axis('equal')
plt.show()

# Display results
print("Velocity vector at (1,1):", velocity_vector)
print("Velocity magnitude:", velocity_magnitude.evalf())
print("Velocity direction (rad):", velocity_direction.evalf())
print("\nAcceleration vector at (1,1):", acceleration_vector)
print("Acceleration magnitude:", acceleration_magnitude.evalf())
print("Acceleration direction (rad):", acceleration_direction.evalf())
print("\nStagnation point:", stagnation_point)
print("\nDivergence (should be 0 for incompressible):", div)
