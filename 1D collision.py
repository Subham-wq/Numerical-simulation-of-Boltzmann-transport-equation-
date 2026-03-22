import numpy as np
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation

# Initial positions
x1, x2 = 0.0, 5.0

# Velocities
v1, v2 = 1.0, -1.0

dt = 0.05
r = 0.2

x1_list = []
x2_list = []

# Simulation
for _ in range(200):
    x1 += v1 * dt
    x2 += v2 * dt

    if abs(x1 - x2) < 2*r:
        v1, v2 = v2, v1

    x1_list.append(x1)
    x2_list.append(x2)

# Animation
fig, ax = plt.subplots()
ax.set_xlim(-1, 6)
ax.set_ylim(-1, 1)

particle1, = ax.plot([], [], 'ro', markersize=12)
particle2, = ax.plot([], [], 'bo', markersize=12)

def update(frame):
    particle1.set_data([x1_list[frame]], [0])
    particle2.set_data([x2_list[frame]], [0])
    return particle1, particle2

anim = FuncAnimation(fig, update, frames=len(x1_list), interval=50)

plt.show()